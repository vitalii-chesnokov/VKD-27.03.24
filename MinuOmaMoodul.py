from string import *
from random import *
import random
import string
from typing import  List
from time import sleep
from os import path, remove
def registeerimine(kasutajad:list, paroolid:list)->any:
    """kikjeldus
    :param list kasutajad: Kirjeldus
    :param list paroolid: Kirjeldus
    :rtype: list,list
    """
    while True:
        nimi=input("Mis on sinu nimi? ")
        if nimi not in kasutajad:
            while True:
                parool=input("Mis on sinu parool?  ")
                flag_p=False
                flag_l=False
                flag_u=False
                flag_d=False
                if len(parool)>=8:
                    parool_list=list(parool)
                    for p in parool_list:
                        if p in punctuation:
                             flag_p=True
                        elif p in digits:
                            flag_l=True
                        elif p in ascii_lowercase:
                             flag_u=True
                        elif p in ascii_uppercase:
                            flag_d=True
                    if flag_p and flag_u and flag_l and flag_d:
                        kasutajad.uppend(nimi)
                        paroolid.uppend(parool)
                    break
                else:
                    print("Nõrk salasõna!")
            break
        else:
             print("Selline kasutaja on juba olemas!")
    return kasutajad, paroolid
def autoriseerimine(kasutajad:list, paroolid:list):
    """Funktsioon kuva ekraanile "Tere tulemast kui kasutaja on olemas nimekirajs
    Nimi on järjendis kasutajad
    Salasõna on paroolide järjendis
    Nimi ja salasõna indeksid on võrdsed
    :param list kasutajad:...
    :param list paroolid:...
    """
    p=0
    while True:
        nimi=input("Sisesta kasutajanimi: ")
        if nimi in kasutajad:
            while True:
                parool=input("Sisesta salasõna: ")
                p+=1
                try:
                    if kasutajad.index(nimi)==paroolid.index(parool):
                        print(f"Tere tulemast! {nimi} ")
                        break
                except:
                    print("Vale nimi või salasõna!")
                    if p==5:
                        print("Proovi uuesti 10 sek pärast")
                        for i in range(10):
                            sleep(1)
                            print(f"On jäänud {10-i} sek ")
        else:
                print("Kasutajad pole")
def muutmine(list_:list):
    """

    """
    muutuja=input("Vana nimi või parool: ")
    if muutuja in list_:
        index=list_.index(muutuja)
        muutuja=input("Uus nimi või parool: ")
        list_[index]=muutuja
    return list_
def loe_failist(fail:str)->list:
    """Funktsioon loeb tekst *.txt failist
    """
    f=open(fail,'r',encoding="utf-8")
    järjend=[]
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend
def kirjuta_failisse(fail:str,järjend=[]):
    """Salvestame tekst failisse
    """
    n=int(input("Mitu: "))
    for i in range(n):
        järjend.append(input(f"{i+1}. sõna "))
    f=open(fail,'a',encoding="utf-8")
    for element in järjend:
        f.write(element+"\n")
    f.close()
def ümber_kirjuta_fail(fail:str):
    """
    """
    f=open(fail,"a")
    text=input("Sissesta tekst:")
    f.write(text+"\n")
    f.close
def failide_kirjutamine():
    """
    """
    failinimi=input("Mis fail tahad eemaldada?") #path.isdir("kaust")
    if path.isfail(failinimi):
        remove(failinimi)
        print(f"Fail {failinimi} oli kastutatud")
    else:
        print(f"Fail {failinimi} puudub")

