#Collect Data, Verify, and Convert Stats
# Read csv file
from utils import *
from production import *
from effciency import *
from effectiveness import *
import pandas as pd

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


    print(df)
    break        

else:
    print("The csv file you have enter is invald.")
    is_formatted = True
