from MinuOmaMoodul import*
salasõnad=ümber_kirjuta_fail("Paroolid.txt")
kasutajanimed=ümber_kirjuta_fail("Nimed.txt")
while True:
    print(kasutajanimed)
    print(salasõnad)
    print("1-registeerimine\n2-autoriseerimine\n3-nime või parooli muutmine\n4-unustanud parooli taastamine\n5-lõpetamine")
    vastus=int(input("Sisestage arv"))
    if vastus == 1:
        print("Registeerimine")
        kasutajanimed,salasõnad=registeerimine(kasutajanimed,salasõnad)
    elif vastus == 2:
        print("Autoriseerimine")
        autoriseerimine(kasutajanimed,salasõnad)
    elif vastus == 3 :
        print("Nimi  või parooli muutmine")
        vastus==int(input("Kas muudame nimi või parooli?"))
        if vastus == "nimi":
            kasutajanimed=muutmine(kasutajanimed)
        elif vastus == "parool":
            salasõma=muutmine(salasõnad)
        elif vastus == "mõlemad":
            kasutajanimed=muutmine(kasutajanimed)
            salasõma=muutmine(salasõnad)
    elif vastus == 4:
        print("Unustanud porooli taastamine")
    elif vastus == 5:
        print("Lõpetamine")
        break
    else:
        print("Tundmatu valik")

