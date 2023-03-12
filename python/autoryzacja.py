import sys
sys.path.append('Oauth2') #zeby wczytalo/bez tego nie dziala teraz
import tkinter
from Oauth2 import webhook
from Oauth2 import AuthorizationOauth2 
from Oauth2 import initWebhook
import multiprocessing

def wlacz_webhook():
            print("zaczyna webhook")
            webhook.flaskAppWebhook.app.run(host="0.0.0.0", port=5000)
def okno():
        initWebhook.inicjalizuj.wybor()
webhookProcess = multiprocessing.Process(target=wlacz_webhook)


if __name__ == "__main__":
        webhookProcess.start()
        okno()
        #webhookProcess.join() # usun zeby sie zamknal webhook po zamknieciu okna, jak to tu jest, webhook wskoczy na główny proces z powrotem

for key, value in os.environ.items():
        print(key + " = " + value)