from functools import reduce
from random import shuffle

FIGURE_CARDS = 'A K Q J'.split()
NUMBER_CARDS = '10 9 8 7 6 5 4 3 2'.split()

ORDERED_CARDS = 'A K Q J 10 9 8 7 6 5 4 3 2'.split()


class Deck():
    def __init__(self):
        self.deck = ORDERED_CARDS * 4
        shuffle(self.deck)

    def draw_cards(self, player_num):
        return self.deck[player_num*26:(player_num+1)*26]


class Player():
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        self.taken_cards = []
        self.score = 0

    def play_card(self):
        return self.cards.pop()

    def take_cards(self, cards):
        self.taken_cards.extend(cards)
        self.score += \
            reduce(lambda x,y: 28 - (ORDERED_CARDS.index(x) + ORDERED_CARDS.index(y)),
                   cards)

    def has_cards(self):
        return self.cards != []


class War():
    def __init__(self):
        self.deck = Deck()
        self.player1 = Player("Gosho", self.deck.draw_cards(0))
        self.player2 = Player("Pesho", self.deck.draw_cards(1))

    def play_round(self):
        while(self.player1.has_cards() and self.player1.has_cards()):
            player1_card = self.player1.play_card()
            player2_card = self.player2.play_card()

            played_cards = [player1_card, player2_card]
            if player1_card == player2_card:
                # iniate war
                player_won = self.play_war(played_cards)
                if player_won:
                    player_won.take_cards(played_cards)
                continue

            if ORDERED_CARDS.index(player1_card) < \
                    ORDERED_CARDS.index(player2_card):
                self.player1.take_cards(played_cards)
            else:
                self.player2.take_cards(played_cards)
        else:
            # One (or both) of the players is out of cards
            player1_score = self.player1.score
            player2_score = self.player2.score
            print(f"Player 1 score: {player1_score}")
            print(f"Player 2 score: {player2_score}")

    def play_war(self, played_cards):
        # Draw 2 cards, if possible
        players_with_cards = list(filter(lambda player: player.has_cards(),
                                         [self.player1, self.player2]))

        if not players_with_cards:
            # No players with cards left
            return
        if len(players_with_cards) == 1:
            # Only 1 player with cards left, so he is the winner
            return players_with_cards[0]

        player1_card = self.player1.play_card()
        player2_card = self.player2.play_card()

        if player1_card == player2_card:
            # iniate war
            played_cards.extend([player1_card, player2_card])
            self.play_war(played_cards)

        if ORDERED_CARDS.index(player1_card) < ORDERED_CARDS.index(player2_card):
            return self.player1
        else:
            return self.player2


if __name__ == '__main__':
    print("Starting game of War...")
    war = War()
    war.play_round()
    print("War game ended!")
