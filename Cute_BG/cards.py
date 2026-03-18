import random

# A small set of simple cards that affect victory points or position
CARDS = [
    {"type": "gain_vp", "amount": 2, "text": "Lucky Day! Gain 2 victory points."},
    {"type": "lose_vp", "amount": 1, "text": "Oops! Lose 1 victory point."},
    {"type": "steal_vp", "amount": 1, "text": "Steal 1 victory point from the next player."},
    {"type": "move_forward", "amount": 2, "text": "Speed Boost! Move forward 2 tiles."},
    {"type": "move_backward", "amount": 2, "text": "Trip! Move backward 2 tiles."},
]

def draw_card():
    return random.choice(CARDS)

def apply_card_effect(card, current_player, all_players):
    if card["type"] == "gain_vp":
        current_player.victory_points += card["amount"]
    elif card["type"] == "lose_vp":
        current_player.victory_points = max(0, current_player.victory_points - card["amount"])
    elif card["type"] == "steal_vp":
        # Steal from the next player in the list
        idx = all_players.index(current_player)
        target = all_players[(idx + 1) % len(all_players)]
        if target.victory_points > 0:
            target.victory_points -= card["amount"]
            current_player.victory_points += card["amount"]
    elif card["type"] == "move_forward":
        current_player.tile_index += card["amount"]
    elif card["type"] == "move_backward":
        current_player.tile_index = max(0, current_player.tile_index - card["amount"])
