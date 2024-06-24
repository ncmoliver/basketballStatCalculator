# Step 5: Calculations

def production(df):
    df['twoMI'] = df['twoA'] - df['twoMA']
    df['twoProduction'] = df['twoMA'] - df['twoMI']
    df['threeMI'] = df['threeA'] - df['threeMA']
    df['threeProduction'] = df['threeMA'] - df['threeMI']
    df['ftMI'] = df['ftA'] - df['ftMA']
    df['ftProduction'] = df['ftMA'] - df['ftMI']
    

    return df
    




#   # Split dataframe into the following sections:
#     '''
#     pTwoShooting = [ Name, twoMA, twoMI, twoA, twoProduction, twoEfficiency, twoEffective, teamTwoEffective  ]
#     '''
#     # df_subset = df[['column1', 'column2']]
#     pTwoShooting = df[['Name', 'twoMA', 'twoMI', 'twoA', 'twoProduction', 'twoEfficiency', 'twoEffective', 'teamTwoEffective']]
