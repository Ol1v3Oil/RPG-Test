import action
import Cards
import Insect

class system():
  def __init__(self):
    self.entities = []
    self.entities2 = {}
    self.entity_id = [0]
    #entity address : [card, team, name, id]

  def adde(self, entity):
    self.entities.append(entity)
    self.entities2[entity] = {"card": entity.cards, "team": entity.stats['ally'], "name" : entity.stats['name'], "id" : self.v(self.entity_id)}
    self.entity_id.append(self.v(self.entity_id))

  def addc(self, card):
    pass
    
  def input(self):
    pass

  def find(self, name):
    for i in self.entities:
      #check name
      if i.stats['name'] == name:
        return i

  def find_id(self, id):
    for key1,value1 in self.entities2.items():
      if id ==  self.entities2[key1]['id']:
        return key1
      
  def v(self, list):
    if not list: return 0
    elif list[len(list) - 1] == 0: return 1
    else:
      for i in range(len(list) -1):
        if ((list[i + 1]) == list[-1]) and not ((list[i] + 1) != list[i + 1]): 
          return i + 2
        elif (((list[i] + 1) == list[i + 1])) == False: 
          return i + 1

  def dealdmg(self, name, dmg):
    entity = self.find(name)
    entity.stats['hp'] -= dmg
    print(entity.stats['hp'])


Card1 = Cards.card(name = "bite")
Card2 = Cards.card(name = "tend")
  
battle = system()
ant = Insect.insect("Ant", 10, 3, ally = True, cards = [])
beetle = Insect.insect("Beetle", 15, 2, ally = False)

battle.adde(ant)
battle.adde(beetle)
print(battle.entities2)
for i in battle.entities:
  i.display()


#cardstats.cards(user = ant, ncard = 'tend', target = beetle)
Card2.activate(user = ant, target = beetle)
print(battle.entities2[battle.find_id(1)]['name'])
