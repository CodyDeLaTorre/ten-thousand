
from game_logic import GameLogic
print('Welcome to Ten Thousand')

choice1 = input('(y)es to play or (n)o to decline \n> ')

def play():
    cur_round = 1
    cur_score = 0
    print('starting round ' + str(cur_round))
    print('rolling 6 dice...')
    roll = GameLogic.roll_dice(6)
    print(roll)
    choice2 = input('Enter dice to keep or (q)uit \n> ')
    if choice2 == 'q':
        print('Thanks for playing. You earned ' + cur_score + ' points')
    else:
        new_list = choice2.split(',')
        acc_list = [eval(i) for i in new_list]
        cur_score += GameLogic.calculate_score(acc_list)
        


if choice1 == 'y':
    play()
