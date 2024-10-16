from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

"""here these are just inputs of questions pulled from data.py and stored in
various various variables below for future uses also"""
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

"""Here we check if the user still has questions 
so the program can continue looping throught 
the list of questions in the data.py"""
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print("\n")
print(f"Your final score is {quiz.score} out of {quiz.question_number}")












































































