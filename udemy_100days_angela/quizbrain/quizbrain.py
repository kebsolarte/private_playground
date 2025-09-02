class QuizBrain:

    def __init__(self, question_bank:list):
        self.question_number = 0
        self.question_bank = question_bank
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_bank) 

    def current_question(self):
        current_question = self.question_bank[self.question_number]
        return input(f"Q:{current_question.question} True/False: ")

    def check_answer(self):
        answer = self.current_question()
        current_question = self.question_bank[self.question_number]
        if answer == current_question.answer:
            self.score += 1