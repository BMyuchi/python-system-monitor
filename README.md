
# Python System Monitor

A lightweight command-line system monitoring tool built with Python and psutil.

## Features

- Monitor CPU usage in real time
- Monitor RAM usage in real time
- Classify usage levels as Normal, Moderate, or High
- Update system metrics approximately every second
- Stop monitoring gracefully using Ctrl+C

## Technologies

- Python
- psutil

## Requirements

- Python 3
- pip

## Installation

1. Clone the repository or download the project files.

2. Create a virtual environment:

   ```powershell
   python -m venv .venv
   ```

3. Activate the virtual environment (Windows PowerShell):

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

4. Install the required dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

# Usage 

1. Run the monitor

    ```powershell
    python monitor.py
    ```

2. The program displays CPU and RAM usage with their status:

    ```text
    CPU Usage: 22.8 %
    CPU Status: Normal
    RAM Usage: 53.2 %
    RAM Status: Moderate
    -----------------------------
    ```

3. Stop the monitor by pressing `Ctrl + C`.

The monitoring results are updated approximately every second.