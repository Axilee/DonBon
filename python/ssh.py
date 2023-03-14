import paramiko
import multiprocessing
import time

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
    ssh.connect(hostname, username=username, password='qwe!@#')

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
        polacz()
        loading_t.terminate()
    except:
        loading_t.terminate()
        print("SSH >> COŚ POSZŁO NIE TAK - NIE WYSŁANO")
    else:
        print(f"\nSSH >> SUKCES! Wysłano komendy do {hostname} jako {username}")


#do testow bezposrednich z cmd
if __name__ == '__main__':
    execute()