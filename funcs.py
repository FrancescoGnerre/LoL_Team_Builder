# import numpy as np
# import pandas as pd


# calculates the average elo of all players
#takes in a list of all of objects with all players and runs through it
def total_average_elo(list):
    elo = 0.0

    for i in list:
        elo += i.Elo

    elo = elo/(len(list))

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
#i got these to work with objects so they take in player objects
def team_ELO(player_top, player_jungle, player_mid, player_ADC, player_supp):
    elo = 0.0

    elo += player_top.Elo
    elo += player_jungle.Elo
    elo += player_mid.Elo
    elo += player_ADC.Elo
    elo += player_supp.Elo
    elo = elo/5

    return elo