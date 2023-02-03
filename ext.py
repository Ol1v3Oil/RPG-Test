def turn(e, **dic):
  #e = [{'dmg': 4.0}]
  i = None
  dict = {'dmg' : dmg, 'heal' : heal, 'stun' : eff}
  dict2={'dmg': (dic['target'], e[i]['dmg']),
         'heal' : (dic['target'], e[i]['heal']),
         'stun' : (dic['target'], e[i]['stun']),
         }
  for i in e:
    pass
  pass

def dmg(target, amm):
  target.stats['hp'] -= amm

def heal(target, amm):
  target.stats['hp'][1] += amm
  if target.stats['hp'][1] > target.stats['hp'][0]: target.stats['hp'][1] = target.stats['hp'][0]

def eff(target, amm):
  temp = []
  for keys in amm.items(): temp.append(keys)
  if not target.stats['effects'].has_key(temp[0]): 
    target.stats['effects'][temp[0]] = amm[temp[0]]
  else: target.stats['effects'][temp[0]] += amm[temp[0]]