def damage(entity, dmg):
  print(f"{entity.stats['name']} has been dmg by {dmg}")
  entity.stats['hp'] -= dmg

def heal(entity, heal):
  print(f"{entity.stats['name']} has been healed by {heal}")
  entity.stats['hp'] += heal

def effect(**dictionary):
  #entity, effect, variables
  entity = dictionary['entity']
  effect = dictionary['effect']

  if effect == 'damage':
    damage(entity, dictionary['dmg'])

  if effect == 'heal':
    heal(entity, dictionary['heal'])