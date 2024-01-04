import os.path
import msvcrt
import subprocess
import time
from datetime import datetime
import psutil


def install():
    if not os.path.exists(os.path.join(os.getenv('appdata'), 'Spotify/Spotify.exe')):
        print('ERROR: Spotify was not found. Install anyway? (y/n)')

        while True:
            got = msvcrt.getch().decode().lower()

            if got == 'n':
                print('Installation was cancelled.')
                return
            elif got == 'y':
                break

    print('Spicetify is installing...')

    spicetify_install_command = 'iwr -useb https://raw.githubusercontent.com/spicetify/spicetify-cli/master/install.ps1 ^| iex'
    subprocess.Popen(['bin/deelevate.exe', 'cmd', f'/c echo.y | powershell -Command {spicetify_install_command}'])
    made_time = datetime.now().strftime('%H:%M:%S')

    time.sleep(1)

    for proc in psutil.process_iter(['pid', 'name']):
        proc_made_time = datetime.fromtimestamp(proc.create_time()).strftime('%H:%M:%S')

        if proc_made_time == made_time and proc.name() == 'cmd.exe':
            while True:
                try:
                    proc.status()
                    time.sleep(1)
                except psutil.NoSuchProcess:
                    break

    print('Spicetify was successfully installed!')
