#Crie um código em Python que teste se o site pudim está acessível pelo
# computador usado
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com.br')
except:
    print('\033[33mERRO\033[m')
else:
    print('\033[35mDeu certo! \033[m')
    print(site.read())
    menu(['opc1','opc2'])