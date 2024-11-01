import random

import art
import game_data
import random

def data_index_choice():
    data_length = range(0, len(game_data.data[0:]))
    data_index = random.choice(data_length)
    return data_index

question1 = game_data.data[data_index_choice()]
question2 = game_data.data[data_index_choice()]
score = 0

def checks(a, b, answer):
    global question1
    global question2
    global score

    if a['follower_count'] > b['follower_count'] and answer == "A":
        score += 1
        question1 = a
        question2 = game_data.data[data_index_choice()]
        game()
    elif a['follower_count'] > b['follower_count'] and answer == "B":
        print(f"\n" * 20)
        return f"Sorry, that's wrong. Final score: {score}"
    elif a['follower_count'] < b['follower_count'] and answer == "B":
        score += 1
        question1 = b
        question2 = game_data.data[data_index_choice()]
        game()
    else:
        print(f"\n" * 20)
        return f"Sorry, that's wrong. Final score: {score}"

def game():
    global question1
    global question2
    game_on = True
    while game_on:
        if question1['name'] == question2['name']:
            question2 = game_data.data[data_index_choice()]

        print(f"{art.logo}\nCompare A: {question1['name']} , a {question1['description']}, from {question1['country']}.")
        print(f"{art.vs}\nAgainst B: {question2['name']}, a {question2['description']}, from {question2['country']}.")
        guess = (input("Who has more followers? Type 'A' or 'B': ").capitalize())

        if guess == "A" or guess == "B":
            result = checks(question1, question2, guess)
            if result:
                print(art.logo)
                print(result)
            game_on = False

game()