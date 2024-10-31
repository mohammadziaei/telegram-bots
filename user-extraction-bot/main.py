from telegram_extractor import TelegramExtractor


API_ID = "#"
API_HASH = "#"
PHONE_NUMBER = "#"


if __name__ == "__main__" : 
    
    extractor = TelegramExtractor(API_ID,API_HASH,PHONE_NUMBER)
    extractor.run()