import platform
import subprocess


def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    code = 'cp866' if platform.system().lower() == 'windows' else 'utf-8'
    command = ['ping', param, '4', host]
    return subprocess.run(command, stdout=subprocess.PIPE, encoding=code)


URLS = ['google.com', 'ya.ru']
for url in URLS:
    print(ping(url).stdout)
    print('=============================')
