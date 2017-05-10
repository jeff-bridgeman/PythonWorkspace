"""Import."""
from classes.enemy import Character
from classes.game import bcolors
from classes.magic import Spell
from classes.inventory import Item

# Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 50, 200, "black")
quake = Spell("Quake", 14, 120, "black")

# White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Items

potion = Item("Potion", 5, "potion", "Heals 50 HP", 50)
hipotion = Item("Super Potion", 5,  "potion", "Heals for 100 HP", 100)
megapotion = Item("Mega Potion", 5,  "potion", "Heals for 500 HP", 500)
elixer = Item("Elixer", "elixer", 5,  "Fully restores one party member", 9999)
hielixer = Item("MegElixer", 5,  "elixer", "Fully restores party", 9999)

grenade = Item("Holy Hand Grenade",  5, "attack", "Count to thrice", 500)

playerSpells = [fire, thunder, blizzard, meteor, quake, cure, cura]
playerItems = [{"item": potion, "quantity": 15},
               {"item": hipotion, "quantity": 5},
               {"item": megapotion, "quantity": 5},
               {"item": elixer, "quantity": 5},
               {"item": hielixer, "quantity": 2},
               {"item": grenade, "quantity": 5}]

player = Character(460, 65, 60, 34,
                   playerSpells,
                   playerItems)
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

        if magicChoice == -1:
            continue

        spell = player.magic[magicChoice]
        magicDmg = spell.generateDamage()

        currentMp = player.getMp()

        if spell.cost > currentMp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduceMp(spell.cost)
        if spell.type == "white":
            player.heal(magicDmg)
            print(bcolors.OKGREEN + "\n" + spell.name + " heals for",
                  str(magicDmg), "HP", bcolors.ENDC)
        elif spell.type == "black":
            enemy.takeDamage(magicDmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals",
                  str(magicDmg) + bcolors.ENDC)

    elif index == 2:
        player.chooseItem()
        itemChoice = int(input("Choose item: ")) - 1

        if itemChoice == -1:
            continue

        item = player.items[itemChoice]["item"]

        if player.items[itemChoice]["quantity"] == 0:
            print("None left...")
            continue
            
        player.items[itemChoice]["quantity"] -= 1

        if item.type == "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + " heals for",
                  str(item.prop), "HP", bcolors.ENDC)
        elif item.type == "elixer":
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(bcolors.OKGREEN + "\n" + item.name + " fully restores",
                  str(item.prop), "HP/MP", bcolors.ENDC)
        elif item.type == "attack":
            enemy.takeDamage(item.prop)
            print(bcolors.OKBLUE + "\n" + item.name + " deals",
                  str(item.prop) + bcolors.ENDC)

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
