import random
import os
from game_data import data
from art import logo, vs

def get_name():
  names = []
  for num in range(len(data)):
    names.append(data[num]['name'])
  return names

def get_description(person):
  for num in range(len(data)):
    if person == data[num]['name']:
      description = data[num]['description']
  return description

def get_country(person):
  for num in range(len(data)):
   if person == data[num]['name']:
     country = data[num]['country']
  return country

def get_follower_count(person):
  for num in range(len(data)):
    if person == data[num]['name']:
      follower_count = data[num]['follower_count']
  return follower_count

def higher_lower():
  playing = True
  names = get_name()
  lives = 1
  current_score = 0

  print(logo)

  person_b = random.choice(names)
  
  while playing:
    person_a = person_b

    if person_a == person_b:
      while person_a == person_b:
        person_b = random.choice(names)

    person_a_description = get_description(person_a)
    person_b_description = get_description(person_b)

    person_a_country = get_country(person_a)
    person_b_country = get_country(person_b)

    person_a_follower_count = get_follower_count(person_a)
    person_b_follower_count = get_follower_count(person_b)


    print(f"Compare A: {person_a}, a {person_a_description}, from {person_a_country}")
    print(vs)
    print(f"Against B: {person_b}, a {person_b_description}, from {person_b_country}")

    choice = input('Who has more followers? Type \'A\' or \'B\': ').lower()

    if choice == 'a' and person_a_follower_count > person_b_follower_count:
      os.system('cls')
      print(logo)
      current_score += 1
      print(f'Your right! Current score: {current_score}')
    elif choice == 'b' and person_b_follower_count > person_a_follower_count:
      os.system('cls')
      print(logo)
      current_score += 1
      print(f'Your right! Current score: {current_score}')
    elif choice == 'a' and person_a_follower_count < person_b_follower_count:
      os.system('cls')
      print(logo)
      print(f'Sorry, that\'s wrong. Final score: {current_score}')
      lives -= 1
    elif choice == 'b' and person_b_follower_count < person_a_follower_count:
      os.system('cls')
      print(logo)
      print(f'Sorry, that\'s wrong. Final score: {current_score}')
      lives -= 1
    

    if lives == 0:
      playing = False

higher_lower()
