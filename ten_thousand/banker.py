class Banker:
    def __init__(self):
        self.balance = 0
        self.shelved = 0

    def shelf(self, cur_score):
        """
        temp stores banked points

        """
        self.shelved = cur_score

    def bank(self):
        """
        add points from shelf to total and resets shelf to 0

        """
        self.balance = self.shelved


    def clear_shelf(self):
        """
        method to remove unbanked points

        """
        self.shelved = 0
