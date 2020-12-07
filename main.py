from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
n = len(question_data)

for i in range(0, n):
    question_bank.append(QuestionModel(question_data[i]['text'], question_data[i]['answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()