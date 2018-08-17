import Deck

d1 = Deck.Deck(10)
d2 = Deck.Deck(10)
d1a = 0
d1h = 0
d2a = 0
d2h = 0
for c in d1.get_deck():
    print(str(c.get_attack()) + '/' + str(c.get_health()))
    d1a += c.get_attack()
    d1h += c.get_health()
print("VS")
for c in d2.get_deck():
    print(str(c.get_attack()) + '/' + str(c.get_health()))
    d2a += c.get_attack()
    d2h += c.get_health()
pointer1 = 0
pointer2 = 0
while pointer1 < len(d1.get_deck()) and pointer2 < len(d2.get_deck()):

    print("Player1's " + str(pointer1 + 1) + 'th card: ' + str(d1.get_deck()[pointer1].get_attack()) + '/' + str(
        d1.get_deck()[pointer1].get_health()) + ' and '
                                                "Player2's " + str(pointer2 + 1) + 'th card: ' + str(
        d2.get_deck()[pointer2].get_attack()) + '/' + str(d2.get_deck()[pointer2].get_health()) + ' are attacking!')
    remainingHealth1 = d1.get_deck()[pointer1].get_health() - d2.get_deck()[pointer2].get_attack()
    remainingHealth2 = d2.get_deck()[pointer2].get_health() - d1.get_deck()[pointer1].get_attack()
    if remainingHealth1 > 0:
        d1.get_deck()[pointer1].set_health(remainingHealth1)
        print("Player1's " + str(pointer1 + 1) + 'th card lived with ' + str(
            d1.get_deck()[pointer1].get_health()) + ' health!')
    else:
        print("Player1's card died!")
        pointer1 += 1

    if remainingHealth2 > 0:
        d2.get_deck()[pointer2].set_health(remainingHealth2)
        print("Player2's " + str(pointer2 + 1) + 'th card lived with ' + str(
            d2.get_deck()[pointer2].get_health()) + ' health!')
    else:
        print("Player2's card died!")
        pointer2 += 1

if pointer1 == pointer2:
    print("It's a tie!")
elif pointer1 == len(d1.get_deck()):
    print('Player2 won!')

elif pointer2 == len(d2.get_deck()):
    print('Player1 won!')
print(d1a, d1h, d2a, d2h)
