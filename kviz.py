# ------------------------
def new_game():
    question_num = 1
    quesses = []
    corect_quesses = 0
    for key in questions:
        print("------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        quess = input("Unesite A, B, C ili D: ").upper()
        quesses.append(quess)
        corect_quesses += check_answer(questions.get(key),quess)
        question_num += 1
    display_score(corect_quesses, quesses)
# ------------------------
def check_answer(answer, quess):
    if answer == quess:
        print("->TACNO!")
        return 1
    else:
        print("->NETACNO!")
        return 0
# ------------------------
def display_score(corect_quesses, quesses):
    print("------------------------")
    print("--------REZULTAT---------")
    print("TACNI ODGOVORI: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    
    print("VASI ODGOVORI: ", end="")
    for i in quesses:
        print(i, end=" ")
    print()
    score = int((corect_quesses/len(quesses))*100)
    print("Tvoj rezultat je {}%".format(score))
# ------------------------
def play_again():
    response = input("Da li zelite da igrate ponovo?(DA ili NE): ").upper()
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
while play_again():
    new_game()
print("Prijatno. Dodjite nam opet!")
