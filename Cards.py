import random
class card():
  def __init__(self, name, id = []):
    self.name,  self.id = name, id

  def activate(self, **d):
    #calculate the entity_stats + cards_stats
    return (card_s(self.id, **d))

def card_s(id = [], **dicti):
  check = lambda x, l : l.append(x) if x != None else False
  e_list = []
  dict1 ={1 : dmg, 2 : heal, 3 : drain, 4 : bash}
  dict2 ={1 : (dicti['user'], dicti['target']),
          2 : (dicti['user'], dicti['target']),
          3 : (dicti['user'], dicti['target']),
          4 : (dicti['user'], dicti['target']),
          }
  for i in id:
    check(dict1[i](dict2[i]), e_list)
  return e_list

def dmg(list):
  user, target = list[0], list[1]
  print(f"{user.stats['name']} has damaged {target.stats['name']}")
  return ({'dmg' : 2 + user.stats['att']/2})

def heal(list):
  user, target = list[0], list[1]
  if hc(user, 50) == True:
    print(f"{user.stats['name']} has healed       {target.stats['name']}'s injuries")
    return ({'heal' : 2,})

def drain(list):
  user, target = list[0], list[1]
  if hc(user, 60) == True:
   print(f"{user.stats['name']} has stolen {target.stats['name']}'s hp'")
   return ({'dmg' : 1 + user.stats['att']/4}, {'heal':1})

def bash(list):
  user, target = list[0], list[1]
  if hc(user, 30) == True:
    print(f"{user.stats['name']} has stunned {target.stats['name']}")
    return ({'stun': 1}, {'dmg': 1})

def hc(user, chc):
  if random.randint(0,100) <= user.stats['mrl'][1] + chc :
    user.stats['mrl'][1] = user.stats['mrl'][0]
    return True
  else: 
    print(f"{user.stats['name']} has missed")
    user.stats['mrl'][1] += 5
    return False
    
   