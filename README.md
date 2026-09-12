<div align="center">

# 🦌 WildLife AI

### _Edge AI–Powered Forest Monitoring and Threat Detection System_

[![Edge AI](https://img.shields.io/badge/Edge-AI-green.svg)](https://github.com/Gavinduachintha/WildLife-AI)
[![Raspberry Pi](https://img.shields.io/badge/Raspberry-Pi%205-red.svg)](https://www.raspberrypi.com/)
[![LoRa](https://img.shields.io/badge/LoRa-SX1278-blue.svg)](https://www.semtech.com/)

</div>

---

## 🎯 Overview

**WildLife AI** is an Edge AI-based forest monitoring system designed to detect unusual activities and objects in remote forest environments.

The system performs **real-time object detection directly on a Raspberry Pi 5**, using a Raspberry Pi Camera 3 NoIR. When a relevant object is detected, the system obtains its location using GPS and transmits the detection information over **LoRa**.

A **Raspberry Pi Pico 2** acts as the receiving station, receiving the LoRa data and displaying the detected information on a compact IPS display.

### 🎯 Monitored Objects & Activities

<table>
  <tr>
    <td align="center">👤<br><b>Humans</b></td>
    <td align="center">🔫<br><b>Guns</b></td>
    <td align="center">🚙<br><b>Vehicles</b></td>
    <td align="center">🏃<br><b>Unusual Activities</b></td>
  </tr>
</table>

### 💡 Core Concept

> **Detect locally. Locate accurately. Communicate over long range.**

---

## ✨ Key Features

<table>
  <tr>
    <td width="50%">
      <h3>🧠 Edge Intelligence</h3>
      <ul>
        <li>Real-time Edge AI object detection</li>
        <li>AI inference on <b>Raspberry Pi 5</b></li>
        <li>Local processing, no cloud dependency</li>
      </ul>
    </td>
    <td width="50%">
      <h3>📡 Communication</h3>
      <ul>
        <li><b>SX1278 LoRa</b> long-range wireless</li>
        <li><b>5–10 km</b> communication range</li>
        <li>Low bandwidth, high reliability</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <h3>📷 Vision System</h3>
      <ul>
        <li>Raspberry Pi Camera 3 NoIR</li>
        <li>Wide-angle monitoring</li>
        <li>Low-light capability</li>
      </ul>
    </td>
    <td>
      <h3>📍 Location Services</h3>
      <ul>
        <li><b>NEO-6M GPS</b> tracking</li>
        <li>Precise geolocation tagging</li>
        <li>Event position logging</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <h3>🖥️ Display Station</h3>
      <ul>
        <li>Raspberry Pi Pico 2 receiver</li>
        <li><b>135 × 240</b> color IPS display</li>
        <li>Real-time alert visualization</li>
      </ul>
    </td>
    <td>
      <h3>🌐 Remote Ready</h3>
      <ul>
        <li>Limited internet connectivity</li>
        <li>Battery-powered deployment</li>
        <li>Off-grid monitoring capable</li>
      </ul>
    </td>
  </tr>
</table>

---

<br>

## 🏗️ System Architecture

<div align="center">

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

</div>

<br>

---

## 🔩 Hardware Components

<div align="center">

|             Component             | Function                           |
| :-------------------------------: | :--------------------------------- |
|     🖥️ **Raspberry Pi 5 2GB**     | Main Edge AI processing unit       |
| 📷 **Raspberry Pi Camera 3 NoIR** | Image acquisition                  |
|        📡 **SX1278 LoRa**         | Long-range wireless communication  |
|         📍 **NEO-6M GPS**         | GPS location acquisition           |
|    🎛️ **Raspberry Pi Pico 2**     | LoRa receiving station             |
|   🖥️ **135 × 240 IPS Display**    | Detection and status visualization |

</div>

---

---

## 🧠 Edge AI Detection

> The main intelligence of WildLife AI runs directly on the **Raspberry Pi 5**.

The camera continuously provides image frames to the AI processing pipeline. The object detection model analyzes the frames and identifies objects of interest.

<div align="center">

```text
    📷 Camera
        │
        ▼
   🖼️ Image Frame
        │
        ▼
   ⚙️ Pre-processing
        │
        ▼
   🤖 AI Object Detection
        │
        ▼
   🎯 Detected Object
        │
        ▼
   ✅ Detection Decision
```

</div>

**Key Advantage:** Because the inference is performed locally, the system does not need to continuously upload camera footage to a cloud server.

---

---

## 📷 Camera System

**WildLife AI** uses the **Raspberry Pi Camera 3 NoIR wide-angle camera** as its primary visual sensor.

<table>
  <tr>
    <td width="50%">
      <b>📐 Wide-Angle View</b><br>
      Allows the monitoring node to observe a larger area
    </td>
    <td width="50%">
      <b>🌙 NoIR Configuration</b><br>
      Suitable for low-light applications with appropriate illumination
    </td>
  </tr>
</table>

**Connection:** The camera is connected directly to the Raspberry Pi 5 through the CSI camera interface.

---

---

## 🎯 Detection Process

When an object is detected, the system extracts the relevant information from the inference result.

### Example Detection Alert

<div align="center">

```text
┌────────────────────────────┐
│    🚨 DETECTION ALERT      │
├────────────────────────────┤
│ Object      : HUMAN        │
│ Confidence  : 91%          │
│ Latitude    : XX.XXXX      │
│ Longitude   : XX.XXXX      │
│ Status      : ALERT        │
└────────────────────────────┘
```

</div>

The detection information is then prepared for transmission.

---

---

## 📍 GPS Location

The **NEO-6M GPS module** obtains the geographic position of the monitoring node.

The GPS information allows the system to associate a detected event with its physical location.

### Detection Data Structure

<div align="center">

```text
📦 Detection Packet
├── 🎯 Object
├── 📊 Confidence
├── 🌍 Latitude
├── 🌎 Longitude
└── ⚠️ Status
```

</div>

This provides more useful information than simply reporting that an object was detected.

---

---

## 📡 LoRa Communication

**WildLife AI** uses an **SX1278 LoRa module** to transmit detection information from the remote monitoring node to the receiving station.

### Communication Architecture

<div align="center">

```text
  Raspberry Pi 5
        │
        ▼
    SX1278
        │
        │  📡 LoRa
        │
        ▼
Raspberry Pi Pico 2
        │
        ▼
   IPS Display
```

</div>

### 🎯 Target Communication Range

<div align="center">

## **5–10 km**

</div>

<details>
<summary><b>📊 Factors Affecting Range</b></summary>

Actual communication distance depends on:

- 📡 Antenna configuration
- 🏔️ Terrain
- 🌳 Vegetation
- 🧱 Obstacles
- ⚡ Transmit power
- 📶 Spreading factor
- 📊 Bandwidth
- 🎛️ Receiver sensitivity
- 📻 Frequency configuration

</details>

> **Note:** The stated range represents a target/typical deployment objective rather than a guaranteed distance.

---

---

## 📦 Detection Data Format

The Raspberry Pi 5 creates a compact message containing the important information associated with a detection.

### Example Transmission

<div align="center">

```text
OBJECT=HUMAN
CONF=0.91
LAT=XX.XXXX
LON=XX.XXXX
STATUS=ALERT
```

</div>

**Transmission Flow:**

1. 📤 Information transmitted through the SX1278 LoRa transmitter
2. 📡 Signal travels over long-range LoRa link
3. 📥 Raspberry Pi Pico 2 receives the LoRa packet
4. ⚙️ Data processed for display

---

---

## 🔭 Receiving Station

The receiving side of **WildLife AI** is built around the **Raspberry Pi Pico 2**.

The Pico 2 receives the LoRa transmission and acts as the interface between the long-range wireless communication system and the display.

<div align="center">

```text
         Raspberry Pi Pico 2
                 │
      ┌──────────┴──────────┐
      │                     │
      ▼                     ▼
📡 LoRa Receiver    🖥️ Display Control
      │                     │
      └──────────┬──────────┘
                 │
                 ▼
          135 × 240 IPS
             Display
```

</div>

### 📊 Display Capabilities

The receiving station can display:

- 🎯 Detected object type
- 📊 Confidence percentage
- 📍 GPS coordinates
- ⚠️ Alert status
- 📡 Communication status

---

---

## 🖥️ Display Interface

A **135 × 240 color IPS display** provides a compact visual interface for the receiving station.

### Example Display Layout

<div align="center">

```text
╔══════════════════════╗
║   🦌 WILDLIFE AI     ║
╠══════════════════════╣
║                      ║
║      🚨 ALERT        ║
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

</div>

---

---

## 🔄 Complete System Workflow

<div align="center">

```text
┌─────────────────────┐
│  🌲 Forest Environment │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  📷 Camera 3 NoIR   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  🖥️ Raspberry Pi 5   │
│                     │
│  🤖 AI Inference     │
└──────────┬──────────┘
           │
           ▼
    ❓ Object Detected?
       │         │
      NO        YES
       │         │
       │         ▼
       │    📍 Read GPS
       │         │
       │         ▼
       │   🚨 Create Alert
       │         │
       │         ▼
       │  📡 SX1278 LoRa
       │         │
       │         ▼
       │    ~~~~~~~~~~~
       │    📡 LoRa Link
       │    ~~~~~~~~~~~
       │         │
       │         ▼
       │  🎛️ Raspberry Pi Pico 2
       │         │
       │         ▼
       │   🖥️ IPS Display
       │
       └──── 🔄 Continue
```

</div>

---

---

## 🧩 System Components

### 📡 Remote Monitoring Node

<div align="center">

```text
🖥️ Raspberry Pi 5
      │
      ├── 📷 Raspberry Pi Camera 3 NoIR
      │
      ├── 📡 SX1278 LoRa
      │
      └── 📍 NEO-6M GPS
```

</div>

**Responsibilities:**

1. 📸 Capturing images
2. 🤖 Running AI inference
3. 🎯 Identifying relevant objects
4. 📍 Obtaining GPS information
5. 📝 Creating detection messages
6. 📤 Transmitting alerts through LoRa

### 📥 Receiving Node

<div align="center">

```text
🎛️ Raspberry Pi Pico 2
       │
       ├── 📡 SX1278 LoRa
       │
       └── 🖥️ 135 × 240 IPS Display
```

</div>

**Responsibilities:**

1. 📥 Receiving LoRa packets
2. ⚙️ Processing detection information
3. 🔄 Updating the display
4. 📊 Presenting the received alert information

---

---

## 🛠️ Software Architecture

The software is logically divided into four main components:

<div align="center">

```text
┌─────────────────────────────┐
│    📷 Camera Module         │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    🤖 AI Detection          │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    📍 GPS Module            │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│   📤 LoRa Transmitter       │
└──────────────┬──────────────┘
               │
               ▼
         📡 LoRa Link
               │
               ▼
┌─────────────────────────────┐
│   📥 LoRa Receiver          │
│   🎛️ Raspberry Pi Pico 2    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    🖥️ IPS Display           │
└─────────────────────────────┘
```

</div>

---

---

## 🚀 Getting Started

### Step 1: Clone the Repository

```bash
git clone https://github.com/Gavinduachintha/WildLife-AI.git
cd WildLife-AI
```

### Step 2: Install Dependencies

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

> 💡 **Note:** The exact dependencies may vary depending on the AI model and software implementation used in the repository.

---

---

## 📷 Camera Test

After connecting the Raspberry Pi Camera 3 NoIR, verify that the camera is detected:

```bash
rpicam-hello
```

✅ If the camera is functioning correctly, the Raspberry Pi should be able to access the camera stream.

---

---

## 📍 GPS Configuration

Connect the **NEO-6M GPS module** to the configured UART interface of the Raspberry Pi 5.

The module provides GPS data through serial communication.

### 📊 Data Obtained

<div align="center">

```text
🌍 Latitude
🌎 Longitude
```

</div>

These coordinates are associated with detection events.

---

---

## 📡 LoRa Configuration

The **SX1278 modules** are used for the LoRa communication link.

<div align="center">

```text
    TRANSMITTER
  Raspberry Pi 5
        │
        ▼
     SX1278
        │
        │ 📡 LoRa
        ▼
     SX1278
        │
        ▼
Raspberry Pi Pico 2
     RECEIVER
```

</div>

### ⚙️ Compatible Radio Settings

Both LoRa modules must use compatible settings:

- 📻 **Frequency**
- 📶 **Spreading Factor**
- 📊 **Bandwidth**
- 🔢 **Coding Rate**
- 🔄 **Sync Word**

> 💡 **Note:** The exact configuration should match the implementation in the source code.

---

---

## ▶️ Running WildLife AI

Start the main application on the Raspberry Pi 5:

```bash
python main.py
```

The system initializes the required hardware and starts the detection pipeline.

### 🔄 Startup Sequence

<div align="center">

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

</div>

---

---

## 🔬 Detection Pipeline

### Operational Flow

<div align="center">

```text
1. 📸 Capture image
        ↓
2. ⚙️ Process image
        ↓
3. 🤖 Run AI inference
        ↓
4. 🎯 Detect target object
        ↓
5. 📍 Obtain GPS position
        ↓
6. 📝 Generate detection message
        ↓
7. 📡 Transmit through LoRa
        ↓
8. 📥 Receive using Pico 2
        ↓
9. 🖥️ Display information
```

</div>

---

---

## 🌲 Application Scenarios

**WildLife AI** is intended for remote environmental monitoring where conventional internet connectivity may not be available.

### 🎯 Use Cases

<table>
  <tr>
    <td align="center">🌳<br><b>Forest Surveillance</b></td>
    <td align="center">🦌<br><b>Wildlife Protection</b></td>
    <td align="center">🚫<br><b>Restricted Zones</b></td>
  </tr>
  <tr>
    <td align="center">🌲<br><b>Environmental Monitoring</b></td>
    <td align="center">👤<br><b>Unauthorized Activity</b></td>
    <td align="center">🔒<br><b>Remote Security</b></td>
  </tr>
</table>

### 💡 Key Advantage

> The system focuses on transmitting **meaningful detection information** instead of continuously transmitting video.

---

---

## ☁️ Edge AI vs Cloud Processing

A major design decision in **WildLife AI** is performing inference directly on the Raspberry Pi 5.

<table>
  <tr>
    <th width="50%">🌐 Conventional Cloud-Based System</th>
    <th width="50%">⚡ WildLife AI (Edge)</th>
  </tr>
  <tr>
    <td>
      <pre>
Camera
   ↓
Internet
   ↓
Cloud
   ↓
AI Model
   ↓
Alert
      </pre>
    </td>
    <td>
      <pre>
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
      </pre>
    </td>
  </tr>
</table>

### ✅ Benefits

This architecture **reduces the need for continuous high-bandwidth connectivity**.

---

---

## ⚡ Why LoRa?

Forest environments can have limited cellular and Wi-Fi coverage.

**LoRa** provides a low-bandwidth, long-range communication method suitable for transmitting compact telemetry and detection information.

### 🏗️ System Architecture

**WildLife AI** separates the system into two layers:

<div align="center">

```text
  High Computation
         │
         ▼
   Raspberry Pi 5
         │
         │
         │ 📦 Small Detection Data
         ▼
        LoRa
         │
         ▼
 Raspberry Pi Pico 2
         │
         ▼
      Display
```

</div>

> 💡 The camera data remains at the monitoring node while the important detection information is transmitted to the receiving station.

---

---

## ⚙️ Engineering Design

**WildLife AI** combines several engineering domains:

<div align="center">

| Domain                         | Technology                |
| :----------------------------- | :------------------------ |
| ⚡ **Edge Computing**          | Raspberry Pi 5            |
| 👁️ **Computer Vision**         | Camera + Object Detection |
| 🤖 **Artificial Intelligence** | Edge AI Model             |
| 🔧 **Embedded Systems**        | Raspberry Pi Pico 2       |
| 📡 **Wireless Communication**  | SX1278 LoRa               |
| 📍 **Positioning**             | NEO-6M GPS                |
| 🖥️ **Human Interface**         | IPS Display               |
| 💻 **Programming**             | Python / Embedded C/C++   |

</div>

---

---

## 📁 Repository Structure

<div align="center">

```text
📂 WildLife-AI/
│
├── 📄 README.md
├── 📄 requirements.txt
│
├── 📂 raspberry-pi/
│   ├── 🐍 main.py
│   ├── 📂 detection/
│   ├── 📂 gps/
│   └── 📂 lora/
│
├── 📂 pico2/
│   ├── 📂 receiver/
│   ├── 📂 lora/
│   └── 📂 display/
│
├── 📂 model/
│   └── ...
│
├── 📂 hardware/
│   ├── 📂 wiring/
│   └── 📂 schematics/
│
├── 📂 images/
│   └── ...
│
└── 📄 LICENSE
```

</div>

> 💡 **Note:** The structure may differ depending on the current implementation.

---

---

## ⚠️ Limitations & Considerations

> **WildLife AI** is a prototype/research project.

### 🎯 Detection Performance Factors

<details>
<summary><b>Click to expand factors affecting detection accuracy</b></summary>

- 🤖 AI model accuracy
- 📊 Training dataset
- 💡 Lighting conditions
- 📷 Camera position
- 📏 Object distance
- 📐 Object size
- 🚧 Occlusion
- 🌦️ Environmental conditions

</details>

### 📡 LoRa Performance Factors

<details>
<summary><b>Click to expand factors affecting communication range</b></summary>

- 📡 Antenna
- 🏔️ Terrain
- 🌳 Vegetation
- ⚙️ Radio configuration
- ⚡ Transmit power
- 📶 Receiver sensitivity
- 🌦️ Environmental conditions

</details>

> ⚠️ **Important:** The **5–10 km range should not be considered a guaranteed operating distance** for every deployment.

---

---

## 👨‍💻 Author

<div align="center">

### Gavindu Achintha

\*Undergraduate in **Applied Electronics\***

</div>

### 🎯 Interests

<table>
  <tr>
    <td align="center">🔧<br><b>Embedded Systems</b></td>
    <td align="center">🤖<br><b>Edge AI</b></td>
    <td align="center">🦾<br><b>Robotics</b></td>
  </tr>
  <tr>
    <td align="center">👁️<br><b>Computer Vision</b></td>
    <td align="center">📊<br><b>Machine Learning</b></td>
    <td align="center">⚙️<br><b>Low-Level Programming</b></td>
  </tr>
  <tr>
    <td align="center" colspan="3">🌐<br><b>Backend Engineering</b></td>
  </tr>
</table>

<div align="center">

### 🔗 Connect

[![GitHub](https://img.shields.io/badge/GitHub-Gavinduachintha-181717?style=for-the-badge&logo=github)](https://github.com/Gavinduachintha)

</div>

---

---

<div align="center">

## 📜 License

This project is provided under the license included in this repository.

See [`LICENSE`](LICENSE) for details.

</div>

---

<div align="center">

<br>

# 🦌 WildLife AI

### **Edge Intelligence for Remote Forest Monitoring**

_See locally. Think locally. Communicate remotely._

<br>

**[⭐ Star this project](https://github.com/Gavinduachintha/WildLife-AI)** • **[🐛 Report Bug]([https://github.com/Gavinduachintha/WildLife-AI/issues](https://github.com/Gavinduachintha/WildLife_AI/issues))** • **[💡 Request Feature](https://github.com/Gavinduachintha/WildLife-AI/issues)**

---

Made with ❤️ for Wildlife Protection

</div>
