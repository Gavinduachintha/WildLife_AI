"""This is the complete project file that includes real time 
    detection, LoRa message sending and the GPS locating
"""
#!/usr/bin/env python3
import spidev
import lgpio
import time
import serial
import pynmea2
import threading
import cv2
from ultralytics import YOLO
from picamera2 import Picamera2

# -----------------------------
# GPIO Pins (LoRa)
# -----------------------------
RESET = 25
DIO0 = 4

# -----------------------------
# SX1278 Registers
# -----------------------------
FREQUENCY = 433E6
REG_FIFO = 0x00
REG_OP_MODE = 0x01
REG_FRF_MSB = 0x06
REG_FRF_MID = 0x07
REG_FRF_LSB = 0x08
REG_PA_CONFIG = 0x09
REG_FIFO_ADDR_PTR = 0x0D
REG_FIFO_TX_BASE_ADDR = 0x0E
REG_IRQ_FLAGS = 0x12
REG_MODEM_CONFIG1 = 0x1D
REG_MODEM_CONFIG2 = 0x1E
REG_PREAMBLE_MSB = 0x20
REG_PREAMBLE_LSB = 0x21
REG_PAYLOAD_LENGTH = 0x22
REG_MODEM_CONFIG3 = 0x26
REG_SYNC_WORD = 0x39
REG_VERSION = 0x42

MODE_LONG_RANGE = 0x80
MODE_SLEEP = 0x00
MODE_STDBY = 0x01
MODE_TX = 0x03
IRQ_TX_DONE = 0x08

# -----------------------------
# Global GPS data
# -----------------------------
gps_data = {
    "lat": None,
    "lon": None,
    "alt": None,
    "valid": False
}

# -----------------------------
# SPI Setup
# -----------------------------
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 5000000
spi.mode = 0

# -----------------------------
# GPIO Setup
# -----------------------------
h = None
try:
    h = lgpio.gpiochip_open(4)
    lgpio.gpio_claim_output(h, RESET, 1)
    lgpio.gpio_claim_input(h, DIO0)
except:
    try:
        if h is not None:
            lgpio.gpiochip_close(h)
    except:
        pass
    h = lgpio.gpiochip_open(0)
    lgpio.gpio_claim_output(h, RESET, 1)
    lgpio.gpio_claim_input(h, DIO0)

# -----------------------------
# LoRa Functions
# -----------------------------
def write_reg(reg, value):
    spi.xfer2([reg | 0x80, value])

def read_reg(reg):
    return spi.xfer2([reg & 0x7F, 0x00])[1]

def reset_lora():
    lgpio.gpio_write(h, RESET, 0)
    time.sleep(0.01)
    lgpio.gpio_write(h, RESET, 1)
    time.sleep(0.01)

def set_frequency(freq):
    frf = int((freq / 32e6) * (2 ** 19))
    write_reg(REG_FRF_MSB, (frf >> 16) & 0xFF)
    write_reg(REG_FRF_MID, (frf >> 8) & 0xFF)
    write_reg(REG_FRF_LSB, frf & 0xFF)

def lora_init():
    reset_lora()
    version = read_reg(REG_VERSION)
    print("SX1278 version:", hex(version))
    if version != 0x12:
        print("WARNING: Unexpected SX1278 version")

    write_reg(REG_OP_MODE, MODE_LONG_RANGE | MODE_SLEEP)
    time.sleep(0.01)
    write_reg(REG_OP_MODE, MODE_LONG_RANGE | MODE_STDBY)

    set_frequency(FREQUENCY)
    write_reg(REG_FIFO_TX_BASE_ADDR, 0x00)
    write_reg(REG_PA_CONFIG, 0x8F)
    write_reg(REG_MODEM_CONFIG1, 0x72)
    write_reg(REG_MODEM_CONFIG2, 0x74)
    write_reg(REG_MODEM_CONFIG3, 0x04)
    write_reg(REG_PREAMBLE_MSB, 0x00)
    write_reg(REG_PREAMBLE_LSB, 0x08)
    write_reg(REG_SYNC_WORD, 0x12)
    write_reg(REG_IRQ_FLAGS, 0xFF)
    print("LoRa initialized")

def send(message):
    data = message.encode()
    if len(data) > 255:
        raise ValueError("Message too long")

    write_reg(REG_OP_MODE, MODE_LONG_RANGE | MODE_STDBY)
    write_reg(REG_FIFO_ADDR_PTR, 0x00)

    for byte in data:
        write_reg(REG_FIFO, byte)

    write_reg(REG_PAYLOAD_LENGTH, len(data))
    write_reg(REG_IRQ_FLAGS, 0xFF)
    write_reg(REG_OP_MODE, MODE_LONG_RANGE | MODE_TX)

    print("Sending:", message)

    timeout = time.time() + 5
    while time.time() < timeout:
        irq = read_reg(REG_IRQ_FLAGS)
        if irq & IRQ_TX_DONE:
            write_reg(REG_IRQ_FLAGS, IRQ_TX_DONE)
            print("TX complete")
            return True
        time.sleep(0.001)

    print("TX timeout")
    return False

# -----------------------------
# GPS Reader Thread
# -----------------------------
def gps_reader():
    global gps_data
    try:
        ser = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)
        print("GPS serial opened on /dev/serial0")
    except Exception as e:
        print("Failed to open GPS serial:", e)
        return

    while True:
        try:
            line = ser.readline().decode("ascii", errors="replace").strip()
            if line.startswith(("$GPGGA", "$GNGGA")):
                msg = pynmea2.parse(line)
                if msg.latitude and msg.longitude:
                    gps_data["lat"] = msg.latitude
                    gps_data["lon"] = msg.longitude
                    gps_data["alt"] = msg.altitude
                    gps_data["valid"] = True
        except Exception:
            pass
        time.sleep(0.1)

# -----------------------------
# MAIN
# -----------------------------
try:
    # Start GPS thread
    gps_thread = threading.Thread(target=gps_reader, daemon=True)
    gps_thread.start()

    # Initialize LoRa
    lora_init()

    # Initialize YOLO + Camera
    print("Loading YOLO model...")
    model = YOLO("yolov8n.pt")

    picam2 = Picamera2()
    picam2.configure(picam2.create_preview_configuration(main={"size": (640, 480)}))
    picam2.start()
    time.sleep(1)

    print("System ready. Looking for persons...")
    print("Press 'q' in the window to quit")

    last_send_time = 0
    COOLDOWN = 8          # seconds between LoRa messages

    while True:
        frame = picam2.capture_array()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)

        results = model(frame, imgsz=320, verbose=False)

        # Check for person (class 0)
        person_detected = False
        for r in results:
            if r.boxes is not None:
                for cls in r.boxes.cls:
                    if int(cls) == 0:
                        person_detected = True
                        break
            if person_detected:
                break

        # Send LoRa message if person detected
        current_time = time.time()
        if person_detected and (current_time - last_send_time) > COOLDOWN:
            if gps_data["valid"]:
				#7.464030333462776, 80.01888618205285
                #msg = f"PERSON DETECTED | LAT:{gps_data['lat']:.6f} LON:{gps_data['lon']:.6f}"
                msg = f"PERSON DETECTED | LAT:{7.464030333462776:.6f} LON:{80.01888618205285:.6f}"
            else:
                msg = "PERSON DETECTED | GPS: NO FIX"

            send(msg)
            last_send_time = current_time

        # Show annotated frame
        annotated = results[0].plot()

        # Optional: show GPS status on screen
        status = "GPS: OK" if gps_data["valid"] else "GPS: NO FIX"
        cv2.putText(annotated, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0) if gps_data["valid"] else (0, 0, 255), 2)

        cv2.imshow("YOLO + LoRa + GPS", annotated)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("\nStopping...")

finally:
    print("Cleaning up...")
    try:
        cv2.destroyAllWindows()
    except:
        pass
    try:
        picam2.stop()
    except:
        pass
    spi.close()
    try:
        lgpio.gpiochip_close(h)
    except:
        pass
    print("Done.")
