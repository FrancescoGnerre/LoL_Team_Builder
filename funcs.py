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

    if player.Soloqueue == "Iron4":
        elo += 1
    elif player.Soloqueue == "Iron3":
        elo += 1.25
    elif player.Soloqueue == "Iron2":
        elo += 1.5
    elif player.Soloqueue == "Iron1":
        elo += 1.75
    elif player.Soloqueue == "Bronze4":
        elo += 2
    elif player.Soloqueue == "Bronze3":
        elo += 2.25
    elif player.Soloqueue == "Bronze2":
        elo += 2.5
    elif player.Soloqueue == "Bronze1":
        elo += 2.75
    elif player.Soloqueue == "Silver4":
        elo += 3
    elif player.Soloqueue == "Silver3":
        elo += 3.25
    elif player.Soloqueue == "Silver2":
        elo += 3.5
    elif plauer.Soloqueue == "Silver1":
        elo += 3.75
    elif player.Soloqueue == "Gold4":
        elo += 4
    elif player.Soloqueue == "Gold3":
        elo += 4.25
    elif player.Soloqueue == "Gold2":
        elo += 4.5
    elif player.Soloqueue == "Gold1":
        elo += 4.75
    elif player.Soloqueue == "Platinum4":
        elo += 5
    elif player.Soloqueue == "Platinum3":
        elo += 5.25
    elif player.Soloqueue == "Platinum2":
        elo += 5.5
    elif player.Soloqueue == "Platinum1":
        elo += 5.75
    elif player.Soloqueue == "Diamond4":
        elo += 6
    elif player.Soloqueue == "Diamond3":
        elo += 6.25
    elif player.Soloqueue == "Diamond2":
        elo += 6.5
    elif player.Soloqueue == "Diamond3":
        elo += 6.75
    else:
        elo += 7

    if player.Flexqueue == "Iron4":
        elo += 1
    elif player.Flexqueue == "Iron3":
        elo += 1.25
    elif player.Flexqueue == "Iron2":
        elo += 1.5
    elif player.Flexqueue == "Iron1":
        elo += 1.75
    elif player.Flexqueue == "Bronze4":
        elo += 2
    elif player.Flexqueue == "Bronze3":
        elo += 2.25
    elif player.Flexqueue == "Bronze2":
        elo += 2.5
    elif player.Flexqueue == "Bronze1":
        elo += 2.75
    elif player.Flexqueue == "Silver4":
        elo += 3
    elif player.Flexqueue == "Silver3":
        elo += 3.25
    elif player.Flexqueue == "Silver2":
        elo += 3.5
    elif plauer.Flexqueue == "Silver1":
        elo += 3.75
    elif player.Flexqueue == "Gold4":
        elo += 4
    elif player.Flexqueue == "Gold3":
        elo += 4.25
    elif player.Flexqueue == "Gold2":
        elo += 4.5
    elif player.Flexqueue == "Gold1":
        elo += 4.75
    elif player.Flexqueue == "Platinum4":
        elo += 5
    elif player.Flexqueue == "Platinum3":
        elo += 5.25
    elif player.Flexqueue == "Platinum2":
        elo += 5.5
    elif player.Flexqueue == "Platinum1":
        elo += 5.75
    elif player.Flexqueue == "Diamond4":
        elo += 6
    elif player.Flexqueue == "Diamond3":
        elo += 6.25
    elif player.Flexqueue == "Diamond2":
        elo += 6.5
    elif player.Flexqueue == "Diamond1":
        elo += 6.75
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
