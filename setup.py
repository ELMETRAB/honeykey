import honeypot.py
import subprocess, platform

if platform == "linux" or platform == "linux2":
    setupLinux()
elif platform == "win32":
    setupWin()

def setupLinux():
#verifier librairie socket, paramiko et threading sont installé
    subprocess.run(["ls", "-l"])
#vérifier si la communication ssh est ouverte sur port 22

def setupWin():
    subprocess.run(["ls", "-l"])