import os
import sys
import requests
import time
import subprocess

os.system('cls')
print('''

⠀⠀⠀⠀⠀⢀⡴⠋⠉⠛⠒⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⠏⠀⠀⣶⡄⠀⠀⣛⠀⠀⠀⠀⠀      AutoTor for Windows
⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀⡤⠋⠠⠉⠡⢤⢀⠀             * 
⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⢉⣝⠲⠤⣄⣀⣀⠌         Rotating proxy...
⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡴⠃⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀
⢀⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀
⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠀⠀⠀⠀
''')

def get_tor_ip():
    session = requests.session()

    session.proxies = {
        'http': 'socks5://localhost:9050',
        'https': 'socks5://localhost:9050'
    }

    try:
        r = session.get('http://httpbin.org/ip')
    except Exception as e:
        print(e)
    else:
        return r.text

def restart_tor():
    print('restarting')
    os.system("taskkill /f /im tor.exe >nul 2>&1")
    time.sleep(2)
    tor_path = r"C:\Users\githubmember\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe" #change it 
    subprocess.Popen(tor_path, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(5)

if __name__ == "__main__":
    for i in range(999):
        print(get_tor_ip())
        time.sleep(5)
        restart_tor()
        print(get_tor_ip())
        time.sleep(5)
