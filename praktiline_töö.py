try:
    nimi = input("Tere! Olen sinu uus sõber - Python! kirjuta oma nimi")
    print(nimi, ", oi kui ilus nimi!")
    KehaIndex = int(input("! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
    if KehaIndex == 1:
        pikkus = float(input("kirjuta oma pikkus"))
        mass = float(input("kirjuta mass"))
        index = mass/(0.01*pikkus)**2
        (nimi,"! Sinu keha indeks on:", index(index,2))
        if index<0:
            vastus = "vale kaal"
        elif index<=16:
            vastus = "Tervisele ohtik alakaal"
        elif index<=19:
            vastus = "Alakaal"
        elif index<25:
            vastus = "Normaalkaal"
        elif index<=30:
            vastus = "Ülekaal"
        elif index<=35:
            vastus = "Rasvumine"
        elif index<40:
            vastus = "Tugev rasvumine"
        elif index>40:
            vastus = "Tervisele ohtlik rasvumine"
        print(vastus, round (index,2))
    else:
        print("Kahju! See on väga kasulik info!")
        print()
        print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")
except :
    ValueError()








    
    


