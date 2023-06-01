import paramiko
import multiprocessing
import time
import configparser
import difflib
import pointbits
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
        print(f"SSH >> Command sync {hostname}")
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
    print("SSH >> Config syncing")
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
                with open('.\\zmienne.ini','wb+') as config_local:
                    config_local.write(cr)
                    config_local.close()
                print("SSH >> Config Updated")
                pointbits.updateRewards()
            time.sleep(1)
    
    
    sftp.close()
    ssh.close()
#do testow bezposrednich z cmd
if __name__ == '__main__':
    execute()