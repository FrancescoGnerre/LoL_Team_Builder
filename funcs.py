import numpy as np
import pandas as pd


# calculates the average elo of all players
def total_average_elo(csv):
    elo = 0.0

    for i in range(csv.shape[0]):
        elo += player_ELO(csv.iloc[i])

    elo = elo/(csv.shape[0])

    return elo


# calculates the elo of a player given the standard format
def player_ELO(player):
    elo = 0.0

    if player.Soloqueue == "Iron":
        elo += 1
    elif player.Soloqueue == "Bronze":
        elo += 2
    elif player.Soloqueue == "Silver":
        elo += 3
    elif player.Soloqueue == "Gold":
        elo += 4
    elif player.Soloqueue == "Platinum":
        elo += 5
    elif player.Soloqueue == "Diamond":
        elo += 6
    else:
        elo += 7

    if player.Flexqueue == "Iron":
        elo += 1
    elif player.Flexqueue == "Bronze":
        elo += 2
    elif player.Flexqueue == "Silver":
        elo += 3
    elif player.Flexqueue == "Gold":
        elo += 4
    elif player.Flexqueue == "Platinum":
        elo += 5
    elif player.Flexqueue == "Diamond":
        elo += 6
    else:
        elo += 7

    elo = elo/2

    return elo


# returns the primary role of a player
def get_primary(player):
    return player.Primary


# returns the secondary role of a player
def get_secondary(player):
    return player.Secondary


# calculates the elo of a team given the elos of all the players in the team
def team_ELO(player_top, player_jungle, player_mid, player_ADC, player_supp):
    elo = 0.0

    elo += player_ELO(player_top)
    elo += player_ELO(player_jungle)
    elo += player_ELO(player_mid)
    elo += player_ELO(player_ADC)
    elo += player_ELO(player_supp)
    elo = elo/5

    return elo
