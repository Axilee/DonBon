import paramiko
import multiprocessing
import time
import configparser
hostname='172.30.85.163'
username='fitas'
password='qwe!@#'

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
    sciezka_zdalna = '/home/fitas/bot/zmienne.ini'

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
        with sftp.open('/home/fitas/bot/zmienne.ini','rb+') as config_remote, open('.\\zmienne.ini','rb+') as config_local:
            cl = config_local.read()
            cr = config_remote.read()
            if cl == cr:
                pass
            else:
                print ("SSH >> Lokalny config \n",cl)
                print ("SSH >> Zdalny config \n",cr)
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