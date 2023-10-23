# Sukuna.py - WiFi Hacking Tool [Created by Alphabet9470]

Sukuna.py is a beginner-friendly WiFi hacking tool for educational purposes. It is designed to assist users in understanding the security vulnerabilities in their own networks and to learn more about network security.

## Version

**Version 1** - Launched on October 23, 2023.

Please note that this tool is for educational purposes only, and any unauthorized use of it is strictly prohibited.

## Getting Started

Follow these steps to use Sukuna.py:

### Step 1: Install Dependencies

Before running Sukuna.py, make sure to install the required Python packages. You can do this using the following command:
**sudo apt-get update**<br>

**sudo apt-get install aircrack-ng**<br>

**pip install -r requirements.txt**


### Step 2: Running Sukuna.py

To run Sukuna.py, use the following command as the root user:

**sudo python3 sukuna.py**

### Usage

Once you've launched Sukuna.py, you can perform various tasks, including scanning for available WiFi networks and analyzing captured handshakes.

Click on Monitor Mode[It will start the Monitor Mode ].

Again Run the Program and Click on Scan ( It will start scanning all WiFi Networks ).

***Note: To stop any ongoing scanning process, simply press Ctrl + C.***

Then select any particular WiFi and Enter the BSSID and CH number of that wifi.

It will start scanning that WiFi and sending deauth attack.

You have to wait untill Handshake captured is displayed on screen.

***Press Ctrl+C after that***
 
The Target Handshake file will be saved in the targets folder then you have to run the program again and this time click on Cracking.

In the "cracking" option, you'll be prompted to enter the last serial digit of the handshake capture (CAP) file that you want to analyze and attempt to crack.

***Note:***
Enter the serial digit correctly (e.g: 01 )


# Disclaimer

Sukuna.py is intended for educational and ethical use only. Do not use this tool for any malicious or unauthorized activities. Respect the privacy and security of others.

Please use this tool responsibly and in compliance with your local laws and regulations.

Sukuna.py is not responsible for any misuse or unlawful activity carried out using this tool. Use it at your own risk.




