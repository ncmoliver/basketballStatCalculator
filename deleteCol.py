

# Step 2
def delete_columns(df):
    drop_columns = ['PTS', 'RNK','2PER', '3PER', 'FTPER']
    dropped_columns = df.drop(drop_columns, axis=1)
    if df.shape != dropped_columns.shape:
        print(f"\nStep 2 Completed - Columns have been dropped successfully.\nDropped Columns: {drop_columns}\n")
        return dropped_columns
    else:
        print("Error 'deleteCol.py': A columns was not dropped properly.\nPlease be screenshot and notify admin immediate.")