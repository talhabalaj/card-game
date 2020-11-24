from random import shuffle


class Card:
  CARD_TYPES = ["PAN", "PATI", "DIL", "DIAMOND"]
  CARD_NUMBERS = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

  def __init__(self, number, card_type):
    assert number >= 1 and number <= 13, 'Card number not valid'
    assert card_type in Card.CARD_TYPES, 'Card type not valid'
    self.number = number
    self.card_type = card_type

  # when we print an object, this function is
  # used to convert it to printable form
  # https://stackoverflow.com/questions/4912852/how-do-i-change-the-string-representation-of-a-python-class
  def __str__(self):
    return f"{Card.CARD_NUMBERS[self.number]} of ${self.card_type}"


class Deck:

  def __init__(self):
    self.cards = []
    for i in Card.CARD_TYPES:
      for j in Card.CARD_NUMBERS:
        self.cards.append(Card(j, i))

  def shuffle(self):
    shuffle(self.cards)
