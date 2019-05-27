
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

            # HANDS
            POKER =

            # 'MAIN'
            if player['name'] == "Lean Brokers":

        return 0

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



