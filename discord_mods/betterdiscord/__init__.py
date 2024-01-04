import sys
import string
import random
import os.path
import subprocess
import urllib.request


def gen_random_temp_file() -> str:
    while True:
        filepath = os.path.join(os.getenv('tmp'), 'tmp0' + ''.join([random.choice(string.ascii_lowercase) for _ in range(9)]) + '.py')
        if not os.path.exists(filepath):
            return filepath


def install():
    script_name = gen_random_temp_file()
    urllib.request.urlretrieve('https://raw.githubusercontent.com/Zwylair/BetterDiscordAutoInstaller/master/installer.py', script_name)

    subprocess.run(['cmd', f'/c {sys.executable} -m pip install -r requirements.txt && {sys.executable} {script_name} --silent'])
    os.remove(script_name)
