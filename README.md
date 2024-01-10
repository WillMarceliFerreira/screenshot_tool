
# Screen Capture Tool

## Introduction

This document provides an overview and usage instructions for a Python-based screen capture tool. The script utilizes **PySimpleGUI** for the graphical user interface, **pyautogui** for taking screenshots, **threading** for concurrent execution, and **keyboard** for monitoring keyboard events.

##Features
- **Graphical User Interface:** Simple and user-friendly interface for capturing screenshots.
- **Keyboard Shortcut:** Use F9 key to capture screenshots without interacting with the GUI.
- **Threaded Monitoring:** Runs a background thread to listen for keyboard events without blocking the main GUI.

## Requirements
- Python 3.x
- PySimpleGUI
- pyautogui
- threading
- keyboard
- Installation

Ensure Python 3.x is installed on your system. You can install the required packages using pip:

```bash
pip install PySimpleGUI pyautogui keyboard
```

## Usage
- Launch the script.
- Use the GUI button "Capture Screen" or press the F9 key to capture a screenshot.
- Captured screenshots are saved in the current directory with the naming format **screenshot_{image_count}.png**.
T- o exit, close the GUI window or click the "Exit" button.

## How It Works
1. **Capture Function:** Takes a screenshot and saves it with an incremental count.
2. **Keyboard Monitor:** A separate thread that listens for the F9 keypress to trigger a screenshot.
3. **GUI Layout:** Contains a button to capture the screen, an exit button, and a status text area.
4. **Event Loop:** Handles GUI events and triggers screenshot capture.

## Limitations
- The tool currently only supports capturing the entire screen.
- It is necessary to manually manage the screenshots as they accumulate in the current directory.