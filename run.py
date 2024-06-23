#Collect Data, Verify, and Convert Stats
'''
This is a function that takes a csv file as a parameter. 

Args: No arguments

Return: Return data in a dictionary format
'''
# Read csv file
import pandas as pd # type: ignore
import os

# Set the maximum number of rows and columns to display
pd.set_option('display.max_rows', None)  # To display all rows
pd.set_option('display.max_columns', None) 
    
    
def verify_csv(filepath):
    # Verify that user input a csv file - by verifying the last four characters
    if not os.path.exists(filepath):
        print("Error: File does not exist")
        return None    
    else:
        print("\nStep 1: Completed - csv file verified\n")
        return filepath

def open_csv(verified_path):
     # Open csv file in reader mode
    df = pd.read_csv(f'{verified_path}') 
    return df
# Step 2
def delete_columns(df):
    drop_columns = ['PTS', 'RNK','2PER', '3PER', 'FTPER']
    dropped_columns = df.drop(drop_columns, axis=1)
    if df.shape != dropped_columns.shape:
        print(f"\nStep 2 Completed - Columns have been dropped successfully.\nDropped Columns: {drop_columns}\n")
        return dropped_columns
    else:
        print("Error: A columns was not dropped properly.\nPlease be screenshot and notify admin immediate.")
# Step 3: Split Stats
def format_split_stats(df):
    old_len = len(df.columns)
    df[['twoMA', 'twoA']] = df['FGM-A'].str.split('-', expand=True)
    df[(['threeMA', 'threeA'])] = df['3PM-A'].str.split('-', expand=True)
    df[['ftMA', 'ftA']] = df['FTM-A'].str.split('-', expand=True)
    df = df.drop(['FGM-A', '3PM-A','FTM-A'], axis=1)
    new_len = len(df.columns)
    if old_len < new_len:
        print("Step 3: Split Successful!\nNew Columns: twoMA twoa threeMA threeA ftMA ftA")
        return df
    else:
        print("Step 3 Error: error in split 'length of columns'")
            

#Step 4: Change to int
def change_to_int(df):
    ''' 
    Goal of this function is to change the following columns datatype to int:
        twoMA twoA threeMA threeA ftMA ftA
    '''
    convert_dict = {'Name': str,
                    'twoMA': int,
                    'twoA': int,
                    'threeMA': int,
                    'threeA': int,
                    'ftMA': int,
                    'ftA': int}
    df = df.astype(convert_dict)
    for type in df.dtypes:
        if type == 'object':
            print(f'Error: All categories have not been converted to int. ')
        else:
            print(f'\nStep 4 Completed: The following columns have been updated\nUpdated Columns:')
            for keys, values in convert_dict.items():
                print('-' + keys)
            return df

# Step 5: Calculate Stats

# Production
def production(df):
    original_len_of_df = len(df.columns)
    df['twoMI'] = df['twoA'] - df['twoMA']
    df['twoProduction'] = df['twoMA'] - df['twoMI']
    df['threeMI'] = df['threeA'] - df['threeMA']
    df['threeProduction'] = df['threeMA'] - df['threeMI']
    df['ftMI'] = df['ftA'] - df['ftMA']
    df['ftProduction'] = df['ftMA'] - df['ftMI']
    
    if original_len_of_df < len(df.columns):
        print('Step 5 Completed: Shooting production stats have been calculated.')
        return df
    else:
        print("Error adding columns")
# Efficiency

# Effectiveness
    production
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
    # Step 4. Split shooting stats into separate categories two_MA, twoA, threeMA, threeA, ftMA, ftA
    formatted_data = format_split_stats(df_update_columns)
        # Step 5: Change data typees
    calculable_df = change_to_int(formatted_data) 
    production(calculable_df)
    
    break
        #Formatting data function
        # split the Name column into two columns using pd.Series.str.split()
        # df[['First Name', 'Last Name']] = df['Name'].str.split(' ', expand=True)
        
            

else:
    print("The csv file you have enter is invald.")
    is_formatted = True



# Format data

# Creat a empty dictionary

# Add data to dictionary

# Balance: Calculate team stats

# Add team stats to Stats dictionary