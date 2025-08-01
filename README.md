<<<<<<< HEAD
# Visual Inspection Popcorn Quality Control

An automated quality control system for popcorn manufacturing using computer vision and YOLO object detection. This project implements real-time visual inspection to classify popcorn quality into good, acceptable, and bad categories.

## Project Overview

Developed for ECEN-631, this system provides automated quality assurance for popcorn production lines by analyzing visual characteristics to determine product quality in real-time.

## Features

### Computer Vision Pipeline
- **Real-time Processing**: Live camera feed analysis for immediate quality assessment
- **YOLO Integration**: State-of-the-art object detection for popcorn classification  
- **Multi-camera Support**: Compatible with both webcams and professional Flea2 cameras
- **Quality Classification**: Three-tier system (good, acceptable/ugly, bad)

### Hardware Integration
- **Flea2 Camera Support**: Professional machine vision camera integration
- **Automated Sorting**: Connected catcher mechanism for physical separation
- **Lab Equipment**: Designed for industrial inspection equipment
- **Flexible Setup**: Configurable for various camera and hardware configurations

## System Components

### Core Files
- `VisualInspection.py` - Main inspection loop and camera interface
- `src/train.py` - YOLO model training pipeline  
- `src/run_inspection.py` - Production inspection runner
- `src/inference_test.py` - Model testing and validation
- `src/Flea2Camera.py` - Professional camera driver interface

### Data Management
- `data/` - Training datasets and annotations
- `runs/` - Model training results and checkpoints
- `video_from_imgs.py` - Video creation from image sequences
=======
# visualInspectionPopcorn
>>>>>>> adbc5ae0658d61b73ba27e6c48175fa21eda03d4
