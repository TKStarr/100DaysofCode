import question_model
import quiz_brain
import data

question_bank = []

for question in data.question_data:
    question_bank.append(question_model.
                         Question(question["text"], question["answer"])
                         )

quiz = quiz_brain.QuizBrain(question_bank)

while quiz.still_has_questions() == True:
    quiz.next_question()

print(f"Your final score is {quiz.score} out of {quiz.question_number}")
