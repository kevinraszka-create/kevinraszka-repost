import random

class Roulette: # jednoduchá implementace rulety, bez sázek na sloupce, tucety, atd.
    red = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
    black = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}
    odd = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35}
    even = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36}

    def __init__(self, # defaultně rovnou nastaveno na straight, ale lze změnit
                 bet_type='straight',
                 wheel='American',
                 bank=10000.0):
        self.bet_type = bet_type.lower()
        self.wheel = wheel.capitalize()
        self.bank = float(bank)
        self.rolls = []
        self.colors = []

    def _color(self, roll): # pomocná metoda pro určení barvy čísla
        if roll in self.red:
            return 'red'
        if roll in self.black:
            return 'black'
        return 'green'

    def spin(self): # vrací číslo, které padlo, a zároveň ukládá historii hodů a jejich barvy
        if self.wheel == 'American':
            # 00 represented by 37
            roll = random.randint(0, 37)
        else:
            roll = random.randint(0, 36)
        self.rolls.append(roll)
        self.colors.append(self._color(roll))
        return roll

    def place_bet(self, amount): # kontrola sázky, odečtení z banku, vrací částku, která byla vsazena
        amount = float(amount)
        if amount <= 0:
            raise ValueError('Bet must be > 0')
        if amount > self.bank:
            raise ValueError('Insufficient balance')
        self.bank -= amount
        return amount

    def resolve_bet(self, amount, choice, roll): # výpočet výhry, aktualizace banku, vrací částku, která byla vyplacena
        """choice can be int for straight or 'red','black','odd','even'"""
        payout = 0.0
        if isinstance(choice, int):
            # straight
            if roll == choice:
                payout = amount * 36
        else:  # barva, sudost, lichost
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
 
    def get_roll_display(self, roll):
        if roll == 37:
            return '00'
        return str(roll)

if __name__ == '__main__': # jednoduchá interaktivní smyčka pro testování, lze rozšířit o další typy sázek, více hráčů, atd.
    r = Roulette()
    print('Starting bank:', r.bank)
    while r.bank > 0:
        try:
            bet_input = input("Enter bet amount (or 'quit' to exit): ")
            if bet_input.lower() == 'quit':
                break
            bet = float(bet_input)
            choice_input = input("Enter choice (number for straight, or 'red', 'black', 'odd', 'even'): ")
            if choice_input.isdigit():
                choice = int(choice_input)
            else:
                choice = choice_input.lower()
            r.place_bet(bet)
            roll = r.spin()
            payout = r.resolve_bet(bet, choice, roll)
            roll_display = r.get_roll_display(roll)
            print(f"Rolled {roll_display} ({r._color(roll)}), payout {payout}, new bank {r.bank}")
        except ValueError as e:
            print(f"Error: {e}")
    print('Game over. Final bank:', r.bank)
