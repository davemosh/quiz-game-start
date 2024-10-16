class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    """here we check if the user still has question by looking at the list 
    and if the answer number is still less than the number of question it will
    give true until its false meaning greater than actual number of questions"""
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    """here the code counts the number of questions until the end"""
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    """here the computer checks if the answer the user entered is correct 
    to that of the list and keeps track of the score of the user"""
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got the answer Right")
        else:
            print("That is not the correct answer")
        print(f"The correct answer was : {correct_answer}.")
        print(f"Your current score is: {self.score} out of {self.question_number}")
        print("\n")

















