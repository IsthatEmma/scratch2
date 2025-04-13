import random
import time


quiz_questions = []
print("Hello! Welcome to the quiz! Let's do this!!")


def first_question():
    question_one = "First question! What is 2+2?"
    print(question_one)
    user_answer = input("Enter your answer: ")

    if user_answer == "4":
        print("Hooray! Thats correct! :D")
    else:
        print("No sorry!:( Thats incorrect")

    return question_one
quiz_questions = first_question()


def second_question():
    question_two = ("Second question! What is 4+4?")
    print(question_two)
    user_answer = input("Enter your answer: ")

    if user_answer == "8":
        print("Amazing!! Correct again! :D")
    else:
        print("No sorry!:( Thats incorrect")

    return question_two
quiz_questions = second_question()

def third_question():
    question_three = ("Third question! What is 7 x 2?")
    print(question_three)
    user_answer = input("Enter your answer: ")

    if user_answer == "14":
        print("Fantastic!! :D")
    else:
        print("No sorry!:(")

    return question_three
quiz_questions = third_question()


def last_question():
    question_four = ("Last Question! What color is the sky")
    print(question_four)
    user_answer = input("Enter your answer: ")

    if user_answer == "blue":
        print("Double Amazing!")
    else:
        print("Incorrect! :(")

    return question_four
quiz_questions = last_question()

print("Thanks for playing my mini quiz game! For all your hard work you get a medal! 🥇")

