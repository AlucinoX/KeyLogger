# Keylogger with Graphical Interface in Kivy

This is a keylogger project developed in Python, with a graphical interface built using the Kivy framework. The keylogger records keystrokes on the system and stores them in a file, with an encryption option. This project includes a user-friendly interface to start/stop the keylogger and clear the logs.

> **Legal Notice**: This project is for educational purposes only and should be used ethically and legally. Ensure you have explicit permission to log keystrokes on any device where you use this software.

## Features

- Records keystrokes on the system.
- Encrypts logs using the `cryptography` library.
- Graphical interface in Kivy for easy control.
- Option to clear logs through the interface.
- Stores logs in a file with automatic rotation (10 MB limit).

## Technologies Used

- Python
- Kivy
- Cryptography
- Pynput

## Prerequisites

- Python 3.x
- Pip

## Installation

1. Clone this repository to your local computer:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```
2. Navigate to the project directory:
    ```bash
    cd your-repository
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
   > If the `requirements.txt` file is not available, install the libraries manually:
    ```bash
    pip install kivy cryptography pynput
    ```

## How to Use

1. Run the application:
    ```bash
    python keylogger_kivy.py
    ```
2. Use the graphical interface to:
   - Start the keylogger (Click on "Start Logger").
   - Stop the keylogger (Click on "Stop Logger").
   - Clear the logs (Click on "Clear Logs").

3. The logs will be stored in the `keystrokes.txt` file.

## Project Structure

- `keylogger_kivy.py`: Main application script with the graphical interface.
- `keystrokes.txt`: File where recorded keystrokes are stored (automatically created).

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request with improvements, bug fixes, or new features.

#
### QUACK!!
