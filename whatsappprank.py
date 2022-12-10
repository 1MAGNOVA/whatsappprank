import pywhatkit


#always open your whatsapp manually before running this code

phone_no =input("Enter the target phone number with country code:")
Text =input("Enter the Text:")
Time =input("Enter the target time in hours(e.g if 9:20pm, enter 9):")
Time_m =input("Enter the target time in mins(e.g if 9:00pm, enter 20):")
wait =input("Enter how many seconds you'd like to wait before sending message(in secs):")

pywhatkit.sendwhatmsg(phone_no,Text,Time,Time_m,wait)