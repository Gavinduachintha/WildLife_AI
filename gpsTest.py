#!/usr/bin/env python3
import serial
import pynmea2
import time

print("Starting GPS test... (Ctrl+C to stop)")
print("Waiting for satellite fix (may take 30-90 seconds outdoors)...\n")

ser = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)

try:
    while True:
        line = ser.readline().decode("ascii", errors="replace").strip()
        
        if line.startswith(("$GPGGA", "$GNGGA")):
            try:
                msg = pynmea2.parse(line)
                if msg.latitude and msg.longitude:
                    print(f"Latitude : {msg.latitude:.6f}")
                    print(f"Longitude: {msg.longitude:.6f}")
                    print(f"Altitude : {msg.altitude} m")
                    print(f"Satellites: {msg.num_sats}")
                    print("-" * 40)
                else:
                    print("No fix yet...")
            except pynmea2.ParseError:
                pass
                
except KeyboardInterrupt:
    print("\nStopped.")
finally:
    ser.close()