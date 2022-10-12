# Jackson Davaies
# Project 1
# October 11th 

import argparse
import socket
import sys
import datetime
  



parser = argparse.ArgumentParser()

parser.add_argument('-s', type=str, required=True)
parser.add_argument('-p', type=str, required=True)
parser.add_argument('-l', type=str, required=True)

args = parser.parse_args()
try:
    with open(args.l, 'a') as logfile:

        def writeP(chars):
            current_time = datetime.datetime.now()
            print(chars + '\n')
            logfile.writelines(f'{current_time.year}-{current_time.month}-{current_time.day} {current_time.hour}:{current_time.minute}:{current_time.second} - INFO - {chars}\n\n')

        writeP(f'command line arguments: IP: {args.s} Port: {args.p} Logfile: {args.l}')

        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:

            soc.connect((args.s, int(args.p)))

            writeP(f'Successfully Connected. IP: {args.s} Port: {args.p}')

            msg = input('Enter message to send to server: ')

            writeP('Sending message to server...')

            bytes = str.encode(msg)
            soc.sendall(bytes)

            writeP(f'Sent message to server: {msg}')

            writeP(f'Waiting for response from server.')

            data = soc.recv(1024)

            writeP('Received response from server')

            writeP(data.decode('utf-8').strip())
            
        except socket.error as message:
            
            print('Bind failed.')
            sys.exit()
    
        writeP('Closing socket.')
except FileNotFoundError:
    file = open(args.l, 'w+')
    file.close
    
    
