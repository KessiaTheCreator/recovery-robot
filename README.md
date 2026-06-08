# recovery-robot
A fully offline, localized AI assistant utilizing LLMs and Piper TTS to bring JARVIS to life as an interactive showpiece for addiction recovery education.
# Project JARVIS: Autonomous Recovery Assistant 🤖

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](#license)
[![Platform](https://img.shields.io/badge/Platform-Linux-orange.svg)]()
[![Status](https://img.shields.io/badge/Status-In%20Development-yellow.svg)]()

**Project JARVIS** is an offline, autonomous 6DOF robotic arm equipped with vision sensing, localized AI processing, and a 1:1 custom voice clone. 

Designed specifically as an interactive showpiece for addiction recovery and AA meetings, this robot acts as a localized knowledge base. By utilizing the familiar, trusted voice of JARVIS, the project serves as a psychological Trojan horse—capturing attention and engaging viewers (both in-person and over Zoom) with literature-based insights on addiction psychology, self-improvement, and recovery.

---

## 🎯 The Mission & Psychology
Technology should heal. If a robotic arm simply recites recovery literature, it is merely a tech demo. By giving it an unmistakable, iconic pop-culture voice, it triggers deeply ingrained associations of intelligence, guidance, and safety. This unconscious attunement transforms the hardware into a magnetic, educational centerpiece, bringing joy and active engagement to the collective recovery process.

---

## ⚙️ Architecture & Tech Stack

This project is built to run **100% offline** with zero latency, ensuring complete privacy and reliability without pinging external cloud APIs during operation.

### 🧠 The Brain (Offline LLM & RAG)
* **Engine:** `llama.cpp` / GGUF models.
* **Knowledge Base:** Offline text retrieval (RAG) loaded with AA literature, addiction psychology studies, and recovery research. 

### 🗣️ The Voice Engine (Piper TTS)
* **Model:** Highly optimized `.onnx` custom neural network.
* **Dataset:** Studio-clean Paul Bettany MCU dialogue, meticulously converted to `22050Hz`, 16-bit mono `.wav` format.
* **Execution:** Direct terminal piping for instant, zero-latency audio generation via CPU.

### 👁️ Vision & Hardware
* **Hardware:** 6DOF Autonomous Robotic Arm (vision-enabled, potentially wheeled deployment).
* **Development Environment:** Linux (Crostini) / Intel i5, 16GB RAM architecture.
* **Sensors:** Localized camera tracking for spatial reasoning and audience engagement.

---

## 📁 Repository Structure

```text
recovery-robot/
├── llama.cpp/            # Submoduled offline LLM inference engine
├── voice_engine/         # Piper TTS environment and audio processing
│   ├── wavs/             # Cleaned training dataset (Ignored in Git)
│   └── metadata.csv      # Phonetic transcription mapping
├── knowledge_base/       # RAG documents and recovery literature
├── .gitignore            # Security and file-size shielding
└── README.md
