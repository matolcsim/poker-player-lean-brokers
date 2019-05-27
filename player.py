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
        if card1_rank != card2_rank:
            counter1 = 1
            counter2 = 1
            for card in board:
                if card == card1_rank:
                    counter1 += 1
                if card == card2_rank:
                    counter2 += 1
            if counter1 == 2 and counter2 == 3 or counter1 == 3 and counter2 == 2:
                return 'fullhouse'

        elif card1_rank == card2_rank:
            counter1 = 2
            counter2 = 1
            sorted = sort_by_ranking(board)
            for i in range(len(sorted)-1):
                if sorted[i+1] == sorted[i]:
                    counter2 += 1
                    if counter2 == 3:
                        return 'fullhouse'
                else:
                    counter = 1



        # FLUSH




        return 'nothing'


    def showdown(self, game_state):
        pass
