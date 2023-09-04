import time


class Quiz:
    def __init__(self):
        self.scores = 0

    def ask_answer(self, question, answers):
        answer_no = 0

        print(question)

        for answer in answers:
            answer_no += 1
            print(f"{answer_no:0>2}.{answer.title()}")

        return str(input("\nAnswer: ")).lower()

    def check_answer(self, given_answer, correct_answer, correct_answer_no):
        # Checking the answer
        if given_answer == correct_answer or int(given_answer) == int(correct_answer_no):
            self.scores += 20
            print(f"Hooray! That's Correct 😊... \n")
            time.sleep(1)

        else:
            print(f"No! That's not Correct 😑... \n")
            time.sleep(1)

    def show_result(self):
        if 50 > self.scores >= 35:
            print(f"\nScore: {self.scores} \nGrade: Pass (S)")

        elif 65 > self.scores >= 50:
            print(f"\nScore: {self.scores} \nGrade: Merit (C)")

        elif 75 > self.scores >= 65:
            print(f"\nScore: {self.scores} \nGrade: Merit (B)")

        elif self.scores >= 75:
            print(f"\nScore: {self.scores} \nGrade: Distinction (A)")

        else:
            print(f"\nScore: {self.scores} \nGrade: Fail")
