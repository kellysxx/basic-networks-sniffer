# Basic Network Sniffer

A simple packet sniffer built with Python and Scapy. It captures live IP traffic and shows where each packet came from, where it's going, and which protocol it uses.

## Tools Used

- Kali Linux
- Python 3
- Scapy
- VirtualBox

## Features

- Captures up to 20 IP packets
- Displays source and destination IP addresses
- Identifies TCP, UDP, and ICMP protocols

## How to Run

Install Scapy if needed:

bash

sudo apt update

sudo apt install python3-scapy -y


Run the program:

bash
sudo python3 sniffer.py


In a second terminal, generate some traffic:

bash
ping -c 10 1.1.1.1


## Example Output


----------------------------------------
Source IP: 10.0.2.15
Destination IP: 1.1.1.1
Protocol: ICMP
----------------------------------------
Source IP: 1.1.1.1
Destination IP: 10.0.2.15
Protocol: ICMP
capture completed!


## What I Learned

I learned how to capture network packets, identify IP addresses, and tell common network protocols apart. I also learned how to use Python to analyze traffic.

## Disclaimer

This project is for learning purposes only. Only run it on networks you own or have permission to monitor.
