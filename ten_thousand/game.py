from banker import Banker
from game_logic import GameLogic
print('Welcome to Ten Thousand')

choice1 = input('(y)es to play or (n)o to decline \n> ')


class Game:
    def __init__(self):
        self.game_round = 1
        self.dice = 6
        self.banker = Banker()

    def play(self):
        print('starting round ' + str(self.game_round))
        print('rolling 6 dice...')
        roll = GameLogic.roll_dice(self.dice)
        print(roll)
        choice2 = input('Enter dice to keep or (q)uit \n> ')
        if choice2 == 'q':
            print(f'Thanks for playing. You earned {self.banker.balance} points')
        else:
            self.game_round += 1
            leftover = list(roll)
            new_list = choice2.split(',')
            acc_list = [eval(i) for i in new_list]
            for i in acc_list:
                leftover.remove(i)
            cur_score = GameLogic.calculate_score(acc_list)
            self.banker.shelf(cur_score)
            print(f'You have {self.banker.shelved} unbanked points and {len(leftover)} dice remaining')
            choice3 = input(f'(r)oll again, (b)ank your points or (q)uit:')
            if choice3 == 'q':
                print(f'Thanks for playing. You earned {self.banker.balance} points')
            elif choice3 == 'b':
                self.banker.bank()
                print(f'You banked {self.banker.balance} points in round {self.game_round}')
            while choice3 == 'r':
                roll = GameLogic.roll_dice(len(leftover))
                print(roll)
                choice2 = input('Enter dice to keep or (q)uit \n> ')
                if choice2 == 'q':
                    print(f'Thanks for playing. You earned {cur_score} points')
                    break
                else:
                    new_list = choice2.split(',')
                    acc_list = [eval(i) for i in new_list]
                    for i in acc_list:
                        leftover.remove(i)
                    cur_score += GameLogic.calculate_score(acc_list)
                    print(f'You have {cur_score} unbanked points and {len(leftover)} dice remaining')
                    choice3 = input(f'(r)oll again, (b)ank your points or (q)uit:')




# def play():
#     cur_round = 1
#     cur_score = 0
#     print('starting round ' + str(cur_round))
#     print('rolling 6 dice...')
#     roll = GameLogic.roll_dice(6)
#     print(roll)
#     choice2 = input('Enter dice to keep or (q)uit \n> ')
#     if choice2 == 'q':
#         print(f'Thanks for playing. You earned {cur_score} points')
#     else:
#         cur_round += 1
#         leftover = list(roll)
#         new_list = choice2.split(',')
#         acc_list = [eval(i) for i in new_list]
#         for i in acc_list:
#             leftover.remove(i)
#         cur_score += GameLogic.calculate_score(acc_list)
#         print(f'You have {cur_score} unbanked points and {len(leftover)} dice remaining')
#         choice3 = input(f'(r)oll again, (b)ank your points or (q)uit:')
#         if choice3 == 'q':
#             print(f'Thanks for playing. You earned {cur_score} points')
#         elif choice3 == 'b':
#             print(f'You banked {cur_score} points in round {cur_round}')
#             play()
#         while choice3 == 'r':
#             roll = GameLogic.roll_dice(len(leftover))
#             print(roll)
#             choice2 = input('Enter dice to keep or (q)uit \n> ')
#             if choice2 == 'q':
#                 print(f'Thanks for playing. You earned {cur_score} points')
#                 break
#             else:
#                 new_list = choice2.split(',')
#                 acc_list = [eval(i) for i in new_list]
#                 for i in acc_list:
#                     leftover.remove(i)
#                 cur_score += GameLogic.calculate_score(acc_list)
#                 print(f'You have {cur_score} unbanked points and {len(leftover)} dice remaining')
#                 choice3 = input(f'(r)oll again, (b)ank your points or (q)uit:')


start = Game()

if choice1 == 'y':
    start.play()
