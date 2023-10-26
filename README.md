# quiz_game
A fun Trivia Game that uses the Open Trivia DB API

The question object from the Question class takes 2 arguments: the text of the question, and the correct answer.
To get those tow arguments i've used requests to acces the Open Trivia DB API with the needed parameters(number of questions, category, dificulty, type) and 
create the question_answer_data, which then I looped through to create the question object to append to the question_bank list.

The question_bank is then passed as an argument to quiz object from the QuizBrain class which keeps the score, the number of questions,it verifies
if there are any questions left for the game to continue, it displays the question, the score, it checks if the answer is  correct or not,accordingly modifying the score.

After the while loop has ended the player will the end of the game message and his final score.

![Image 26 10 2023 at 13 00](https://github.com/gabrielsorin88/quiz_game/assets/126314730/24390cbb-9fa5-4519-bbfa-10485131c181)

![Image 26 10 2023 at 11 59](https://github.com/gabrielsorin88/quiz_game/assets/126314730/5d53efd2-88f1-4ddf-9f02-baa507628de8)
