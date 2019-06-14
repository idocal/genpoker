from pypokerengine.api.game import setup_config, start_poker
from RanomPlayer import RandomPlayer

# Game general configuration
config = setup_config(max_round=10, initial_stack=100, small_blind_amount=5)

# Define AI players
config.register_player(name="p1", algorithm=RandomPlayer())
config.register_player(name="p2", algorithm=RandomPlayer())

# Start Poker game
game_result = start_poker(config, verbose=1)
