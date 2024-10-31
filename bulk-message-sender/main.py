from pyrogram import Client
from pyrogram.errors import UserDeactivatedBan
import asyncio
from bulk_message import BulkMessage



async def main():
    
    api_id = '#'  # get api_id from my.telgram.org
    api_hash = '#'  # get api_id from my.telgram.org
    phone = '#'  
    message = " پیام تست "
    app =  Client(name= "bulksender" ,api_id=api_id, api_hash=api_hash, phone_number=phone)

    option_help = f"{'#'*20}\n1- run script\n\
2- sef csv file\n\
3- time delay for sending messages\n\
4- get_contacts\n\
5- exit\n\
{'#'*20}\n\
select one option : "

    
    
    try:
        async with app:
            robot = BulkMessage(app,message)
            
            while(True):
                option = input(option_help)
                
                if option == '1' :
                    await robot.run()
                elif option == '2' :
                    robot.set_file()
                elif option == '3' :
                    time = input("time_delay(seconds): ")
                    robot.time_delay = int(time) 
                elif option == '4' :
                    await robot.get_contacts(save=True)
                elif option == '5' :
                    break

            
    except UserDeactivatedBan as e :
        print(e)
        
if __name__ == "__main__":
    asyncio.run(main())