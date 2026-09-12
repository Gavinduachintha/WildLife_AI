# 🦌 WildLife AI

### Edge AI–Powered Forest Monitoring and Threat Detection System

WildLife AI is an **Edge AI-based forest monitoring system** designed to detect unusual activities and objects in remote forest environments.

The system performs **real-time object detection directly on a Raspberry Pi 5**, using a Raspberry Pi Camera 3 NoIR. When a relevant object is detected, the system obtains its location using GPS and transmits the detection information over **LoRa**.

A **Raspberry Pi Pico 2** acts as the receiving station, receiving the LoRa data and displaying the detected information on a compact IPS display.

The system is designed to monitor objects and activities such as:

* 👤 Humans
* 🔫 Guns
* 🚙 Vehicles
* 🏃 Other unusual activities or objects

The core concept is:

> **Detect locally. Locate accurately. Communicate over long range.**

---

## ✨ Features

* 🧠 Real-time **Edge AI object detection**
* ⚡ AI inference performed directly on **Raspberry Pi 5**
* 📷 Raspberry Pi Camera 3 NoIR wide-angle camera
* 📡 **SX1278 LoRa** long-range communication
* 📍 **NEO-6M GPS** location tracking
* 🔭 Target LoRa communication range of approximately **5–10 km**
* 🖥️ Raspberry Pi Pico 2-based receiving station
* 🎨 135 × 240 color IPS display
* 🌐 Designed for environments with limited internet connectivity
* 🔋 Suitable for remote monitoring applications

---

# 🏗️ System Architecture

```text
                         FOREST ENVIRONMENT
                                │
                  ┌─────────────┴─────────────┐
                  │                           │
             Humans                      Vehicles
             Weapons                    Other Objects
                  │                           │
                  └─────────────┬─────────────┘
                                │
                                ▼
                    ┌─────────────────────┐
                    │ Raspberry Pi Camera │
                    │      3 NoIR          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Raspberry Pi 5    │
                    │                     │
                    │   Image Processing  │
                    │          ↓          │
                    │    Edge AI Model    │
                    │          ↓          │
                    │ Object Detection    │
                    └─────────┬───────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
                    ▼                   ▼
             ┌─────────────┐     ┌─────────────┐
             │   NEO-6M    │     │   SX1278    │
             │     GPS     │     │    LoRa     │
             └──────┬──────┘     └──────┬──────┘
                    │                   │
                    │ Location          │ Alert Data
                    │                   │
                    └─────────┬─────────┘
                              │
                              │
                       ~~~~~ LoRa ~~~~~
                              │
                              ▼
                    ┌─────────────────────┐
                    │   Raspberry Pi Pico │
                    │          2          │
                    │                     │
                    │    LoRa Receiver    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     IPS Display     │
                    │      135 × 240      │
                    └─────────────────────┘
```

---

# 🔩 Hardware

| Component                      | Function                           |
| ------------------------------ | ---------------------------------- |
| **Raspberry Pi 5 2GB**         | Main Edge AI processing unit       |
| **Raspberry Pi Camera 3 NoIR** | Image acquisition                  |
| **SX1278 LoRa**                | Long-range wireless communication  |
| **NEO-6M GPS**                 | GPS location acquisition           |
| **Raspberry Pi Pico 2**        | LoRa receiving station             |
| **135 × 240 IPS Display**      | Detection and status visualization |

---

# 🧠 Edge AI Detection

The main intelligence of WildLife AI runs directly on the **Raspberry Pi 5**.

The camera continuously provides image frames to the AI processing pipeline. The object detection model analyzes the frames and identifies objects of interest.

```text
Camera
   │
   ▼
Image Frame
   │
   ▼
Pre-processing
   │
   ▼
AI Object Detection
   │
   ▼
Detected Object
   │
   ▼
Detection Decision
```

Because the inference is performed locally, the system does not need to continuously upload camera footage to a cloud server.

---

# 📷 Camera System

WildLife AI uses the **Raspberry Pi Camera 3 NoIR wide-angle camera** as its primary visual sensor.

The wide-angle view allows the monitoring node to observe a larger area, while the NoIR configuration makes the camera suitable for low-light applications when appropriate illumination is available.

The camera is connected directly to the Raspberry Pi 5 through the CSI camera interface.

---

# 🧠 Detection Process

When an object is detected, the system extracts the relevant information from the inference result.

For example:

```text
┌────────────────────────────┐
│       DETECTION ALERT      │
├────────────────────────────┤
│ Object      : HUMAN        │
│ Confidence  : 91%          │
│ Latitude    : XX.XXXX      │
│ Longitude   : XX.XXXX      │
│ Status      : ALERT        │
└────────────────────────────┘
```

The detection information is then prepared for transmission.

---

# 📍 GPS Location

The **NEO-6M GPS module** is used to obtain the geographic position of the monitoring node.

The GPS information allows the system to associate a detected event with its physical location.

A detection can therefore contain:

```text
Object
Confidence
Latitude
Longitude
Status
```

This provides more useful information than simply reporting that an object was detected.

---

# 📡 LoRa Communication

WildLife AI uses an **SX1278 LoRa module** to transmit detection information from the remote monitoring node to the receiving station.

The communication architecture is:

```text
Raspberry Pi 5
      │
      ▼
   SX1278
      │
      │  LoRa
      │
      ▼
Raspberry Pi Pico 2
      │
      ▼
 IPS Display
```

The target communication range is approximately:

## **5–10 km**

Actual communication distance depends on factors such as:

* Antenna configuration
* Terrain
* Vegetation
* Obstacles
* Transmit power
* Spreading factor
* Bandwidth
* Receiver sensitivity
* Frequency configuration

Therefore, the stated range represents a target/typical deployment objective rather than a guaranteed distance.

---

# 📦 Detection Data

The Raspberry Pi 5 creates a compact message containing the important information associated with a detection.

Example:

```text
OBJECT=HUMAN
CONF=0.91
LAT=XX.XXXX
LON=XX.XXXX
STATUS=ALERT
```

This information is transmitted through the SX1278 LoRa transmitter.

The Raspberry Pi Pico 2 receives the LoRa packet and processes the information for display.

---

# 🔭 Receiving Station

The receiving side of WildLife AI is built around the **Raspberry Pi Pico 2**.

The Pico 2 receives the LoRa transmission and acts as the interface between the long-range wireless communication system and the display.

```text
                 Raspberry Pi Pico 2
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
        LoRa Receiver          Display Control
              │                     │
              └──────────┬──────────┘
                         │
                         ▼
                  135 × 240 IPS
                     Display
```

The receiving station can display information such as:

* Detected object
* Confidence
* GPS coordinates
* Alert status
* Communication status

---

# 🖥️ Display

A **135 × 240 color IPS display** is used to provide a compact visual interface for the receiving station.

An example display layout is:

```text
╔══════════════════════╗
║     WILDLIFE AI      ║
╠══════════════════════╣
║                      ║
║       ALERT          ║
║                      ║
║ Object : HUMAN       ║
║ Conf.  : 91%         ║
║                      ║
║ LAT : XX.XXXX        ║
║ LON : XX.XXXX        ║
║                      ║
║ LoRa : CONNECTED     ║
╚══════════════════════╝
```

---

# 🔄 Complete System Workflow

The complete WildLife AI workflow is:

```text
┌─────────────────────┐
│  Forest Environment │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Camera 3 NoIR     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Raspberry Pi 5    │
│                     │
│   AI Inference      │
└──────────┬──────────┘
           │
           ▼
    Object Detected?
       │         │
      NO        YES
       │         │
       │         ▼
       │    Read GPS
       │         │
       │         ▼
       │    Create Alert
       │         │
       │         ▼
       │     SX1278 LoRa
       │         │
       │         ▼
       │    ~~~~~~~~~~~
       │      LoRa Link
       │    ~~~~~~~~~~~
       │         │
       │         ▼
       │  Raspberry Pi Pico 2
       │         │
       │         ▼
       │     IPS Display
       │
       └──── Continue
```

---

# 🧩 System Components

## Remote Monitoring Node

The remote node contains:

```text
Raspberry Pi 5
      │
      ├── Raspberry Pi Camera 3 NoIR
      │
      ├── SX1278 LoRa
      │
      └── NEO-6M GPS
```

The Raspberry Pi 5 is responsible for:

1. Capturing images
2. Running AI inference
3. Identifying relevant objects
4. Obtaining GPS information
5. Creating detection messages
6. Transmitting alerts through LoRa

---

## Receiving Node

The receiving node contains:

```text
Raspberry Pi Pico 2
       │
       ├── SX1278 LoRa
       │
       └── 135 × 240 IPS Display
```

The Pico 2 is responsible for:

1. Receiving LoRa packets
2. Processing detection information
3. Updating the display
4. Presenting the received alert information

---

# 🛠️ Software Architecture

The software can be logically divided into four main components:

```text
┌─────────────────────────────┐
│       Camera Module         │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       AI Detection          │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       GPS Module            │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      LoRa Transmitter       │
└──────────────┬──────────────┘
               │
               ▼
          LoRa Link
               │
               ▼
┌─────────────────────────────┐
│      LoRa Receiver          │
│      Raspberry Pi Pico 2    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       IPS Display           │
└─────────────────────────────┘
```

---

# 🚀 Setup

## 1. Clone the Repository

```bash
git clone https://github.com/Gavinduachintha/WildLife-AI.git
cd WildLife-AI
```

## 2. Install Dependencies

Create a Python virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

> The exact dependencies may vary depending on the AI model and software implementation used in the repository.

---

# 📷 Camera Test

After connecting the Raspberry Pi Camera 3 NoIR, verify that the camera is detected:

```bash
rpicam-hello
```

If the camera is functioning correctly, the Raspberry Pi should be able to access the camera stream.

---

# 📍 GPS Configuration

Connect the NEO-6M GPS module to the configured UART interface of the Raspberry Pi 5.

The module provides GPS data through serial communication.

The system uses the received information to obtain:

```text
Latitude
Longitude
```

These coordinates are associated with detection events.

---

# 📡 LoRa Configuration

The SX1278 modules are used for the LoRa communication link.

```text
TRANSMITTER
Raspberry Pi 5
      │
      ▼
   SX1278
      │
      │ LoRa
      ▼
   SX1278
      │
      ▼
Raspberry Pi Pico 2
RECEIVER
```

Both LoRa modules must use compatible radio settings, including:

* Frequency
* Spreading Factor
* Bandwidth
* Coding Rate
* Sync Word

The exact configuration should match the implementation in the source code.

---

# ▶️ Running WildLife AI

Start the main application on the Raspberry Pi 5:

```bash
python main.py
```

The system initializes the required hardware and starts the detection pipeline.

The general startup sequence is:

```text
Initialize Camera
       ↓
Initialize GPS
       ↓
Initialize LoRa
       ↓
Load AI Model
       ↓
Start Detection Loop
```

---

# 🔬 Detection Pipeline

During operation:

```text
1. Capture image
        ↓
2. Process image
        ↓
3. Run AI inference
        ↓
4. Detect target object
        ↓
5. Obtain GPS position
        ↓
6. Generate detection message
        ↓
7. Transmit through LoRa
        ↓
8. Receive using Pico 2
        ↓
9. Display information
```

---

# 🌲 Application

WildLife AI is intended for remote environmental monitoring where conventional internet connectivity may not be available.

Potential monitoring scenarios include:

* Forest surveillance
* Wildlife protection areas
* Restricted forest zones
* Remote environmental monitoring
* Detection of unauthorized human activity
* Remote security monitoring

The system focuses on transmitting **meaningful detection information** instead of continuously transmitting video.

---

# ☁️ Edge AI vs Cloud Processing

A major design decision in WildLife AI is performing inference directly on the Raspberry Pi 5.

### Conventional Cloud-Based System

```text
Camera
   ↓
Internet
   ↓
Cloud
   ↓
AI Model
   ↓
Alert
```

### WildLife AI

```text
Camera
   ↓
Raspberry Pi 5
   ↓
Edge AI
   ↓
Detection
   ↓
LoRa
   ↓
Pico 2
```

This architecture reduces the need for continuous high-bandwidth connectivity.

---

# ⚡ Why LoRa?

Forest environments can have limited cellular and Wi-Fi coverage.

LoRa provides a low-bandwidth, long-range communication method suitable for transmitting compact telemetry and detection information.

WildLife AI therefore separates the system into two layers:

```text
High Computation
       │
       ▼
 Raspberry Pi 5
       │
       │
       │ Small Detection Data
       ▼
      LoRa
       │
       ▼
 Raspberry Pi Pico 2
       │
       ▼
    Display
```

The camera data remains at the monitoring node while the important detection information is transmitted to the receiving station.

---

# ⚙️ Engineering Design

WildLife AI combines several engineering domains:

| Domain                  | Technology                |
| ----------------------- | ------------------------- |
| Edge Computing          | Raspberry Pi 5            |
| Computer Vision         | Camera + Object Detection |
| Artificial Intelligence | Edge AI Model             |
| Embedded Systems        | Raspberry Pi Pico 2       |
| Wireless Communication  | SX1278 LoRa               |
| Positioning             | NEO-6M GPS                |
| Human Interface         | IPS Display               |
| Programming             | Python / Embedded C/C++   |

---

# 📁 Repository Structure

A typical project structure is:

```text
WildLife-AI/
│
├── README.md
├── requirements.txt
│
├── raspberry-pi/
│   ├── main.py
│   ├── detection/
│   ├── gps/
│   └── lora/
│
├── pico2/
│   ├── receiver/
│   ├── lora/
│   └── display/
│
├── model/
│   └── ...
│
├── hardware/
│   ├── wiring/
│   └── schematics/
│
├── images/
│   └── ...
│
└── LICENSE
```

The structure may differ depending on the current implementation.

---

# ⚠️ Limitations

WildLife AI is a prototype/research project.

Detection performance depends on factors such as:

* AI model accuracy
* Training dataset
* Lighting conditions
* Camera position
* Object distance
* Object size
* Occlusion
* Environmental conditions

LoRa performance also depends on:

* Antenna
* Terrain
* Vegetation
* Radio configuration
* Transmit power
* Receiver sensitivity
* Environmental conditions

The **5–10 km range should therefore not be considered a guaranteed operating distance** for every deployment.

---

# 👨‍💻 Author

## Gavindu Achintha

Undergraduate in **Applied Electronics**

Interested in:

* Embedded Systems
* Edge AI
* Robotics
* Computer Vision
* Machine Learning
* Low-Level Programming
* Backend Engineering

### Links

* GitHub: [Gavinduachintha](https://github.com/Gavinduachintha)

---

# 📜 License

This project is provided under the license included in this repository.

See [`LICENSE`](LICENSE) for details.

---

<p align="center">

### 🦌 WildLife AI

**Edge Intelligence for Remote Forest Monitoring**

*See locally. Think locally. Communicate remotely.*

</p>
