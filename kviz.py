# ------------------------
def new_game():
    question_num = 1
    quesses = [] #pravimo niz od nasih odgovora
    corect_quesses = 0 #broji nam tacne odgovore. svaki tacni odg +1, netacni +0
    for key in questions:
        print("------------------------")
        print(key) #Ko je kreirao Python?:
        for i in options[question_num - 1]: #pristupamo prvoj stavci niza options i ispisujemo A.Guido van Rossum
            print(i)                                                                          #B. Elon Mask
        quess = input("Unesite A, B, C ili D: ").upper() #ovde mi unosimo odg                 #C. Mark Zukelberg
        quesses.append(quess) #dodajemo ga u niz nasih odg                                    #D. Bill Gates
        corect_quesses += check_answer(questions.get(key),quess)#ovde uporedjujemo tacan odg i nas unos pomocu f-je check_ansver
        #atribut koji prosledjujemo je tacni odg iz questions (A), kao i nas uneti odgovor 
        question_num += 1
    display_score(corect_quesses, quesses)#pozivamo ispis kojem prosledjujemo tacne odg., kao i niz nasih odg. kao atribute
# ------------------------
def check_answer(answer, quess):
    if answer == quess: #ako je tacni odg. od prvog pitanja == mom odgovoru ispisi tacno, i uvecaj broj tacnih za 1 (ovo je u for petlji)
        print("->TACNO!")
        return 1
    else:
        print("->NETACNO!")
        return 0
# ------------------------
def display_score(corect_quesses, quesses):
    print("------------------------")
    print("--------REZULTAT---------")
    print("TACNI ODGOVORI: ", end="")#odstampaj niz tacnih odgovra
    for i in questions:
        print(questions.get(i), end=" ") 
    print()
    
    print("VASI ODGOVORI: ", end=" ") #odstampaj niz mojih odgvora
    for i in quesses:
        print(i, end=" ")
    print()
    score = int((corect_quesses/len(quesses))*100) #odstampaj procenat tacnosti
    print("Tvoj rezultat je {}%".format(score))
# ------------------------
def play_again():
    response = input("Da li zelite da igrate ponovo?(DA ili NE): ").upper() #ako zelimo ponovo da igramo vraca true, u suprutnom vraca false
    if response == "DA":
        return True
    else:
        return False
# ------------------------

questions = {
    "Ko je kreirao Python?: ": "A",
    "Koje godine je napravljen Python?: ": "B",
    "Koja inspiracija je bila za naziv jezika 'Python'?: ": "C",
    "Da li je Python programski jezik visokog nivoa opste namene?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Mask", "C. Mark Zukelberg", "D. Bill Gates"],
          ["A. 1990", "B. 1991", "C. 1992", "D. 1993"],
          ["A. Zmija-piton", "B. Grad Pyton", "C. 'Leteci cirkus Monty Pythona'", "D. Ostalo"],
          ["A. Jeste", "B. Nije", "C. Mozda", "D.Zavisi do namene"]]

new_game()
while play_again(): #sve dok je true, pozivaj new_game()
    new_game()
print("Prijatno. Dodjite nam opet!")#kada bude false, izadji i odstampaj Prijatno. Dodjite nam opet!
