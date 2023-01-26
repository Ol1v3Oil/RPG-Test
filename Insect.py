import Cards

class insect():
  def __init__(self, name, hp, att, ally = False, cards = []):
    self.stats = { "name": name, "hp" : hp, "att" : att, "ally" : ally}
    self.cards = []
    self.effect = {}
    #add id

  def display(self):
    temp = []
    for i in range(len(self.cards)):
      temp.append(self.cards[i].name)
    print(f"{self.stats}, cards:{temp}")

  