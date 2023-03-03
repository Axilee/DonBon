import paramiko
def polacz():
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='172.30.85.163', username='fitas', password='qwe!@#')

    sciezka_lokalna = '.\\zmienne.ini'
    sciezka_zdalna = '/home/fitas/bot/zmienne.ini'

    with open(sciezka_lokalna, 'rb') as plik_lokalny:
        plik_content = plik_lokalny.read()


    sftp = ssh.open_sftp()
    with sftp.open(sciezka_zdalna, 'wb') as plik_zdalny:
        plik_zdalny.write(plik_content)
    sftp.close()
    ssh.close() 
if __name__ == "__main__":
    polacz()