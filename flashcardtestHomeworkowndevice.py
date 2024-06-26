def add_flashcard(flashcards):
    duplicate = True
    while duplicate == True:
        key = input ("Gebe mir ein Keyword: ")
        if key in flashcards.keys():
            print("Du hast ein Duplikat erzeugt, gebe bitte ein neues Keyword ein: ")
        else:
            duplicate = False
    Explanation = input("Dein Keyword war super, jetzt gebe mir bitte eine Erklärung dazu: ")
    flashcards[key] = Explanation
def view_flashcards(flashcards):
        print(flashcards)

flashcards = dict()

for i in range (0, 3):
    add_flashcard(flashcards)
view_flashcards(flashcards)