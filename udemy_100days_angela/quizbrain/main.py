from data import question_data
from question import Question
from quizbrain import QuizBrain

# Creating the question bank using list comprehension
question_bank =[Question(item["text"], item["answer"]) for item in question_data]

quiz = QuizBrain(question_bank)

# Main program
while quiz.still_has_questions():
    quiz.check_answer()
    print(f"The correct answer is {quiz.question_bank[quiz.question_number].answer}")
    quiz.question_number += 1
    print(f"Score: {quiz.score}/{quiz.question_number}")






    