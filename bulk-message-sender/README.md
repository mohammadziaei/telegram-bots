# bulk message sender - Python Script for Sending Bulk Messages via Telegram

This is a Python script that utilizes the Pyrogram library to send bulk messages to Telegram contacts. It reads phone numbers and usernames from a CSV file and sends a message to each of them with a customizable time delay.

## Features

- Send bulk messages to Telegram contacts using a CSV file input.
- Check if a contact exists by phone number or username before sending a message.
- Log successfully sent messages in a separate log file.
- Save all Telegram contacts (phone number, username, and ID) into a CSV file.

## Requirements

- Python 3.7 or higher
- Pyrogram
- Telegram API ID and API Hash (You need to create a Telegram app on [my.telegram.org](https://my.telegram.org) to get these credentials)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/mohammadziaei/telegram-bots.git
    cd telegram-bots/bulk-message-sender
    ```

2. Install the dependencies:
    ```bash
    pip install -U pyrogram tgcrypto
    ```

## Usage

1. Setting up the client
Before running the script, fill in your api_id, api_hash, and phone_number directly in the main.py file:

    ```python
    from pyrogram import Client
    from pyrogram.errors import UserDeactivatedBan
    import asyncio
    from bulk_message import BulkMessage

    async def main():
        api_id = '#'  # get api_id from my.telegram.org
        api_hash = '#'  # get api_hash from my.telegram.org
        phone = '#'  # your phone number
        app = Client(name="bulksender", api_id=api_id, api_hash=api_hash, phone_number=phone)

        # Rest of the code...
    ```

2. Running the main.py script
    ```bash
    python main.py
    ```

## Menu Options
The script provides a menu with the following options:

1. Run the script to send messages.
2. Set the path for the CSV file.
3. Adjust the time delay for sending messages.
4. Get and save contacts to a CSV file.
5. Exit the application.


## CSV File Format
Your CSV file should have two columns: phone_number and username. Example:

    ```csv
    1234567890,username1
    0987654321,username2
    ```

If a phone number or username is not available, leave it blank.

## Error Handling
The script handles some common Telegram API errors:

PeerIdInvalid: If the contact's ID is not valid.
BadRequest: If the request format is incorrect.
UserDeactivatedBan: If the user has been banned or deactivated.

## Contributing
If you encounter any bugs or have feature requests, feel free to open an issue or submit a pull request.


## License
This project is open-source and available under the MIT License. See the LICENSE file for more details.

## Contact
Mohammad Ziaei - ziaeemohammad008@gmail.com

Project Link: https://github.com/mohammadziaei/telegram-bots/tree/main/bulk-message-sender