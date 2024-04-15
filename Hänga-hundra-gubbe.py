import random
namn = input("Hej! Vad heter du?: ")

#Välkommen funktionen som välkommnar spelaren
def välkommen():
    print("Välkommen " + namn + ", är du redo för att köra hänga-hundra-gubbe?")


def play():
    # frågar om det var kul att spela
    fråga = input("Var det kul att spela? Y/N:")
    if fråga in ("Y", "Yes", "y", "yes", "YES"):
        print("Bazinga!")
    else:
        print("Womp Womp")

# orden som kan väljas
def ordet():
    ord = ["python", "ramez", "hangman", "dator", "stol", "ryan", ]
    return random.choice(ord).lower()

def spelet():
    # kalla välkommen funktionen för att börja spelet
    välkommen()
    # definera alfabetet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    word = ordet()
    # Tom lista för gissade bokstäver
    gissade_bokstäver = []
    #antal försök spelaren har.
    försök = 8
    # Ställ in första gissning som False
    gissning = False
    # print ett tips antal bokstäver i ordet
    print("Ordet har", len(word), "bokstäver")
    #Printar den antal ord i understräck.
    print(len(word) * "_")
    # Loopar tills spelaren har gissat rätt ord eller försök är 0

    while gissning == False and försök > 0:
        #berättar hur många försök spelaren har
        print("Du har " + str(försök) + " försök")
        guess = input("Gissa en bokstav i ordet eller gissa hela ordet(inkludera ej mellanslag):").lower()
        # spelaren skriver in en bokstav
        if len(guess) == 1:
            #Vilket svar du får beroende på vad du gissat/skrivit
            if guess not in alphabet:
                ("Du har inte skrivit in en bokstav i det engelska alfabetet.")
            elif guess in gissade_bokstäver:
                print("Du har redan gissat den bokstäven försök igen")
            elif guess not in word:
                print("Bokstäven finns inte i ordet")
                gissade_bokstäver.append(guess)
                försök -= 1
            elif guess in word:
                print("Bokstaven finns i ordet")
        # Spelaren skriver in hela ordet
        elif len(guess) == len(word):
            if guess == word:
                print("Du gissade rätt ord! Bra jobbat!")
                fråga = input("Var det kul att spela? Y/N:")
                if fråga in ("Y", "Yes", "y", "yes", "YES"):
                    print("Bazinga!")
                    break
                else:
                    print("Womp Womp")
                    break
            else:
                print("Du gissade tyvärr fel")
                försök -= 1
        # Spelaren gissar ett ord men det matchar inte antal ord
        elif len(guess) != len(gissade_bokstäver):
            print("Längden på ditt gissade ord matchar inte med antal bokstäver i ordet")
            försök -= 1
        # En funktion för att lägga till en gissad bokstav
        if guess in word:
            gissade_bokstäver.append(guess)
        status = ""
        for letter in word:
            if letter in gissade_bokstäver:
                status += letter
            else:
                status += "_"
        print(status)
        #bara några play again funktioner och om man lyckas gissa hela ordet via gissade bokstäver
        if status == word:
            print("Bra jobbat! Du gissade ordet!")
            fråga = input("Var det kul att spela? Y/N:")
            if fråga in ("Y", "Yes", "y", "yes", "YES"):
                print("Bazinga!")
                break
            else:
                print("Womp Womp")
                break
        elif försök == 0:
            print("Du har tyvärr inga fler gissningar :(")
            fråga = input("Var det kul att spela? Y/N:")
            if fråga in ("Y", "Yes", "y", "yes", "YES"):
                print("Bazinga!")
                break
            else:
                print("Womp Womp")
                break
spelet()

