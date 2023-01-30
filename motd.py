#!/usr/bin/env python3

"""
programita de mierda que armé para molestar.
si querés cambiar algo dsp hace: chmod +x motd.py && sudo cp motd.py /bin/motd
    
básicamente hay 3 comandos: 
    -a (o --add)  para agregar, 
    -d (o --del)  para borrar,
    -l (o --list) para listar.
y si lo dejas solo te printea el motd. abz.
"""


from datetime import datetime
from random import choice
from sys import argv
from json import load, dump
from os.path import expanduser, join

MOTD_PATH = join(expanduser("~"), "motd", "mensajes_inicio.json")

def load_json():
    with open(MOTD_PATH, "r") as j:
        return load(j)
def change_json(c):
    with open(MOTD_PATH, "w+") as e:
        dump(c, e)
        print("listo pa quedo re cheto")

def hello():
    print(datetime.now().strftime("%d %b %Y, %H:%M:%S"), end=" - ")
    a = load_json()["mensajes"]
    print(choice(a))

def add_hello(a):
    latest = load_json()
    latest["mensajes"].append(a)
    change_json(latest)

def del_hello(a):
    latest = load_json()
    b = [e for e in latest["mensajes"] if e != a]

    if b == latest["mensajes"]:
        print("no hay de esos mi viejo")
        return
    
    latest["mensajes"] = b
    change_json(latest)
    list_hello()

def list_hello():
    latest = load_json()
    [print("->", e) for e in latest["mensajes"]]


if len(argv) > 1:
    argu = " ".join(argv[2:])
    if argv[1] == "-a"   or argv[1] == "--add":
        add_hello(argu)
    elif argv[1] == "-d" or argv[1] == "--del":
        del_hello(argu)
    elif argv[1] == "-l" or argv[1] == "--list":
        list_hello()
    elif argv[1] == "-h" or argv[1] == "--help":
        print(__doc__)
    else:
        print("que haces pa? no te entiendo")
else:
    hello()
