class Card:
    suits = ["\u2666", "\u2665", "\u2663", "\u2660"]
    values = ["7", "8", "9", "10", "S", "U", "K", "A"]
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{Card.values[self.value]}{Card.suits[self.suit]}"


c1 = Card(0, 0)
c2 = Card(3, 7)
print(c1)
print(c2)