"""Import."""
from classes.enemy import Character
from classes.game import bcolors
from classes.magic import Spell
from classes.inventory import Item

# Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 120, "black")

# White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Items

potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Super Potion", "potion", "Heals for 100 HP", 100)
megapotion = Item("Mega Potion", "potion", "Heals for 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores one party member", 9999)
hielixer = Item("MegElixer", "elixer", "Fully restores party", 9999)

grenade = Item("Holy Hand Grenade", "attack", "Count to thrice", 500)

player = Character(460, 65, 60, 34,
                   [fire, thunder, blizzard, meteor, cure, cura],
                   potion)
enemy = Character(1200, 65, 45, 25, [], [])

running = True
i = 0
line = "============================================================\n"

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print(line)
    player.chooseAction()
    choice = input("Choose action: ")
    index = int(choice) - 1

    print("\n")

    if index == 0:
        dmg = player.generateDamage()
        enemy.takeDamage(dmg)
        print("You attack for ", dmg, "points of damage.")
    elif index == 1:
        print("Abilities.")
        player.chooseMagic()
        magicChoice = int(input("Choose magic: ")) - 1

        spell = player.magic[magicChoice]
        magicDmg = spell.generateDamage()

        currentMp = player.getMp()

        if spell.cost > currentMp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduceMp(spell.cost)
        if spell.type == "white":
            player.heal(magicDmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for",
                  str(magicDmg), "HP", bcolors.ENDC)
        elif spell.type == "black":
            enemy.takeDamage(magicDmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals",
                  str(magicDmg) + bcolors.ENDC)

    enemyChoice = 1
    enemyDmg = enemy.generateDamage()
    player.takeDamage(enemyDmg)
    print("Enemy attacks for ", enemyDmg, "\n")

    print(line)

    print("Enemy HP: ", bcolors.FAIL + str(enemy.getHp()) + "/"
          + str(enemy.getMaxHp()) + bcolors.ENDC, "\n")
    print("Your HP: ", bcolors.OKGREEN + str(player.getHp()) + "/"
          + str(player.getMaxHp()) + bcolors.ENDC)
    print("Your MP: ", bcolors.OKBLUE + str(player.getMp()) + "/"
          + str(player.getMaxMp()) + bcolors.ENDC)

    if enemy.getHp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.getHp() == 0:
        print(bcolors.FAIL + "You have been defeated!", bcolors.ENDC)
        running = False
