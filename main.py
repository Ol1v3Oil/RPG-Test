import Cards
import Insect
import random

class system():
  def __init__(self):
    self.entities, self.entity_id = [], [0]
    self.c_list = self.p, self.e = card_list('p'), card_list('e')
    
  def adde(self, entity):
    entity.stats['id'] = self.v(self.entity_id)
    self.entities.append(entity)
    self.entity_id.append(self.v(self.entity_id))

  def act(self, card, **d):
    e = card.activate(**d)
    return e #deal damage or effect
  
  def find(self, value, key = 'name'):
    for i in self.entities:
      if i.stats[key] == value:
        return i
        
  def v(self, list):
    if not list: return 0
    elif list[len(list) - 1] == 0: return 1
    else:
      for i in range(len(list) -1):
        if ((list[i + 1]) == list[-1]) and not ((list[i] + 1) != list[i + 1]): 
          return i + 2
        elif (((list[i] + 1) == list[i + 1])) == False: 
          return i + 1

  def after():
    pass

class card_list():
  def __init__(self, team):
    self.team = team
    self.list = {}
    self.amount = 10 #card limit per player
    self.cards = []

  def addc(self, cname, owner, amount = 0, able = True):
    self.list[self.v2(self.list)] =  {'name' : cname, 'owner' : owner, 'amount' : amount} # remove if the insect is knock out

  def addl(self, entity):
    n , c = entity.stats['name'] , entity.cards
    for i in c: self.addc(i.name, n)

  def v2(self, dict):
    l = [0]
    for key, value in dict.items(): l.append(key)
    if not l: return 0
    elif l[len(l) - 1] == 0: return 1
    else:
      for i in range(len(l) -1):
        if ((l[i + 1]) == l[-1]) and not ((l[i] + 1) != l[i + 1]): return i + 2
        elif (((l[i] + 1) == l[i + 1])) == False: return i + 1

  def adda(self, i):
    if self.amount <= 11: pass
    for i in range(0,i):
      while True:
        v = random.randint(1, len(self.list))
        if self.list[v]['amount'] <= 1: 
          self.list[v]['amount'] += 1
          break

  def showable(self):
    t_l = [] # shows available cards
    for k in self.list: # dont
      if self.list[k]['amount'] >= 1 :
        for i in range(0, self.list[k]['amount']):
          t_l.append([self.list[k]['name'], self.list[k]['owner']])

    return t_l

Card1 = Cards.card(name = "slash", id = [1])
Card2 = Cards.card(name = "tend", id = [2])
Card3 = Cards.card(name = "succ", id = [3])
Card4 = Cards.card(name = "bash", id = [4])
  
battle = system()
ant = Insect.insect("Ant", 10, 4, ally = True, cards = [Card1, Card2, Card3, Card4], mrl = 20)
beetle = Insect.insect("Beetle", 15, 2, ally = False, cards = [Card1, Card2, Card3, Card4])

battle.adde(ant)
battle.adde(beetle)
for i in battle.entities: i.display()
 
#print(battle.find(1, key ='id').stats['name'])
battle.p.addl(ant)
battle.e.addl(beetle)
for i in battle.c_list: i.adda(4)
for i in battle.c_list: print(i.showable())
print(battle.act(Card1, user = ant, target = beetle))