from question_model import Question
# from data import question_data
# de schimbat in question_bank.append(Question(elem--->>["question"], elem--->>["correct_answer"].lower()))
from quiz_brain import QuizBrain
from data1 import question_data

question_bank = []

for elem in question_data:
    question_bank.append(Question(elem["question"], elem["correct_answer"].lower()))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz\nYour final score is: {quiz.score}/{quiz.question_number}.")
