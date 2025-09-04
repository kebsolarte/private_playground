# Main class for the game functionalities
class QuizBrain:

    # Takes in a list of Question objects to construct object
    def __init__(self, question_bank:list):
        self.question_number = 0
        self.question_bank = question_bank
        self.score = 0

    def still_has_questions(self):
        """Checks if there are still remaining questions in the question bank"""
        return self.question_number < len(self.question_bank) 

    def current_question(self):
        """Gets and prints the current question and returns the user answer"""
        current_question = self.question_bank[self.question_number]
        return input(f"Q:{current_question.question} True/False: ")

    def check_answer(self):
        """Checks if the user answer is the correct answer from the question bank"""
        answer = self.current_question()
        current_question = self.question_bank[self.question_number]
        if answer == current_question.answer:
            self.score += 1