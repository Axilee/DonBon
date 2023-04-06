import paramiko
import multiprocessing
import time
import configparser
import difflib
hostname='172.30.85.163'
username='fitas'
password='qwe!@#'
diff = difflib.Differ()
def loading():
    while True:
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print("\r   \r", end="", flush=True)
loading_t = multiprocessing.Process(target=loading)

def polacz():

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password='qwe!@#',timeout=3)
    sciezka_lokalna = '.\\zmienne.ini'
    sciezka_zdalna = '/var/www/python/zmienne.ini'

    with open(sciezka_lokalna, 'rb') as plik_lokalny:
        plik_content = plik_lokalny.read()

    sftp = ssh.open_sftp()
    with sftp.open(sciezka_zdalna, 'wb') as plik_zdalny:
        plik_zdalny.write(plik_content)
    sftp.close()
    ssh.close()

def execute():
    try:
        print(f"\nSSH >> Wysyłanie komend do {hostname}")
        loading_t.start()
        try:
            polaczenie = polacz()
            print(f"\nSSH >> SUKCES! Wysłano komendy do {hostname} jako {username}")
            loading_t.terminate()
        except paramiko.ChannelException as e:
            print("\nSSH >> Nieudane połączenie ",e)
        
        
    except:
        loading_t.terminate()
        print("\nSSH >> COŚ POSZŁO NIE TAK - NIE WYSŁANO")
def config_sync():
    print("Config remote sync...")
    config = configparser.ConfigParser()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password='qwe!@#')
    sftp = ssh.open_sftp()

    while ssh:
        with sftp.open('/var/www/python/zmienne.ini','rb+') as config_remote, open('.\\zmienne.ini','rb+') as config_local:
            cl = config_local.read()
            cr = config_remote.read()
            if cl == cr:
                pass
            else:
                # remote = sftp.open('/var/www/python/zmienne.ini','r') #pojedyncza roznica linijkami, moze sie przyda
                # local = open('.\\zmienne.ini','r')
                # roznica = list(diff.compare(remote.readlines(),local.readlines()))
                # for i in roznica:
                #     if i.startswith("+") or i.startswith("-"):
                #         print("Zmiana komendy",i, end="")
                # print ("SSH >> Lokalny config \n",cl) #pokazuje cale configi przy zmianie
                # print ("SSH >> Zdalny config \n",cr)
                with open('.\\zmienne.ini','wb+') as config_local:
                    print("SSH >> Config Updated")
                    config_local.write(cr)
                    config_local.close()
            time.sleep(0.5)
    
    
    sftp.close()
    ssh.close()
#do testow bezposrednich z cmd
if __name__ == '__main__':
    execute()