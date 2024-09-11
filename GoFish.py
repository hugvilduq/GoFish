# """GoFish.py: Plays a GoFish match with two machines competing onto each other
# 
#   -"strategy"?
    # can machines get better at the game? ML?
# 
# """
import random

__author__      = "Hugo Villanueva"
__copyright__   = "Open source code 2022, Planet Earth"

# class creation
class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
        self.name = str(value) + " " + color


# deck suits (also possible with spanish deck)
colors = ['hearts', 'diamonds', 'spades', 'clubs']


# deck creation with list comprehension
deck = [Card(value, color) for value in range(1, 14) for color in colors]

random.shuffle(deck)

# initialization of the players
alice=[]
bob=[]

def draw(player):
    card = deck.pop()
    player.append(card)

found=False






# drawing cards
for i in range(7):
    draw(alice)
    draw(bob)

# CARTAS INICIALES
print("Cartas iniciales:")
print("Alice:",[c.name for c in alice])
print("Bob:",[c.name for c in bob])

# Mover cartas iguales al final
def reshuffle(player):
    first_value=player[0].value
    player_copy=player.copy()

    for c in player_copy:
        if c.value==first_value:
            player.remove(c)
            player.append(c)

    player_copy=[]


def ask(player_asking,player_stolen,given_card):
    found=False
    for c in player_stolen:
        if given_card.value==c.value:
            print("Here, have my ", c.name)
            player_asking.insert(0,c)
            player_stolen.remove(c)
            found=True 
    return found

# def turno:
# # Alice pregunta:

def player_name(player):
    if player=="Alice":
        return "Alice"
    else:
        return "Bob"

def turno(active):

    if active==alice:
        passive=bob
    else:
        passive=alice

    if deck==[]:
        print("\n game over")

        print("Alice:",[c.name for c in alice])
        print("Bob:",[c.name for c in bob])
    else: 
        
        print("Cartas actuales:")
        print("Alice:",[c.name for c in alice])
        print("Bob:",[c.name for c in bob])

        reshuffle(active)

    # Asking for a card
        print("Hey {}, do you have a {} ?".format(player_name(passive),active[0].value))
        if ask(active,passive,active[0]): 
            turno(active)
        else:
            draw(active)
            turno(passive)


turno(alice)


reshuffle(alice)
print("Alice:",[c.name for c in alice])

















