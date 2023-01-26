import action

class card():
  def __init__(self, name, id = []):
    self.name = name
    self.id = id

  def __str__(self):
    return self.name

  def activate(self, **dictionary):
    cards_e(self.name, self.id, **dictionary)
    
  def special(self):
    print()

def cards_e(ncard = '', id = [], **dictionary):
  #entity, effect, variables
  user = dictionary['user']
  id.append(ncard)

  for i in id:
    if i == 'bite' or 1:
      print(f"{user.stats['name']} has bitten {dictionary['target'].stats['name']}")
      
    elif i == 'tend' or 2:
      print(f"{user.stats['name']} has tended {dictionary['target'].stats['name']}'s injuries")