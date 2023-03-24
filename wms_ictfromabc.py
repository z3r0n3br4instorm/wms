#Zerone
#CREW2K22AL
#WMS Whatsapp Management System
import subprocess
import os
import time
import json
switch = 0
def smn(number,message):
    if switch == 0:
        print("Sending Message to returned number...")
        return_os_text = "npx mudslide send "+str(number)+" \""+str(message)+"\""
        print(return_os_text)
        os.system(return_os_text)
def loop_msg(number,message):
    print("Message will loop until i reaches infinity...")
    while True:
        smn(number,message)
def send_msg_mult(msgstring):
    print("Sending Messages to Multiple Numbers")
    print("Reading Data from numbers.txt")
    with open("numbers.txt", 'r') as fp:
        for count, line in enumerate(fp):
            pass
    for i in range(0,count+1):
        #print(msgstring+open("numbers.txt","r").readlines()[i].strip())
        smn((open("numbers.txt","r").readlines()[i].strip()),msgstring)
def send_msg_mult_grp(message):
    print("Warning ! This function is still under development. \n Please recheck the input data before proceed !")
    name = input("Enter Group name:")
    print("Searching for groups...")
    with open("groups.txt") as file:
        data = file.readlines()
        print("Search Resutls\033[0;36m")
        try:
            for line in data:
            # Remove the newline character from each line
                line = line.strip()
                json_data = json.loads(line)
                if name in json_data["subject"]:
                    print(json_data["subject"])
        except:
            print("\u001b[37mAN ERROR OCCURED ! IGNORING...")
        x = input("\u001b[37m! MESSAGE WILL BE SENT TO ALL THESE GROUPS !. Enter P to proceed.")
        if x == "p" or x == "P":
            with open("groups.txt") as file:
                data = file.readlines()
                print("Sending...(Press ctrl+z to force stop the process)")
                try:
                    for line in data:
                    # Remove the newline character from each line
                        line = line.strip()
                        json_data = json.loads(line)
                        if name in json_data["subject"]:
                            smn(json_data["id"],message)
                except:
                    print("AN ERROR OCCURED ! IGNORING...")
        input("Press enter to continue...")
def find_grp(name,message):
    with open("groups.txt") as file:
        data = file.readlines()

    try:
        for line in data:
            line = line.strip()
            json_data = json.loads(line)
            if json_data["subject"] == name:
                print("Found the subject: "+name)
                #print(json_data["id"], json_data["subject"])
                smn(json_data["id"],message)
            else:
                print("Subject not detected !, Searching for similer names...")
                if name in json_data["subject"].lower():
                    # Print the "id" and "subject" values
                    print("Search Resutls")
                    print(json_data["subject"])
                    x = input("Enter the Group Subject:")
                    y = input("Enter the message:")
                    send_check = input("Send Message ?(Y/N):")
                    if send_check == "Y" or send_check == "y":
                        print("Connecting to function...")
                        find_grp(x,y)

    except:
        print("Error detected !. Ignoring...")
def start():
    print("Checking Login Status...")
    os.system("npx mudslide login")
    while True:
        os.system("clear")
        print("- Zerone Technologies Systems -\n\n")
        print("\u001b[31mict", end ="")
        print("\u001b[37mfromabc by \u001b[31mRavindu Bandaranayake\u001b[37m\n\n")
        print("Checking Internet Status : \u001b[32mONLINE\u001b[37m")
        print("Whatsapp Management System (WMS)")
        print("WMS Version 1 [ReadyRelease]")
        print("dataSync Intergration [pending]")
        print("Select Option...")
        print("[0]Scan QR Code")
        print("[1]Send Message to a number")
        print("[2]Send Message to a group")
        print("[3]Send Message to Multiple groups")
        print("[4]Send Message to Multiple numbers")
        print("[5]Loop a Message to a number")
        print("[6]Log out")
        print("[7]Dump dataSync log [Under Dev]")
        get_input = input(str("ENTER SELECTION :"))
        if get_input == "0":
            os.system("npx mudslide login")
            os.system("clear")
        elif get_input == "1":
            x = input("Enter the number :")
            y = input("Enter the message :")
            send_check = input("Send Message ? (Y/N) :")
            if (send_check == "Y" or send_check == "y"):
                print("Sending Message...")
                smn(x,y)
        elif get_input == "4":
            print("Numbers will be selected from numbers.txt file !")
            y = input("Enter the message :")
            send_check = input("Send Message ? (Y/N) :")
            if (send_check == "Y" or send_check == "y"):
                print("Sending Message...")
                send_msg_mult(y)
        elif get_input == "2":
            os.system("clear")
            print("Listing Available Groups")
            os.system("mudslide groups")
            os.system("mudslide groups > groups.txt")
            x = input("Enter the Group Subject:")
            y = input("Enter the message:")
            send_check = input("Send Message ?(Y/N):")
            if send_check == "Y" or send_check == "y":
                print("Connecting to function...")
                find_grp(x,y)
        elif get_input == "3":
            os.system("clear")
            print("Processing Data...")
            #os.system("mudslide groups")
            os.system("npx mudslide groups > groups.txt")
            print("Please Double check the message before sending !, To enter a multi-lined message, type and enter 'mlt_ln_strt' and to stop recording strings, type 'mlt_ln_stp'")
            y = input("Enter the message:")
            if y == "mlt_ln_strt":
                print("\033[0;36mSystem Set to multi line reading mode. To exit, type 'mlt_ln_stp'\u001b[37m\n\n")
                contents = []
                while True:
                    try:
                        line = input()
                    except EOFError:
                        continue
                    if line == "mlt_ln_stp":
                        break
                    contents.append(line)
                send_check = input("Send Message ?(Y/N):")
                send_msg_mult_grp("\n".join(contents))
            else:
                send_check = input("Send Message ? (Y/N):")
                send_msg_mult_grp(y)
        elif get_input == "5":
            x = input("Enter the number :")
            y = input("Enter the message :")
            send_check = input("Loop Message ? (Y/N) :")
            if (send_check == "Y" or send_check == "y"):
                print("Sending Message...")
                loop_msg(x,y)
        elif get_input == "6":
            print("System Logout")
            os.system("npx mudslide@latest logout")
def windows():
    #DEV
    print("UNDERDEV")
def linux():
    print("Starting program...")
    print("Checking Npm Version....")
    print("Please wait while System Configures Dependencies...")
    os.system("curl -s https://deb.nodesource.com/setup_16.x | sudo bash")
    os.system("sudo apt-get install nodejs")
    os.system("npm install mudslide")
    start()

def main():
    try:
        subprocess.run(['clear'], check = True)
        print("Zerone Technologies Systems...")
        print("Initializing Program. Please wait !")
        print("Detecting host os")
        print("Linux Host Detected !")
        linux()
    except subprocess.CalledProcessError:
        print("Zerone Technologies Systems...")
        print("Initializing Program. Please wait...")
        print("Detecting host os...")
        print ('Windows host detected...')
        windows()
main()
