import random

class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def display_question(self):
        print(self.question)
        for i, option in enumerate(self.options):
            print(f"{i+1}. {option}")

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.current_question_index = 0
        self.current_money = 0

    def start_game(self):
        print("Vítejte ve hře Kdo chce být milionářem!")
        print("Máte před sebou sérii otázek, na které musíte odpovědět správně.")
        print("Za každou správnou odpověď získáte peníze. Kolik peněz vyhrajete? To záleží jen na vás!")
        input("Stiskněte Enter pro začátek hry...")
        self.display_question()

    def display_question(self):
        question = self.questions[self.current_question_index]
        question.display_question()
        user_answer = input("Zadejte číslo odpovědi: ")
        if user_answer.lower() == 'quit':
            print("Hra byla přerušena. Vaše výhra je", self.current_money, "Kč.")
            return
        if user_answer.isdigit():
            user_answer = int(user_answer)
            if 1 <= user_answer <= len(question.options):
                if question.check_answer(user_answer):
                    self.current_money += 1000
                    print("Správně! Vyhráli jste 1000 Kč.")
                else:
                    print("Špatně! Hra končí. Vaše výhra je", self.current_money, "Kč.")
                    return
                self.current_question_index += 1
                if self.current_question_index < len(self.questions):
                    self.display_question()
                else:
                    print("Gratulujeme! Vyhráli jste 1 000 000 Kč!")
            else:
                print("Neplatná volba. Zadejte číslo odpovědi od 1 do", len(question.options))
                self.display_question()
        else:
            print("Neplatný vstup. Zadejte prosím číslo odpovědi.")
            self.display_question()

# Seznam otázek
questions = [
    Question("Kdo je autorem knihy Hobit?", ["J.R.R. Tolkien", "J.K. Rowling", "C.S. Lewis"], 1),
    Question("Jaké je hlavní město České republiky?", ["Praha", "Brno", "Ostrava"], 1),
    Question("Kolik dní má únor v přestupném roce?", ["28", "29", "30"], 2),
    Question("Jaký je chemický symbol pro vodík?", ["H", "O", "V"], 1),
    Question("Kdo namaloval obraz Mona Lisa?", ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso"], 1)
]

# Vytvoření instance hry a spuštění hry
quiz_game = QuizGame(questions)
quiz_game.start_game()
