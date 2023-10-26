from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import requests

# API endpoint URL
url = "https://opentdb.com/api.php"

# Parameters for the API request
params = {
    "amount": 10,  # Number of questions to retrieve
    "category": 9,  # Category ID (General Knowledge)
    "difficulty": "easy",  # Difficulty level
    "type": "boolean",  # Type of questions
}

# Make the GET request to the API
response = requests.get(url, params=params)
data = response.json()

question_answer_data = data['results']

question_bank = []

for item in question_answer_data:
    question = Question(item["question"], item["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've compleated the quiz\n"
      f"Your final score was: {quiz.score}/{quiz.question_number}")
