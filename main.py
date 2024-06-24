#Collect Data, Verify, and Convert Stats
# Read csv file
from utils import *
from production import *
from effciency import *
from effectiveness import *
import pandas as pd
import matplotlib.pyplot as plt

# Set the maximum number of rows and columns to display
pd.set_option('display.max_rows', None)  # To display all rows
pd.set_option('display.max_columns', None) 
    

is_formatted = False
while is_formatted == False:
    path_to_stats = input('Please enter filepath to game/season stats: ')
    
    # Step 1. Verify file name ends with .csv
    path = verify_csv(path_to_stats)
    
    # Step 2. Turn data in csv file into panda
    # empty --> Check to see if df is empty 
    df = open_csv(path)
    
    # Step 3. Delete useless columns (2pt, 3pt, ft - Percentage | Points | Rank)
    df_update_columns = delete_columns(df)
    
    # Step 4. Split shooting stats into separate categories two_MA, 
    # twoA, threeMA, threeA, ftMA, ftA
    formatted_data = format_split_stats(df_update_columns)
    
    # Step 5: Change data types
    calculable_df = change_to_int(formatted_data) 
    
    # Production, Efficiency, Effectiveness Calculations
    df = production(calculable_df)
    df = efficient(calculable_df)
    df = effective(calculable_df)
    # Three different dataframes in new_dfs
    # Returns: twoStats, threeStats, ftStats, rebounding, aux(ast, blk, to, fouls)
    two_df = split_two_shooting(df)
    # twoDf_tolist = two_df.tolist()
    three_df = split_three_shooting(df)
    # threeDf_tolist = three_df.tolist()
    ft_df = split_ft_shooting(df)
    # ftDf_tolist = ft_df.tolist()
    category = input('Would you like a team or player analysis?\n(type \'p\' or \'t\' or anything else to exit program: )')
    match category:
        case 'p':
            print(df['Name'])
            player = int(input('Please choose a player, enter # associated: '))
            print('Name stored successfully!')
        case 't':
            print
        

    break        

else:
    print("The csv file you have enter is invalid.")
    is_formatted = True
