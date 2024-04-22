# Time Tracker

This repository contains a simple Python script (`app.py`) designed to help track work time on various projects. The script logs the start and end times of your work sessions, handles pauses (AFK periods), and calculates the total time spent on each project.

## Features

- **Project Tracking**: Logs work sessions for different projects.
- **AFK Handling**: Detects and logs AFK times that should not count towards the total work time.
- **Work Time Calculation**: Calculates and displays the total work time for each project.

## Requirements

- Python 3.6+
- Operating system with support for Python and basic file operations.

## Setup

To run this script, you need to have Python installed on your machine. You can download and install Python from [python.org](https://www.python.org/downloads/).

## Usage

1. Clone this repository or download `app.py` to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where `app.py` is located.
4. Run the script using Python:

    ```bash
    python app.py
    ```

5. Follow the on-screen prompts to enter project names and tasks. Type `stop` to end the current project session or `change project` to switch to a different project.

## How it Works

- The script uses the Python `logging` library to record work sessions in a log file (`time_tracking.logs`).
- Each entry in the log records a timestamp and a message about the task or session status (start, stop, AFK start/stop).
- The script reads the log file to calculate the total work time, subtracting any AFK periods.

## Contributing

Feel free to fork this repository, make changes, and submit pull requests. If you find any issues or have suggestions for improvements, please open an issue.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

