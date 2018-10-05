"""
This py file is used to demonstrate the data structure in python lanauge
via the world cup dataset.
. Dataframe
. Array
. List
. Tuple
. Dictionary
. Set
"""

"""
Dataframe
"""
import pandas as pd

# create: import data
df_player = pd.read_csv(r".\dataset\WorldCupPlayers.csv")

# read: inspect data structure
df_player.info() # show overall information
df_player.head() # show the first five rows

df_player.index # show the total number of rows
df_player.columns # show all columns

# read: find data
df_player.loc[0:2, ['Coach Name']]
df_player.iloc[0:2, 3]
df_player['Coach Name'][0:2]

# update: edit data
df_player.iloc[-1, 3] = 'Chris Chien (Earth)' # change the value of the last row
df_player = df_player.append({'Player Name': 'Ian Chen (Universe)'}, ignore_index=True) # add a new row

# delete
df_player = df_player.iloc[:-1, :] # remove the last row


"""
Array
"""
import numpy as np
# create: import data
array_player = df_player.values

# read: inspect data structure
array_player.shape # show the number of rows and columns in an array

# read: find data
array_player[0] # show the first row
array_player[0][0] # show the first element in the first row

# update: 
array_player[-1][0] = 201
array_player = np.append(array_player, [[201, 1096.0, 'Universe', 'Christopher Chris (Universe)', 'S', 0.0, 'Faster Chien', 'GK', None]], axis=0)

# delete:
array_player = np.delete(array_player, -1, axis = 0)


"""
List
"""
# create: import data
list_player = df_player.values.tolist()

# read: inspect data structure
len(list_player) # show the total number of rows in a list
max(list_player)
min(list_player)

# read: find data
list_player[0] # show the first row
list_player[0][0] # show the first element in the first row

# update: edit data
list_player[0][3] = 'UNI' # change the value of the list
list_player[0].append('Hi I\'m here') # add a new element 

# delete:
del list_player[0][-1] # delete the value in a list

"""
Dictionary
"""
# create
dict_player = {'messi':['argentina', 30, 'striker'], 'dembele':['france', '25', 'striker']}

# read
dict_player['messi']

# update
dict_player['messi'][1] = 31

# delete
del dict_player['dembele']


"""
Tuple: cannot be changed
"""

# create
tup = ("ronaldo", "xavi", "iniesta")

# read
tup[0]
tup[1]

# update: tuple cannot be modified
tup[0] = 'messi'
tup*4

# delete
del tup[0] # not allowed
del tup # feasible
