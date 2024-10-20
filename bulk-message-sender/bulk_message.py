from pyrogram import Client
from pyrogram.errors import PeerIdInvalid, BadRequest,UserDeactivatedBan
import asyncio
import csv
import os

class BulkMessage():
    contacts = []
    
    def __init__(self,client:Client) -> None:
        self.client=client 
        self.time_delay = 20
        
    #Main execution of script file to send mass message
    async def run(self):
        try:
            with open(self.file_path,'r') as cv:
                reader = csv.reader(cv) 
                with open('logs_sucsses.txt','w') as f:
                    for line in reader:
                        result_check = await self.check_is_contact_exists(phone_number= line[0],username=line[1]) #line[0] -> phone_number & line[1] -> username
                        if result_check :
                            print(f"{'*'*10} Message sent successfully -> ",line[0] if line[0] else line[1],'*'*10) 
                            f.write(f"{line[0]},{line[1]}\n") # logs phone numbers and usernames to which the message was sent successfully
                            f.flush()
                            await self.client.send_message(chat_id = result_check,text = 'message test') # send message to user

                        await asyncio.sleep(self.time_delay)
        except AttributeError :
            print(f"\n {'*'*10} error -> You have not made some settings before running the program {'*'*10}\n")        
        except Exception as e :
            print('*'*10 ,e ,'*'*10)
    
    #Check contacts for username or phone number is available
    async def check_is_contact_exists(self,phone_number:str = None,username:str = None): 
        if not self.contacts :
            await self.get_contacts()
            
        for contact in self.contacts:
            if phone_number == contact[0] or username == contact[1]:
                return contact[2] # return user id
            
        print(f"{'*'*10} ({phone_number}:{username}) Not in your telegram contacts {'*'*10}") 
        return None
    
    #Obtaining the phone, username and ID of contacts in Telegram
    async def get_contacts(self,save=False):
        if not self.contacts :
            contacts = await self.client.get_contacts()
            for contact in contacts :
                self.contacts.append([contact.phone_number,contact.username,contact.id])
        
        if save: #logs information in csv file
            with open('my_contacts.csv','w') as fcsv:
                writer = csv.writer(fcsv)
                writer.writerows(self.contacts)
                print(f"\n{'*'*10} Your contacts have been successfully saved in 'my_contacts.csv' file. {'*'*10}\n")
            
        return (self.contacts)
    
    
    async def set_new_phone(self,phone_number):
        try:
            self.client.send_code(phone_number=phone_number)
            code = input("The confirmation code has been sent via Telegram app\n\
                Enter confirmation code: ")
            self.client.sign_in(phone_number=phone_number,phone_code=code)
            print(f"\n{'*'*10}Login successful! Session saved.{'*'*10}\n")
        except Exception as e :
            print(f"\n{'*'*10} error -> ",e ,'*'*10 ," \n")
    
    #Enter the csv file in the program   
    def set_file(self):
        while(True):
            file_path = input('Enter the file address (csv) : ')
            file_name, file_extension = os.path.splitext(file_path)
            if os.path.exists(file_path) and os.path.isfile(file_path) :
                print(file_extension)
                if file_extension == '.csv' :
                    self.file_path=file_path
                    print(f"\n{'*'*10} file added successfully. {'*'*10}\n")  
                    break
                else:
                    print(f"\n{'*'*10} error -> The file extension is not valid. {'*'*10}\n")
            else :
                print(f"\n{'*'*10} error -> The file does not exist. {'*'*10}\n")
  
    def __str__(self) -> str:
        return self.client 
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.client})"