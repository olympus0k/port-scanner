import socket
import os
import signal
import time
import threading
import sys
import subprocess
from queue import Queue
from datetime import datetime


subprocess.call('clear', shell=True)


def main():
    socket.setdefaulttimeout(0.30)
    print_lock = threading.Lock()
    discovered_ports = []


    print("made by olympus")
    
  
    print("                   the creator of this tool is not responsable for the bad use of this tool            ")
    print("-" * 60)
    time.sleep(1)
    target = input("enter host HERE: ")
    error = ("i am sorry we could not find a host ")
    try:
        t_ip = socket.gethostbyname(target)
    except (UnboundLocalError, socket.gaierror):
        print("\n[-]Invalid format. Please use a correct IP or web address[-]\n")
        sys.exit()
   
    print("-" * 60)
    print("Scanning target "+ t_ip)
    print("Time started: "+ str(datetime.now()))
    print("-" * 60)
    t1 = datetime.now()

    def portscan(port):

       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       
       try:
          conx = s.connect((t_ip, port))
          with print_lock:
             print("Port {} is open".format(port))
             discovered_ports.append(str(port))
          conx.close()

       except (ConnectionRefusedError, AttributeError, OSError):
          pass

    def threader():
       while True:
          worker = q.get()
          portscan(worker)
          q.task_done()
      
    q = Queue()
     
  
     
    for x in range(200):
       t = threading.Thread(target = threader)
       t.daemon = True
       t.start()

    for worker in range(1, 65536):
       q.put(worker)

    q.join()

    t2 = datetime.now()
    total = t2 - t1
    print("Port scan completed in "+str(total))
    print("-" - 60)
   
    print("-" - 60)
    print("nmap -p{ports} -sV -sC -T4 -Pn -oA {ip} {ip}".format(ports=",".join(discovered_ports), ip=target))
    print("*" * 60)
    outfile = "nmap -p{ports} -sV -sC -Pn -T4 -oA {ip} {ip}".format(ports=",".join(discovered_ports), ip=target)
    t3 = datetime.now()
    total1 = t3 - t1



    def automate():
       choice = '0'
       while choice =='0':
        
          print("-" * 60)
          print("1 = NMAP SCAN?")
         
       
          print("-" * 60)
          choice = input("Option Selection: ")
          if choice == "1":
             try:
                print(outfile)
                os.mkdir(target)
                os.chdir(target)
                os.system(outfile)
               
                t3 = datetime.now()
                total1 = t3 - t1
                print("-" * 60)
                print("Combined scan completed in "+str(total1))
                print("Press enter to quit...")
                input()
             except FileExistsError as e:
                print(e)
                exit()
          elif choice =="2":
             main()
          elif choice =="3":
             sys.exit()
          else:
             print("Please make a valid selection")
             automate()
    automate()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        quit()