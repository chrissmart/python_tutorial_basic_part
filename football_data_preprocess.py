"""
This py file introduces the basic 
manipulation of data
"""

"""
import data
"""
import pandas as pd
df_match = pd.read_csv(r"C:\Users\chris\Desktop\StatisticsAIDevp\techFun\WorldCupPlayers.csv\WorldCupMatches.csv")
df_match.info()
df_match.head()

# As a coach, what kind of information you would like to know more so that you can help your team?

"""
data preprocess
"""
df_match_target = df_match[(df_match['Home Team Name'] == 'Spain') | (df_match['Away Team Name'] == 'Spain')].reset_index(drop=True)
df_match_target = df_match[(df_match['Home Team Name'] == 'Spain')].reset_index(drop=True)
df_match_target.tail()

"""
calculate data
"""

# + operator
df_match_target['Home Team Goals'].iloc[-1] + df_match_target['Away Team Goals'].iloc[-1]

# - operator
df_match_target['Home Team Goals'].iloc[-1] - df_match_target['Away Team Goals'].iloc[-1]

# * operator

# / operator

# % operator

# placeholder
slogan = "The best team in the world in %d is %s !"
print(slogan%(2018, "Spanin"))

