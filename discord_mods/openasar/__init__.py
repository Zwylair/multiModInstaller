import os.path
import subprocess
import time
import urllib.request
import psutil


def install():
    print('Killing discord (waiting 5 seconds)')
    for process in psutil.process_iter(['name']):
        if process.info['name'] == 'Discord.exe':
            process.kill()

    time.sleep(5)

    print('Killed. Installing...')

    discord_parent_path = os.path.join(os.getenv('localappdata'), 'Discord')
    discord_path = [i for i in os.listdir(discord_parent_path) if i.startswith('app-')]  # remove all not 'app-' items
    discord_path.sort()
    discord_path = os.path.join(discord_parent_path, discord_path[-1])
    discord_resources = os.path.join(discord_path, 'resources')

    print('Backupping old app.asar')
    if os.path.exists(f'{discord_resources}/app.asar.backup'):
        os.remove(f'{discord_resources}/app.asar.backup')

    os.rename(f'{discord_resources}/app.asar', f'{discord_resources}/app.asar.backup')
    if os.path.exists(f'{discord_resources}/_app.asar'):
        os.rename(f'{discord_resources}/_app.asar', f'{discord_resources}/app.asar.backup')

    if os.path.exists(f'{discord_resources}/app.asar.orig'):
        os.rename(f'{discord_resources}/app.asar.orig', f'{discord_resources}/app.asar.backup')

    print('Downloading app.asar...')
    urllib.request.urlretrieve('https://github.com/GooseMod/OpenAsar/releases/download/nightly/app.asar', f'{discord_resources}/app.asar')

    print('Starting discord...')
    subprocess.run(['bin/deelevate.exe', f'"{discord_path}/Discord.exe"'])
    print('Installation complete.')
