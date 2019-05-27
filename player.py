
class Player:
    VERSION = "v3.0"

    def betRequest(self, game_state):

        players = game_state['players']


        for player in players:
            # PLAYER CARDS
            card1_rank = player['hole_cards'][0]['rank']
            card1_suit = player['hole_cards'][0]['suit']
            card2_rank = player['hole_cards'][1]['rank']
            card2_suit = player['hole_cards'][1]['suit']


            # BET SIZES
            current_buy_in = game_state['current_buy_in']
            pot = game_state['pot']
            big_blind = game_state['big_blind']
            call = current_buy_in - player['bet']
            half_pot = pot / 2
            bet = max(pot, big_blind)
            all_in = player['stack']

            BOARD = game_state['community_cards']  # LIST

            # 'MAIN'
            if player['name'] == "Lean Brokers":
                if card1_rank == card2_rank:
                    if card1_rank in ['K', 'A', 'Q', 'J']:
                        return all_in
                    elif current_buy_in < (all_in / 5):
                        return call
                elif current_buy_in < (all_in / 5) and (card1_rank in ['8', '9', '10', 'J', 'Q', 'K', 'A']) and diference() < 2: #card1_suit == card2_suit
                    return call


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
                if card == card1_rank:
                    counter1 += 1
                if card == card2_rank:
                    counter2 += 1
            if counter1 == 2 and counter2 == 3 or counter1 == 3 and counter2 == 2:
                return 'fullhouse'

        elif card1_rank == card2_rank:
            counter1 = 2
            counter2 = 1
            sorted_cards = Player().sort_by_ranking(board)
            for i in range(len(sorted_cards) - 1):
                if sorted_cards[i + 1] == sorted_cards[i]:
                    counter2 += 1
                    if counter2 == 3:
                        return 'fullhouse'
                else:
                    counter = 1

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


        # Straight


        return 'nothing'

    def sort_by_ranking(self, community_cards):
        for card in community_cards:
            if card['rank'] == 'J':
                card['rank'] = '11'
            elif card['rank'] == 'Q':
                card['rank'] = '12'
            elif card['rank'] == 'K':
                card['rank'] = '13'
            elif card['rank'] == 'A':
                card['rank'] = '14'

        sorted_cards = sorted(community_cards, key=lambda x: int(x['rank']), reverse=True)

        for card in community_cards:
            if card['rank'] == '11':
                card['rank'] = 'J'
            elif card['rank'] == '12':
                card['rank'] = 'Q'
            elif card['rank'] == '13':
                card['rank'] = 'K'
            elif card['rank'] == '14':
                card['rank'] = 'A'

        return sorted_cards


    def card_differences(self, hole_cards):
        for card in hole_cards:
            if card['rank'] == 'J':
                card['rank'] = 11
            elif card['rank'] == 'Q':
                card['rank'] = 12
            elif card['rank'] == 'K':
                card['rank'] = 13
            elif card['rank'] == 'A':
                card['rank'] = 14
            elif type(card['rank']) == 'string':
                card['rank'] = int(card['rank'])

            sorted_cards = sorted(hole_cards, key=lambda x: int(x['rank']), reverse=True)

            return sorted_cards[0] - sorted_cards[1]


    def showdown(self, game_state):
        pass

    def pair(self, card1_rank, card2_rank, community):

        # RETURN OPTIONS (string):
        # "big_pair"
        # "little_pair"
        # "two_pair"
        # "two_pair_one_big"
        # "two_pair_two_big"

        if card1_rank == card2_rank:
            if card1_rank in ['K', 'A', 'Q', 'J']:
                return "big_pair"
            else:
                return "little_pair"
        else:
            true_pair_1 = 0
            true_pair_2 = 0
            for card in community:
                if card[0] == card1_rank:
                    true_pair_1 += 1
                elif card[0] == card2_rank:
                    true_pair_2 += 1
            if true_pair_1 == 1 and true_pair_2 != 1:
                if card1_rank in ['K', 'A', 'Q', 'J']:
                    return "big_pair"
                else:
                    return 'little_pair'
            elif true_pair_2 == 1 and true_pair_1 != 1:
                if card2_rank in ['K', 'A', 'Q', 'J']:
                    return "big_pair"
                else:
                    return 'little_pair'
            elif true_pair_1 == 1 and true_pair_2 == 1:
                if card1_rank in ['K', 'A', 'Q', 'J'] and card2_rank not in ['K', 'A', 'Q', 'J']:
                    return "two_pair_one_big"
                elif card1_rank not in ['K', 'A', 'Q', 'J'] and card2_rank  in ['K', 'A', 'Q', 'J']:
                    return "two_pair_one_big"
                elif card1_rank in ['K', 'A', 'Q', 'J'] and card2_rank  in ['K', 'A', 'Q', 'J']:
                    return "two_pair_two_big"
                else:
                    return "two_par"

    def drill(self, card1_rank, card2_rank, community):

        # RETURN OPTIONS (string):
        # "big_drill"
        # "little_drill"

        if card1_rank == card2_rank:
            true_drill = 0
            for card in community:
                if card[0] == card1_rank:
                    true_drill += 1
            if true_drill == 1:
                if card1_rank in ['K', 'A', 'Q', 'J']:
                    return "big_drill"
                else:
                    return "little_drill"
        else:
            true_drill_1 = 0
            true_drill_2 = 0
            for card in community:
                if card[0] == card1_rank:
                    true_drill_1 += 1
                elif card[0] == card2_rank:
                    true_drill_2 += 1
            if true_drill_1 == 2:
                if card1_rank in ['K', 'A', 'Q', 'J']:
                    return "big_drill"
                else:
                    return "little_drill"
            elif true_drill_2 == 2:
                if card2_rank in ['K', 'A', 'Q', 'J']:
                    return "big_drill"
                else:
                    return "little_drill"



