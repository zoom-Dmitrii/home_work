import subprocess
import chardet

args = {'ping': ['yandex.ru', 'google.com']}
for keys in args:
    for ind in range(0, len(args.values())+1):
        test_ping = subprocess.Popen([keys, args[keys][ind]], stdout=subprocess.PIPE)
        for line in test_ping.stdout:
            result = chardet.detect(line)
            line = line.decode(result['encoding']).encode('utf-8')
            print(line.decode('utf-8'), end='')
