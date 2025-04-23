import time  # Make sure to import the time module

quiz_questions = ["What is 2 + 2?", "What is 4 + 4?", "What is 7 x 2?", "What color is the sky?"]
quiz_answers = ["4", "8", "14", "Blue"]  

def quiz_question(new_question):
    for i in range(len(quiz_questions)):
        print(new_question[i])  # Display question
        time.sleep(3)  # Wait for 3 seconds before asking for the answer
        user_answer = input("Your answer: ")  # Ask for the answer after the delay
        if user_answer == quiz_answers[i]:
            print("correct")
        else:
            print("incorrect")
        time.sleep(1)  # Optional: add a small delay after each question for a smoother flow

continue_playing = True

while continue_playing:
    play_quiz = input("Hello! Want to play my quiz, Yes or No: ")
    if play_quiz.lower() == "yes":  # Making the input case-insensitive
        print("Awesome! Let's start")
        time.sleep(1)  # Delay after starting the quiz
        quiz_question(quiz_questions)
    else: 
        print("Okay bye! :)")
        continue_playing = False
