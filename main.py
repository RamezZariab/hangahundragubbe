import random
namn = input("Hej! Vad heter du? ")
def välkommen ():
    print("Välkommen " + namn + ", är du redo för att köra hänga-hundra-gubbe?")
def play ():
    #frågar om man vill köra igen
    fråga = input ("Vill du köra igen? Y/N:")
    if fråga in ("Y", "Yes", "y", "yes", "YES"):
        print("Bazinga!") and spelet()
    else:
        print("Womp Womp")

#orden som kan väljas
def ordet ():
    ord = ["python", "ramez", "hangman", "dator", "stol", "ryan", ]
    return random.choice(ord).lower()
def spelet ():
    #kalla välkommen funktionen för att börja spelet
    välkommen()
    #definera alfabetet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    word = ordet()
    #Tom lista för gissade bokstäver
    gissade_bokstäver = []
    försök = 8    #Ställ in första gissning som False
    gissning = False
    print()
    #print ett tips antal bokstäver i ordet
    print("Ordet har", len(word), "bokstäver")
    print(len(word) * "_")
    while gissning == False and försök > 0:
        print("Du har " + str(försök) + " försök")
        guess = input("Gissa en bokstav i ordet eller gissa hela ordet(inkludera ej mellanslag):").lower()
        #spelaren skriver in en bokstav
        if len(guess) == 1:
            if guess not in alphabet:
                ("Du har inte skrivit in ett ord i det engelska alfabetet.")
            elif guess in gissade_bokstäver:
                print("Du har redan gissat den bokstäven försök igen")
            elif guess not in word:
                print("Bokstäven finns inte i ordet")
                gissade_bokstäver.append(guess)
                försök -=1
            elif guess in word:
                print("Bokstaven finns i ordet")
        #Spelaren skriver in hela ordet
        elif len(guess) == len(word):
            if guess == word:
                print("Du gissade rätt ord! Bra jobbat!")
                gissning = True
            else:
                print("Du gissade tyvärr fel")
                försök -=1
                #Spelaren gissar ett ord men det matchar inte antal ord
        elif len(guess) != len(gissade_bokstäver):
            print("Längden på ditt gissade ord matchar inte med antal bokstäver i ordet")
            försök -=1
        status = ""
        for letter in word:
            if letter in gissade_bokstäver:
                status += letter
            else:
                status += "_"
        print(status)
        if status == word:
            print("Bra jobbat! Du gissade ordet!")
            guessed = True
        elif försök == 0:
            print("Du har tyvärr inga fler gissningar :(")
    play()
spelet()