from GameLogic import Deck

class CardGame:
  deck = Deck()

  def __init__(self, players_count):
    self.players_count = players_count
    pass

  def run(self):
    pass


def main():
  pass

# This condition is true when this file is run with 
# $ python main.py
# It isn't true when we import this file in another file
if __name__ == "__main__":
  main()
