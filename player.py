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

    def hands(self, board, card1_rank, card2_rank, card1_suit, card2_suit):
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
                if card['rank'] == card1_rank:
                    counter1 += 1
                if card['rank'] == card2_rank:
                    counter2 += 1
            if counter1 == 2 and counter2 == 3 or counter1 == 3 and counter2 == 2:
                return 'fullhouse'

        elif card1_rank == card2_rank:
            counter1 = 2
            counter2 = 1
            sorted = Player().sort_by_ranking(self, board)
            print(sorted)
            for i in range(len(sorted) - 1):
                if sorted[i]['rank'] == sorted[i + 1]['rank']:
                    counter2 += 1
                    if counter1 == 2 and counter2 == 3 or counter1 == 3 and counter2 == 2:
                        return 'fullhouse'
                if sorted[i]['rank'] == card1_rank:
                    counter1 += 1
                    if counter1 == 2 and counter2 == 3 or counter1 == 3 and counter2 == 2:
                        return 'fullhouse'



        # FLUSH
            if card1_suit == card2_suit:
                suit_counter = 2
            for card in board:
                if card['suit'] == card1_suit:
                    counter += 1
                if counter == 5:
                    return 'flush'

            if card1_suit != card2_suit:
                suit1_counter = 1
                suit2_counter = 1
                for card in board:
                    if card['suit'] == card1_suit:
                        suit1_counter += 1
                    elif card['suit'] == card2_suit:
                        suit2_counter += 1
                if suit1_counter >= 5 or suit2_counter >= 5:
                    return 'flush'

        return 'nothing'

    def sort_by_ranking(self, board):
        for card in board:
            if card['rank'] == 'J':
                card['rank'] = '11'
            elif card['rank'] == 'Q':
                card['rank'] = '12'
            elif card['rank'] == 'K':
                card['rank'] = '13'
            elif card['rank'] == 'A':
                card['rank'] = '14'

        sorted_cards = sorted(board, key=lambda x: int(x['rank']), reverse=True)

        for card in board:
            if card['rank'] == '11':
                card['rank'] = 'J'
            elif card['rank'] == '12':
                card['rank'] = 'Q'
            elif card['rank'] == '13':
                card['rank'] = 'K'
            elif card['rank'] == '14':
                card['rank'] = 'A'

        return sorted_cards


    def showdown(self, game_state):
        pass
