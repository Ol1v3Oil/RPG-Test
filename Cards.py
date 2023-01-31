import random
class card():
  def __init__(self, name, id = []):
    self.name,  self.id = name, id

  def activate(self, **d):
    #calculate the entity_stats + cards_stats
    return (cards_s(self.name, self.id, **d))

def cards_s(ncard = '', id = [], **dictionary):
  #entity, effect, variables
  # dict = {'bite' : ("user has bitten target" , {'dmg': 1}}
  user = dictionary['user']
  e_list = []
  id.append(ncard)
  for i in id:
    if i == 'dmg' or i == 1:
      print(f"{user.stats['name']} has damaged {dictionary['target'].stats['name']}")
      e_list.append({'dmg' : 2 + user.stats['att']/2})
 
    elif i == 'heal' or i == 2:
      if hc(user, 50) == True:
        print(f"{user.stats['name']} has healed {dictionary['target'].stats['name']}'s injuries")
        e_list.append({'heal' : 2})
 
    elif i == 'stealhp' or i == 3:
       if hc(user, 60) == True:
        print(f"{user.stats['name']} has stolen {dictionary['target'].stats['name']}'s hp'")
        e_list.append({'dmg' : 1 + user.stats['att']/4}, {'heal':1})
   
    elif i == 'stun' or i == 4:
      if hc(user, 30) == True:
        print(f"{user.stats['name']} has stunned {dictionary['target'].stats['name']}")
        e_list.append({'stun': 1}, {'dmg': 1})

  return e_list

def hc(user, chc):
  if random.randint(0,100) <= user.stats['mrl'][1] + chc :
    user.stats['mrl'][1] = user.stats['mrl'][0]
    return True
  else: 
    print(f"{user.stats['name']} has missed")
    user.stats['mrl'][1] += 5
    return False
    