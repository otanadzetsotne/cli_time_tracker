# Time Tracker

This repository contains a set of Python scripts designed to help track work time on various projects efficiently. The `app.py` script logs the start and end times of work sessions, manages AFK periods effectively, and the `time_calculator.py` script calculates the total time spent on each project.

## Features

- **Project Tracking**: The `app.py` script logs work sessions for different projects, allowing for easy tracking of time spent on individual tasks.
- **AFK Handling**: It detects and logs times when the user is away from the keyboard (AFK), ensuring these periods do not count towards the total work time.
- **Dynamic Time Calculation**: The `time_calculator.py` script provides functionality to calculate and display the total work time for each project, with options to specify the time calculation starting point (`--since` parameter).

## Requirements

- Python 3.6 or higher
- Compatible with any operating system that supports Python and basic file operations.

## Setup

Ensure Python is installed on your system. If not, download and install it from [python.org](https://www.python.org/downloads/).

## Usage

### app.py
1. Clone this repository or download `app.py` and any related files to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `app.py`.
4. Run the script using the following command:

    ```bash
    python app.py
    ```

5. Follow the on-screen prompts to enter project names and tasks. Use the command `stop` to end the current project session or `change project` to switch to another project.

### time_calculator.py
1. To run the time calculation independently, use the following command in the terminal where `time_calculator.py` is located:

    ```bash
    python time_calculator.py --since [day|midnight|YYYY-MM-DD HH:MM:SS]
    ```

    Replace `[day|midnight|YYYY-MM-DD HH:MM:SS]` with your desired starting point for time calculation. If omitted, the script calculates time for the entire recorded period.

## How it Works

- `app.py` uses the Python `logging` library to create detailed logs of each work session in the `time_tracking.logs` file.
- `time_calculator.py` reads these logs and processes them based on the specified `--since` parameter to compute the total effective work time, excluding any AFK periods.

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request. If you encounter any issues or have suggestions for improvements, feel free to open an issue.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
