from data import question_data
from question import Question
from quizbrain import QuizBrain

# Creating the question bank using list comprehension
question_bank =[Question(item["text"], item["answer"]) for item in question_data]

quiz = QuizBrain(question_bank)
quiz.next_question()




    