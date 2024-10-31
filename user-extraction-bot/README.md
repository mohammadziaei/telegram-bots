# Telegram User Extractor

This project is a Telegram user data extractor that allows you to extract user information from groups and channels. It uses the Pyrogram library to connect with the Telegram API and retrieve users' comments or member lists.

## Features

- **Channel or Group Username Setup**: Set the username for a specific Telegram group or channel to extract users from.
- **Search Delay Configuration**: Configure the delay between searches to avoid API limits.
- **Comment Extraction**: Retrieve and save users who commented in a specific channel.
- **Member Extraction**: Retrieve and save members from a specified group.
- **CSV Export**: Save the extracted user data in CSV format for further analysis.
  

## Requirements

- Python 3.7 or higher
- Pyrogram
- Telegram API ID and API Hash (You need to create a Telegram app on [my.telegram.org](https://my.telegram.org) to get these credentials)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/mohammadziaei/telegram-bots.git
    cd telegram-bots/user-extraction-bot
    ```

2. Install the dependencies:
    ```bash
    pip install -U pyrogram tgcrypto
    ```

## Usage

1. Setting up the client
Before running the script, fill in your api_id, api_hash, and phone_number directly in the main.py file:

    ```python
    from telegram_extractor import TelegramExtractor
    API_ID = "#"
    API_HASH = "#"
    PHONE_NUMBER = "#"

    if __name__ == "__main__" : 
        extractor = TelegramExtractor(API_ID,API_HASH,PHONE_NUMBER)
        extractor.run()

    ```

2. Running the main.py script
    ```bash
    python main.py
    ```

## Menu Options
When you run the program, a menu with options will appear:

1. Setup username for channels or groups.
2. Set search delay in seconds.
3. Extract user comments from channels.
4. Extract members from groups.
5. Save found users to a CSV file.
6. Exit.


## CSV Export Format
The extracted data is saved in listUser.csv with the following fields:

    ```CSV
    id: Telegram User ID
    username: Telegram Username
    first_name: First Name
    phone_number: Phone Number (if available)
    ```


## Disclaimer
This project is intended for educational purposes. Use responsibly and respect users' privacy by complying with Telegram's Terms of Service and the applicable data protection laws.

## License
This project is licensed under the MIT License.

## Contact
Mohammad Ziaei - ziaeemohammad008@gmail.com

Project Link: https://github.com/mohammadziaei/telegram-bots/tree/main/user-extraction-bot