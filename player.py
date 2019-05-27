class Player:
    VERSION = "v1.0"

    def betRequest(self, game_state):

        players = game_state['players']

        for player in players:
            # PLAYER CARDS
            card1_rank = player['hole_cards'][0]['rank']
            card1_suite = player['hole_cards'][0]['suite']
            card2_rank = player['hole_cards'][1]['rank']
            card2_suite = player['hole_cards'][1]['suite']

            # BET SIZES
            pot = game_state['pot']
            big_blind = game_state['big_blind']
            half_pot = pot / 2
            bet = max(pot, big_blind)
            all_in = player['stack']

            BOARD = game_state['community_cards']  # LIST

            # 'MAIN'
            if player['name'] == "Lean Brokers":
                if player['hole_cards'][0]['rank'] == player['hole_cards'][1]['rank']:
                    if player['hole_cards'][0]['rank'] in ['K', 'A', 'Q', 'J']:
                        return player['stack']
                    return bet

        return 0

    def hands(self, board, card1_rank, card2_rank):
        # HANDS
        # POKER
        if card1_rank == card2_rank:
            counter = 2
        elif card1_rank != card2_rank:
            counter = 1
        for card in board:
            if card['rank'] == card1_rank:
                counter += 1
            if counter == 4:
                return 'poker'

        if card1_rank == card2_rank:
            counter = 2
        elif card1_rank != card2_rank:
            counter = 1
        for card in board:
            if card['rank'] == card2_rank:
                counter += 1
            if counter == 4:
                return 'poker'


        # FULL HOUSE
        counter1 = 0
        counter2 = 0
        for card in board:


    def showdown(self, game_state):
        pass
