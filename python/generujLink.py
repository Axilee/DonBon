import webbrowser
#from main import ACCESS_TOKEN
#do zmiany na publiczny adres redirect po autoryzacji, tam wysyla sie token oauth2 (narazie jest w linku po prostu XD)
redirect_uri="http://localhost:5000"



client_id="nohxc0resfams2ui1ftvvs07awax2c"
link = "https://id.twitch.tv/oauth2/"
client_uri = f"authorize?response_type=token&client_id={client_id}&redirect_uri={redirect_uri}&scope="
scope=""
with open("permisjeDoLinku") as permisje:
    linie = permisje.readlines()
    for l in linie:
        l = l.replace(":","%3A")
        scope = scope.__add__(l)
        scope = scope.strip()
        scope = scope.__add__("+")
    scope = scope.removesuffix("+")
                
link = link+client_uri+scope+"&state=c3ab8aa609ea11e793ae92361f002671"
print(link)
webbrowser.open(link)



#https://id.twitch.tv/oauth2/authorize?response_type=token&client_id=nohxc0resfams2ui1ftvvs07awax2c&redirect_uri=http://localhost&scope=channel%3Amanage%3Apolls+channel%3Aread%3Apolls+bits%3Aread&state=c3ab8aa609ea11e793ae92361f002671

