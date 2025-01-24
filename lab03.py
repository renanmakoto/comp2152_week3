import random
# dice
diceOptions = list(range(1, 7))
weapons = ['First', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']
print('Available weapons: ', ' '.join(weapons))
def getCombatStrength(prompt):
    while True:
        value = int(input(prompt))
        if 1 <= value <= 6:
            return value
        else:
            print('Invalid input. Please, enter a number between 1 and 6')
combatStrength = getCombatStrength('Enter combat strength 1-6')
mCombatStrength = getCombatStrength('Enter your combat strength 1-6')
for j in range(1, 21, 2):
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)
    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon = weapons[monsterRoll - 1]
    heroTotal = combatStrength + heroRoll
    monsterTotal = mCombatStrength + monsterRoll
    print(f'\n Hero rolled {heroRoll} and Monster rolled {monsterRoll}')
    print(f'\n Hero selected {heroWeapon} and Monster selected {monsterWeapon}')
    print(f'\n Hero total Strength: {heroTotal} and Monster total: {monsterTotal}')
    if heroTotal > monsterTotal:
        print('Hero wins')
    elif heroTotal < monsterTotal:
        print('Monster wins')
    else:
        print("It's a tie.")
if j != 11:
    print(f'\n Battle concluded after 20 rounds!')