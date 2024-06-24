from utils import length_of_df

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
        