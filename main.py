import random
from datetime import datetime
from scores import save_score, show_high_scores

moves = {1: "Rock", 2: "Paper", 3: "Scissors"}

score = 0
lives = 5

bot_name = "Bot"
user_name = input("Enter your name: ").strip()

print(f"\nHello {user_name}! Let's play Rock-Paper-Scissors.")
print(f"You have {lives} lives. Try to win as many rounds as you can.\n")

while lives > 0:
    print("Your turn! Choose one:")
    for key, move in moves.items():
        print(f"{key} = {move}")

    choice = input("Enter your move (1, 2, 3): ").strip()
    if not choice.isdigit() or int(choice) not in moves:
        print("Invalid input! Please enter 1, 2, or 3.\n")
        continue

    user_move = int(choice)
    bot_move = random.choice(list(moves.keys()))

    print(f"\nYou chose: {moves[user_move]}")
    print(f"{bot_name} chose: {moves[bot_move]}")

    if user_move == bot_move:
        print("It's a tie! No points this round.\n")
        continue

    if (user_move == 1 and bot_move == 3) or \
       (user_move == 2 and bot_move == 1) or \
       (user_move == 3 and bot_move == 2):
        score += 1
        print(f"Great! You won this round. Your score is now {score}.\n")
    else:
        lives -= 1
        print(f"Oh no! {bot_name} won this round. You have {lives} lives left.\n")

    print(f"Scoreboard → {user_name}: {score} | Lives: {lives}")
    print("-" * 50)

now = datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")

print(f"\nGame Over! {user_name}, your final score is {score}.")
save_score(user_name, score, date, time)
show_high_scores()
