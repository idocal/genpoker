from pypokerengine.players import BasePokerPlayer
import numpy as np


class RandomPlayer(BasePokerPlayer):

    def declare_action(self, valid_actions, hole_card, round_state):
        # Randomly pick a valid action
        random_action_info = np.random.choice(valid_actions)
        action = random_action_info["action"]
        amount = random_action_info["amount"]

        if isinstance(amount, dict):
            amount = np.random.randint(low=amount['min'], high=amount['max'])

        return action, amount

    def receive_game_start_message(self, game_info):
        pass

    def receive_round_start_message(self, round_count, hole_card, seats):
        pass

    def receive_street_start_message(self, street, round_state):
        pass

    def receive_game_update_message(self, action, round_state):
        pass

    def receive_round_result_message(self, winners, hand_info, round_state):
        pass
