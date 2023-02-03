import Cards

class insect():
  def __init__(self, name, hp, att, ally = False, cards = [], mrl = 0, speed = 1):
    self.stats = {
      "name": name, 
      "hp" : [hp, hp], 
      "att" : att, 
      "effects": {}, 
      "spd" : 1,
      "mrl" : [mrl , mrl],
      "ally" : ally, 
      "id" : 0,
      "able": True}
    self.cards = cards
    self.body = {"body" : [], 
                 "head" : [], 
                 "legs" : [], 
                 "back" : [], 
                 "tail" : []} #card, stats, name, id
    #add id, make it so that the parts are the stats

  def display(self):
    temp = []
    for i in range(len(self.cards)):
      temp.append(self.cards[i].name)
    print(f"{self.stats}, \n cards:{temp}")


class parts():
  def __init__(self, name, part, card, **stats):
    self.name, self.part, self.card = name, part, card
    self.stats = stats #adds to the body

def part_stats():
  pass