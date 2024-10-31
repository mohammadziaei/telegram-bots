from pyrogram import Client
from pyrogram.errors import MsgIdInvalid
import asyncio
import csv

class TelegramExtractor():
    list_user = list()
    def __init__(self, api_id, api_hash, phone_number) -> None:
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone_number = phone_number 
        self.delay = 5 #seconds       
        self.app = Client('extraction-bot', api_id=self.api_id, api_hash=self.api_hash, phone_number=self.phone_number)
        
    def help(self):
        print("Welcome to the Telegram Extractor Helper!")
        print("Please choose an option:")
        print("1 - Setup username channels or groups")
        print("2 - Setting the search delay in seconds")
        print("3 - Extract user comments from channels")
        print("4 - Extract user from groups")
        print("5 - Save found users in csv ")
        print("6 - Exit")
        return input("option : ");
        
    def set_channel_username(self, username):
        self.channel_username = username
        print("*"*10, "channel username saved successfully", "*"*10, "\n")
        
    def save_list_user(self):
        with open("listUser.csv",'w') as fcsv : 
            writer = csv.writer(fcsv)
            self.list_user.insert(0,['id','username','first_name','phone_number'])
            writer.writerows(self.list_user)
            
        print("*"*10, "Information saved successfully", "*"*10, "\n")
        
    async def get_all_comments(self):
        async for message in self.app.get_chat_history(chat_id=self.channel_username):           
            try:
                count = await self.app.get_discussion_replies_count(self.channel_username, message.id)
                if count>0 :
                    async for comment in self.app.get_discussion_replies(self.channel_username, message.id):
                        user = comment.from_user
                        if user and user.id not in map(lambda x : x[0] , self.list_user):
                            self.list_user.append([user.id,user.username,user.first_name, user.phone_number])
                            print(" ====>>> " , user.id, user.username, user.first_name , user.phone_number)  
                        await asyncio.sleep(self.delay) #delay for find user
                    break #test
            except MsgIdInvalid as e :
                print('MsgIdInvalid' , ' : ', message.id , " : ", e)
            except Exception as e:
                print('error' , ' : ', message.id , " : ", e)              
                break
            
            await asyncio.sleep(self.delay) #delay for find post
        
        print(f'{"*"*10} {len(self.list_user)} users were successfully registered {"*"*10} \n')
        
        
    async def get_all_members(self):
        # دریافت اعضای گروه
        count = 1
        async for member in self.app.get_chat_members(self.channel_username):
            if member.user.is_deleted == False and member.user.is_bot == False:  # اگر حساب کاربر پاک نشده باشد
                self.list_user.append([member.user.id,member.user.username,member.user.first_name,member.user.phone_number])
                print(" ====>>> ", member.user.id, member.user.username, member.user.first_name , member.user.phone_number)
                count+=1
                if count >=6 :
                    break
                await asyncio.sleep(self.delay)   
                
        
        print(f'{"*"*10} {len(self.list_user)} users were successfully registered {"*"*10} \n') 
                       
                        
    async def start_bot(self):        
        while(True):
            choice = self.help()
            if choice == '1' : 
                username = input('Channel username: ')
                self.set_channel_username(username)         
            if choice == '2' : 
                time = input('delay in seconds : ')
                self.delay = int(time)
            elif choice == '3' : 
                await self.get_all_comments()
            elif choice == '4' : 
                await self.get_all_members()
            elif choice == '5' :
                self.save_list_user()
            elif choice == '6' :
                break
            else:
                continue
            
    def run(self):
        self.app.start()
        self.app.loop.run_until_complete(self.start_bot())
        self.app.stop()

