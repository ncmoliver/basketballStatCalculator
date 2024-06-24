import pandas as pd
import os

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

# Step 2
def delete_columns(df):
    drop_columns = ['PTS', 'RNK','2PER', '3PER', 'FTPER']
    dropped_columns = df.drop(drop_columns, axis=1)
    if df.shape != dropped_columns.shape:
        print(f"\nStep 2 Completed - Columns have been dropped successfully.\nDropped Columns: {drop_columns}\n")
        return dropped_columns
    else:
        print("Error 'deleteCol.py': A columns was not dropped properly.\nPlease be screenshot and notify admin immediate.")

# Step 3: Split Stats
def format_split_stats(df):
    old_len = length_of_df(df)
    df[['twoMA', 'twoA']] = df['FGM-A'].str.split('-', expand=True)
    df[(['threeMA', 'threeA'])] = df['3PM-A'].str.split('-', expand=True)
    df[['ftMA', 'ftA']] = df['FTM-A'].str.split('-', expand=True)
    df = df.drop(['FGM-A', '3PM-A','FTM-A'], axis=1)
    new_len = length_of_df(df)
    if old_len < new_len:
        print("Step 3: Split Successful!\nNew Columns: twoMA twoa threeMA threeA ftMA ftA")
        return df
    else:
        print('Step 3 Error \'splitStats.py\': error in split length of columns')

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

# Returns: Length of columns in dataframe 
def length_of_df(df):
        length = len(df.columns)
        return length

# Split dataframes into twoShooting, threeShooting, ftShooting, rebounds, aux
def twoShooting_df(df):
    twoShooting = df[['twoProduction', 'column2']]