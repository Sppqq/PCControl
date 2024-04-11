## PC Control Server - README

**Table of Contents**

* [Introduction](#introduction)
* [Features](#features)
* [Requirements](#requirements)
* [Getting Started](#getting-started)
* [Usage](#usage)
    * [Sending Messages](#sending-messages)
    * [Controlling PC Actions](#controlling-pc-actions)
* [Files](#files)
* [Security](#security)
* [Additional Notes](#additional-notes)
* [Disclaimer](#disclaimer)

## Introduction

This project provides a way to control your PC remotely using HTTP requests. You can send messages to display on your PC or trigger actions like shutdown, restart, or opening a URL. This can be useful for a variety of purposes, such as:

* **Remotely checking on your PC's status.**
* **Sending yourself reminders or notes.**
* **Shutting down or restarting your PC without being physically present.**
* **Automating tasks or integrating with other services.**

## Features

* **Send messages to your PC:** Display toast notifications with custom messages from any device capable of sending HTTP POST requests.
* **Control PC actions:** Trigger shutdown, restart, or hibernation remotely.
* **Customizable:** Configure the password, server port, and enable/disable toast notifications.
* **Start on boot:** Option to automatically start the server when your PC boots up.
* **Apple Shortcut integration:** Obtain your local IP address for use with an Apple Shortcut to control your PC from your iPhone.

## Requirements

* **Python 3.x:** Ensure you have Python 3 installed on your system.
* **Required libraries:** Install the necessary libraries using the command "pip install -r requirements.txt". The required libraries are:
    * `win11toast`: For displaying toast notifications.
    * `http`: For creating the HTTP server.
    * `socketserver`: For handling network connections.
    * `json`: For working with JSON data.
    * `webbrowser`: For opening URLs.
    * `colorama`: For colored terminal output (optional, for first-time configuration).
    * `winreg`: For adding the server to startup (optional).
    * `requests`: For network communication (optional, for testing).

## Getting Started

1. **Clone the repository:** Use the command `git clone https://github.com/Sppqq/PCControl` to download the project files to your PC.
2. **Install dependencies:** Navigate to the project directory and run `pip install -r requirements.txt` to install the required libraries.
3. **Run the start tray script:** Execute "python start_tray.py" to start the server and create a tray icon for control.

![Tray Icon](https://cdn.discordapp.com/attachments/1045023444980473958/1226890642555146300/image.png?ex=662669f3&is=6613f4f3&hm=1ba37e2955dcd0405e59918dc638dc0b83db870362da882b5cc90cdd8774d4c2&)

4. **Configure settings (First Run):**
    * You'll be prompted to configure options like:
        * **Password:** Change the default password for security.
        * **Port:** Choose the port on which the server will listen.
        * **Toasts:** Enable or disable toast notifications.
        * **Startup:** Add the server to startup for automatic launch on boot.
        * **Apple Shortcut:** Get your local IP address for use with an Apple Shortcut.
5. **Start the server:** The server will start automatically after configuration or on subsequent runs.

## Usage

### Sending Messages

1. **Prepare the JSON data:** Create a JSON object with the following structure:

```json
{
    "password": "YOUR_PASSWORD",
    "text": "This is the message to display"
}
```

2. **Send an HTTP POST request:** Use any tool or programming language capable of sending HTTP requests to send a POST request to your server's address (e.g., `http://localhost:10000/`).
    * Make sure to include the JSON data in the request body.
3. **Receive the message on your PC:** If the password is correct, a toast notification will appear on your PC displaying the message.

### Controlling PC Actions

1. **Prepare the JSON data:** Similar to sending messages, create a JSON object with your password and a specific keyword in the "text" field to trigger an action:

```json
{
    "password": "YOUR_PASSWORD",
    "text": "shutdown"
}
```

2. **Send the HTTP POST request:** Send the POST request with the JSON data as described in the previous section.
3. **PC performs the action:** Depending on the keyword used, your PC will:
    * **`shutdown`**: Shut down the PC.
    * **`restart`**: Restart the PC.
    * **`hb`**: Hibernate the PC.
    * **`br`**: Open a predefined URL in your web browser (configurable in "server.py").

## Files

* **start_tray.py:** Starts the server and creates a tray icon for control.
* **tray.py:** Manages the tray icon and its menu options (currently only "Exit").
* **server.py:** Implements the core HTTP server functionality and handles incoming requests.
* **stop.py:** Provides a way to stop the running server process.
* **config.json:** Stores the server's configuration settings, including password, port, and toast preferences.
* **requirements.txt:** Lists the required Python libraries for installation.

## Security

* **Change the default password!** This is crucial to prevent unauthorized access to your PC.
* **Use a strong password:** Choose a complex password that is difficult to guess.
* **Be cautious about exposing your server to the public internet:** Only run the server on a trusted network or take additional security measures if exposing it publicly.

## Additional Notes

* **Apple Shortcut Integration:** Requires downloading a specific shortcut from the GitHub repository for easy control from your iPhone. [here](https://www.icloud.com/shortcuts/8e2b513cecbe49aeb71407cee164bf35)
* **Custom URL for `br` command:** You can modify the URL opened by the "br" command in the "server.py" file.

## Disclaimer

Use this project at your own risk. The author is not responsible for any damage or security issues caused by using this software.