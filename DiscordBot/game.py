import random

class Card:
    def __init__(self, name, min_value, max_value, card_type, card_type_detail, card_element, attack_type):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        self.card_type = card_type
        self.card_type_detail = card_type_detail
        self.card_elem = card_element
        self.attack_type = attack_type

    def __str__(self):
        return self.name

    def effect(self):
        return random.randint(self.min_value, self.max_value)

class Deck:
    def __init__(self, cards):
        self.cards = cards[:]
        self.discard_pile = []
        random.shuffle(self.cards)

    def draw_card(self):
        if not self.cards:
            self.reshuffle_deck()
        return self.cards.pop()

    def discard_card(self, card):
        self.discard_pile.append(card)

    def reshuffle_deck(self):
        self.cards = self.discard_pile[:]
        self.discard_pile = []
        random.shuffle(self.cards)

    # Changed hand_size to 5
    def starting_hand(self, hand_size=5):
        return [self.draw_card() for _ in range(hand_size)]

class Player:
    def __init__(self, name, hit_points, deck):
        self.name = name
        self.max_hit_points = hit_points
        self.hit_points = hit_points
        self.deck = deck
        # Changed hand_size to 5
        self.hand = self.deck.starting_hand(hand_size=5)

    def draw_card(self):
        self.hand.append(self.deck.draw_card())

    def play_card(self, card_index, target):
        card = self.hand.pop(card_index)
        value = card.effect()
        if card.card_type == 'attack':
            target.hit_points -= value
            result = f'{self.name} uses {card.name} and deals {value} damage to {target.name}!'
        elif card.card_type == 'support':
            self.hit_points = min(self.max_hit_points, self.hit_points + value)
            result = f'{self.name} uses {card.name} and heals {value} hit points!'
        self.deck.discard_card(card)
        return result

    def is_alive(self):
        return self.hit_points > 0

class Monster:
    def __init__(self, name, hit_points, attack_power):
        self.name = name
        self.hit_points = hit_points
        self.attack_power = attack_power

    def attack(self, target):
        damage = random.randint(1, self.attack_power)
        target.hit_points -= damage
        return damage

    def is_alive(self):
        return self.hit_points > 0

class GameState:
    def __init__(self, player, monsters):
        self.player = player
        self.monsters = monsters

    def display_health(self):
        health_status = f'{self.player.name} HP: {self.player.hit_points}/{self.player.max_hit_points}\n'
        for i, monster in enumerate(self.monsters):
            health_status += f'{i + 1}. {monster.name} HP: {monster.hit_points}\n'
        return health_status

    def player_turn(self, card_choice, target_index):
        target = self.monsters[target_index]
        result = self.player.play_card(card_choice, target)
        self.player.draw_card()
        if not target.is_alive():
            result += f'\n{target.name} is defeated!'
            self.monsters.pop(target_index)
        return result

    def monster_turn(self):
        results = []
        for monster in self.monsters:
            if monster.is_alive():
                damage = monster.attack(self.player)
                results.append(f'{monster.name} attacks {self.player.name} for {damage} damage!')
        return '\n'.join(results)

    def is_combat_over(self):
        return not self.player.is_alive() or not any(monster.is_alive() for monster in self.monsters)

    def combat_result(self):
        if self.player.is_alive():
            return f'{self.player.name} has won the battle!'
        else:
            return f'{self.player.name} has been defeated...'

# List of possible monsters
monsters_grasslands = [
    {'name': 'Bees', 'hit_points': 10, 'attack_power': 3},
    {'name': 'Thief', 'hit_points': 15, 'attack_power': 5},
    {'name': 'Living Rock', 'hit_points': 20, 'attack_power': 4},
    {'name': 'Evil Grandma', 'hit_points': 12, 'attack_power': 2},
    {'name': 'Wolf', 'hit_points': 18, 'attack_power': 6},
]

# Create a deck of cards
cards = [
    Card("Punch", 1, 3, 'attack', 'melee attack', 'normal', 'physical'),
    Card("Punch", 1, 3, 'attack', 'melee attack', 'normal', 'physical'),
    Card("Punch", 1, 3, 'attack', 'melee attack', 'normal', 'physical'),
    Card("Punch", 1, 3, 'attack', 'melee attack', 'normal', 'physical'),
    Card("Punch", 1, 3, 'attack', 'melee attack', 'normal', 'physical'),
    Card("Punch", 1, 3, 'attack', 'melee attack', 'normal', 'physical'),
    Card("Kick", 2, 5, 'attack', 'melee attack', 'normal', 'physical'),
    Card("Kick", 2, 5, 'attack', 'melee attack', 'normal', 'physical'),
    Card("Kick", 2, 5, 'attack', 'melee attack', 'normal', 'physical'),
    Card("Kick", 2, 5, 'attack', 'melee attack', 'normal', 'physical'),
    Card("Kick", 2, 5, 'attack', 'melee attack', 'normal', 'physical'),
    Card("Slash", 3, 7, 'attack', 'melee attack', 'normal', 'physical'),
    Card("Slash", 3, 7, 'attack', 'melee attack', 'normal', 'physical'),
    Card("Slash", 3, 7, 'attack', 'melee attack', 'normal', 'physical'),
    Card("Fireball", 4, 9, 'attack', 'spell', 'magic', 'fire'),
    Card("Fireball", 4, 9, 'attack', 'spell', 'magic', 'fire'),
    Card("Heal", 5, 7, 'support', 'spell', 'magic', 'heal'),
    Card("Heal", 5, 7, 'support', 'spell', 'magic', 'heal'),
    Card("Jump Kick", 2, 8, 'attack', 'melee attack', 'normal', 'physical'),
    Card('Ice Ray', 5, 7, 'attack', 'spell', 'magic', 'ice'),
    Card('Ice Ray', 5, 7, 'attack', 'spell', 'magic', 'ice')
]

def create_game(player_name):
    deck = Deck(cards)
    player = Player(name=player_name, hit_points=30, deck=deck)
    monster_data = random.choice(monsters_grasslands)

    # Handle the case where the monster is Bees, spawning two Bees instead of one
    if monster_data['name'] == 'Bees':
        monsters = [Monster(name='Bee', hit_points=monster_data['hit_points'], attack_power=monster_data['attack_power']),
                    Monster(name='Bee', hit_points=monster_data['hit_points'], attack_power=monster_data['attack_power'])]
    else:
        monsters = [Monster(name=monster_data['name'], hit_points=monster_data['hit_points'], attack_power=monster_data['attack_power'])]

    return GameState(player, monsters)
