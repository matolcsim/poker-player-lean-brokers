
class Player:
    VERSION = "v1.0"

    def betRequest(self, game_state):

        players = game_state['players']
        pot = game_state['pot']
        big_blind = game_state['pot']
        bet = max(pot, big_blind)
        for player in players:
            if player['name'] == "Lean Brokers":
                if player['hole_cards'][0]['rank'] == player['hole_cards'][1]['rank']:
                    return bet

        return 0

    def showdown(self, game_state):
        print(game_state)
        pass

