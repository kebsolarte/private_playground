class QuizBrain:

    def __init__(self, question_bank:list):
        self.question_number = 0
        self.question_bank = question_bank

    def next_question(self):
        current_question = self.question_bank[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.question} True/False: ")