import numpy as np
import pandas as pd
import funcs as func

# THIS IS A DEBUG FILE

df = pd.read_csv("test dataset - Sheet1.csv")

print("total average:")
print(func.total_average_elo(df))

print("individual averages:")
for i in range(df.shape[0]):
    print(df.iloc[i].Player)
    print(func.player_ELO(df.iloc[i]))

print("Random Team Average ELO:")
print(func.team_ELO(df.iloc[0], df.iloc[3], df.iloc[5], df.iloc[8], df.iloc[11]))
