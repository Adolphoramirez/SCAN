# Importer les modules necéssaires
import nmap
import requests

# Déclarer la version de Nmap
nv = nmap.__version__
print("The current version of nmap is ", nv)


# Fonction pour scanner une IP
def scan():
    ns = nmap.PortScanner()
    ipinput = input("Indiquez l'adresse IP :")
    portinput = input("Indiquez la plage de port à scanner de l'adresse IP : ")
    ns.scan("{}".format(ipinput), "{}".format(portinput), "-v")
    print(ns.scaninfo())



# Fonction pour tester les requêtes
def requestsend():
    chooseinput = input("Ecrivez POST pour une requête en POST et GET pour une requête en GET : ")
# Différencier utilisation de GET ou POST
    urlinput = input("Indiquez l'adresse du site à requêter : ")
    paramsinput = input("Indiquez les paramètres de l'URL séparés d'un ':' ")
    if chooseinput == "GET" or "get":
        rg = requests.get("{}".format(urlinput))
        print("Le code HTTP est : ", rg.status_code)
        print("Informations du header", rg.headers)
        print(rg.cookies)
    elif chooseinput == "POST" or "post":
        rp = requests.post("{}".format(urlinput), "{:}".format(paramsinput))
        print("Le code HTTP est : ", rp.status_code)
        print("Informations du header", rp.headers)
        print(rp.text)

    else:
        print("Vous n'avez pas indiqué la bonne valeur")


# Choisir entre NMAP et requests
def choosing():
    chooser = input("NMAP ou Requests? ")
    if chooser == "NMAP":
        scan()
    elif chooser == "Requests":
        requestsend()

# Utiliser TOR
def torusage():
    if __name__ == "__main__":
        session = requests.session()
        session.proxies = {'http': 'socks5://127.0.0.1:9150', 'https': 'socks5://127.0.0.1:9150'}
        r = session.get("http://www.google.com")
        print(r.status_code)
    for header in r.headers.keys():
        print(header + " : " + r.headers[header])


# Utiliser une connection TOR
accesstor=input("Voulez vous utiliser un proxy TOR ?")
if accesstor == "o":
    torusage()
elif accesstor == "n":
    choosing()
