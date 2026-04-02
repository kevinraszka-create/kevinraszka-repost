import random

class Roulette:
    red = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
    black = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}
    odd = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35}
    even = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36}

    def __init__(self,
                 bet_type='straight',
                 wheel='American',
                 bank=10000.0):
        self.bet_type = bet_type.lower()
        self.wheel = wheel.capitalize()
        self.bank = float(bank)
        self.rolls = []
        self.colors = []

    def _color(self, roll):
        if roll in self.red:
            return 'red'
        if roll in self.black:
            return 'black'
        return 'green'

    def spin(self):
        if self.wheel == 'American':
            # 00 represented by 37
            roll = random.randint(0, 37)
        else:
            roll = random.randint(0, 36)
        self.rolls.append(roll)
        self.colors.append(self._color(roll))
        return roll

    def place_bet(self, amount):
        amount = float(amount)
        if amount <= 0:
            raise ValueError('Bet must be > 0')
        if amount > self.bank:
            raise ValueError('Insufficient balance')
        self.bank -= amount
        return amount

    def resolve_bet(self, amount, choice, roll):
        """choice can be int for straight or 'red','black','odd','even'"""
        payout = 0.0
        if isinstance(choice, int):
            # straight
            if roll == choice:
                payout = amount * 36
        else:
            choice_s = str(choice).strip().lower()
            if choice_s in ('red', 'black'):
                if self._color(roll) == choice_s:
                    payout = amount * 2
            elif choice_s == 'odd':
                if roll in self.odd:
                    payout = amount * 2
            elif choice_s == 'even':
                if roll in self.even:
                    payout = amount * 2
            else:
                raise ValueError('Unknown bet type')
        self.bank += payout
        return payout

if __name__ == '__main__':
    r = Roulette()
    print('Starting bank:', r.bank)
    bet = 100
    choice = 'red'
    r.place_bet(bet)
    result = r.spin()
    paid = r.resolve_bet(bet, choice, result)
    print('spin', result, r._color(result), 'payout', paid, 'new bank', r.bank)
    
