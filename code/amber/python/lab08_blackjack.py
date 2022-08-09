# BLACKJACK ADVICE

# ask the player for cards using a dictionary

card_dict = {
  'A': 1,
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  '10': 10,
  'J': 10,
  'Q': 10,
  'K': 10
  }

def bj_machine(card_input):
  card_value = 0

  for item in card_dict.items():
    key = item[0]
    value = item[1]

    if card_input == key:
      card_value += value

  if card_input not in card_dict.keys():
    return False

  return card_value

total_value = 0

hit_me = 'y'

while hit_me == 'y':

  user_card = input('What\'s your first card? ').upper()
  hit_value = bj_machine(user_card)
  total_value += hit_value

  user_card = input('What\'s your second card? ').upper()
  hit_value = bj_machine(user_card)
  total_value += hit_value

  user_card = input('What\'s your third card? ').upper()
  hit_value = bj_machine(user_card)
  total_value += hit_value

  if total_value >= 17 and total_value <= 21:
    print(f'{total_value} Stay.')
    hit_me - input('Play again? y/n: ')

  elif total_value == 21:
    print(f'{total_value} Blackjack!')
    hit_me - input('Play again? y/n: ')

  else:
    print(f'{total_value} Already busted!')
    hit_me - input('Play again? y/n: ')

    if hit_me == 'n':
      print('Fine, bye!')
      break

    else:
      total_value = 0
      continue
