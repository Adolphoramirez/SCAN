import dns.resolver
import dns.name

def main():

    chooser = input("Que veux tu faire ? ( MX/KEY/reverser/analyzer) : ")
    if chooser == "KEY":
        dnskey()
    elif chooser == "reverser" :
        reversename()
    elif chooser == "analyzer" :
        domainanalyze()
    elif chooser == "MX":
        mxcheck()

def mxcheck():

        try:
            userinput = input("Donne-moi le domaine à tester :  ")
            answers = dns.resolver.query(userinput, 'MX')
            for rdata in answers:
                print('Host', rdata.exchange, "has preference", rdata.preference)
        except:
            print("Pas de réponse du serveur DNS")

def dnskey():

    user = input("Quelle TLD pour récupérer les DNSKEY ? (en format fr.)")
    edns_size = 1500
    myresolver = dns.resolver.Resolver()
    myresolver.use_edns(0, 0, edns_size)
    result = myresolver.query (user, 'DNSKEY')
    for item in result:
        print(item)



def reversename():

    userinputs = input("Donnez moi l'adresse IP à reverse : ")
    print(dns.reversename.from_address(userinputs))

def domainanalyze():

    parent = input("Donnez moi le domaine parent")
    child = input ( "Donnez moi le domaine enfant")
    other = input("Donnez moi tout autre domaine")

    p = dns.name.from_text(parent)
    c = dns.name.from_text(child)
    o = dns.name.from_text(other)
    print ("%s is a subdomain of %s: %s" % (c, p, c.is_subdomain(p)))
    print ("%s is a parent domain of %s: %s" % (c, p, c.is_superdomain(p)))
    print ("%s is a subdomain of %s: %s" % (o, p, o.is_subdomain(p)))
    print ("%s is a parent domain of %s: %s" % (o, p, c.is_superdomain(o)))
    print ("Relative name of %s in %s: %s" % (c, p, c.relativize(p)))
    print ("%s has %i labels" % (p, len(p.labels)-1))
    print ("%s has %i labels" % (c, len(c.labels)-1))

main()
