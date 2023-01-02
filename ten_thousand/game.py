from banker import Banker
from game_logic import GameLogic
print('Welcome to Ten Thousand')

choice1 = input('(y)es to play or (n)o to decline \n> ')


class Game:
    def __init__(self):
        self.game_round = 1
        self.dice = 6
        self.banker = Banker()

    def quit_game(self):
       print(f'Thanks for playing. You earned {self.banker.balance} points')

    def start_round(self):
        print(f'starting round {str(self.game_round)} \n')
        self.game_round += 1
        print('rolling 6 dice...')
        roll = GameLogic.roll_dice(self.dice)
        print(roll)
        return roll

    def bank_points(self):
        self.banker.add_to_total()
        print(f'You banked {self.banker.shelved} points in round {self.game_round}')
        print(f'Total score is {self.banker.balance} \n')
        self.banker.clear_shelf()
        start.play()

    def re_roll(self, old_di):
        reroll = GameLogic.roll_dice(self.dice)
        print(reroll)
        choice4 = input('Enter dice to keep or (q)uit \n> ')
        if choice4 == 'q':
            print(f'Thanks for playing. You earned {self.banker.balance} points')
        else:
            new_list = choice4.split(',')
            actual_list = [eval(i) for i in new_list]
            print(f"actual list {actual_list}")
            for i in actual_list:
                print(f"Im in the loop {i}")
                old_di.remove(i)
                print(old_di)
            print(old_di)
            self.dice = len(old_di)
            cur_score = GameLogic.calculate_score(actual_list)
            self.banker.temp_shelf(cur_score)
            print(f'You have {self.banker.shelved} unbanked points and {self.dice} dice remaining')
            choice3 = input(f'(r)oll again, (b)ank your points or (q)uit:')
            if choice3 == 'r':
                print('feature not added yet')
                # Game.re_roll(self)
                Game.quit_game(self)

    def play(self):
        roll = Game.start_round(self)
        choice2 = input('Enter dice to keep or (q)uit \n> ')
        if choice2 == 'q':
            Game.quit_game(self)
        else:
            leftover = list(roll)
            new_list = choice2.split(',')
            actual_list = [eval(i) for i in new_list]
            try:
                for i in actual_list:
                    leftover.remove(i)
                self.dice = len(leftover)
                cur_score = GameLogic.calculate_score(actual_list)
                self.banker.temp_shelf(cur_score)
                print(f'You have {self.banker.shelved} unbanked points and {len(leftover)} dice remaining')
                choice3 = input(f'(r)oll again, (b)ank your points or (q)uit:')
                if choice3 == 'q':
                    Game.quit_game(self)
                elif choice3 == 'b':
                    self.dice = 6
                    Game.bank_points(self)
                elif choice3 == 'r':
                    # print('feature not added yet')
                    Game.re_roll(self, leftover)
                    # Game.quit_game(self)
            except:
                print('Cheater!!! Or possibly made a typo...')


start = Game()

if choice1 == 'y':
    start.play()
else:
    print('Maybe next time.')


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