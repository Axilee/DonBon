import webbrowser

#do zmiany na publiczny adres redirect po autoryzacji, tam wysyla sie token oauth2 (narazie jest w linku po prostu XD)
#budujemy webook w flasku po to zeby callback pobierac z clienta a nie z serwera, jak zrobimy z serwera to potem bedzie trzeba to do klienta jakos wyslac bez sensu

def getOAuth(service_name,client_id,link,redirect_uri):
    scope=""
    if(service_name == "twitch"):
        print("TWITCH")
        client_uri = f"authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope="
        with open("permisjeDoLinku", "r") as permisje:
            linie = permisje.readlines()
            for l in linie:
                l = l.replace(":","%3A")
                scope = scope.__add__(l)
                scope = scope.strip()
                scope = scope.__add__("+")
            scope = scope.removesuffix("+")
    elif(service_name =="spotify"):
        print("SPOTIFY")
        client_uri = f"authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope="
        with open("permisjeDoLinkuSpotify","r") as permisje:
            linie = permisje.readlines()
            for l in linie:
                l = l.replace(":","%3A")
                scope = scope.__add__(l)
                scope = scope.strip()
                scope = scope.__add__("+")
            scope = scope.removesuffix("+")
    else:
        return "sraka"
                    
    if(service_name == "spotify"):
        link = link+client_uri+scope
    elif(service_name == "twitch"):
        link = link+client_uri+scope+"&state=c3ab8aa609ea11e793ae92361f002671"
    print(link)
    webbrowser.open(link)

#https://id.twitch.tv/oauth2/authorize?response_type=token&client_id=nohxc0resfams2ui1ftvvs07awax2c&redirect_uri=http://localhost&scope=channel%3Amanage%3Apolls+channel%3Aread%3Apolls+bits%3Aread&state=c3ab8aa609ea11e793ae92361f002671

