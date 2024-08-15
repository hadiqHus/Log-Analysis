# Process Event Logger with Python

## Overview

This project is a Python script that continuously monitors process events on a Windows machine. It logs when processes start and terminate, including details such as process ID, name, and command line arguments. The logs are stored in a CSV file for easy analysis.

## Features

- **Real-time Process Monitoring:** Logs both the start and termination of processes in real-time.
- **Handles Permission Errors Gracefully:** If access to a process is denied, the script logs an "Access Denied" message and continues running.
- **File Access Management:** If the log file is open in another program (like Excel), the script pauses and retries writing until the file is available.
- **CSV Log Format:** Logs are stored in a human-readable CSV file, making it easy to analyze process activity.

## Prerequisites

- **Python 3.x** installed on your machine.
- Required Python libraries:
  - `psutil`
  - `pandas`
  - `keyboard`

You can install the necessary libraries using pip:

```bash
pip install psutil pandas keyboard


## Example
![image](https://github.com/user-attachments/assets/7c0d1553-c139-4430-97b4-a727350c8571)
