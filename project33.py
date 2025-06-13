import random
import time

player_score = 0
computer_score = 0
round_num = 1

print("🎯 Welcome to Dice Fight Game🎲 \n")
while player_score < 5 and computer_score <5:
    input(f"Round{ round_num} - Press Enter to roll your dice...")
    player_roll = random.randint(1,6)
    computer_roll = random.randint(1,6)

    print(f"You rolled: {player_roll}")
    print(f"Computer rolled : {computer_roll}")

    if player_roll > computer_roll:
        print("✅ computer wins this round! \n")
        computer_score += 1
    elif player_roll<computer_roll:
        print("❌ computer wins this round! \n")
        computer_score += 1
    else: 
        print("🔰 It's  a tie! \n")    

    print(f"Score - You: {player_score} | Computer : {computer_score} \n")    
    round_num +=  1
    time.sleep(1)

    if player_score == 5:
        print("🏆 You won the game!")
    
    else:
        print("😭 Computer won the game.Try again!")
        


