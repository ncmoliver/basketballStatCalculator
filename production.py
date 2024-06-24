# Step 5: Calcula

def calculations(df):
    
    def length_of_df(df):
        length = len(df.columns)
        return length

    def production(df):
        original_len_of_df = length_of_df(df)
        df['twoMI'] = df['twoA'] - df['twoMA']
        df['twoProduction'] = df['twoMA'] - df['twoMI']
        df['threeMI'] = df['threeA'] - df['threeMA']
        df['threeProduction'] = df['threeMA'] - df['threeMI']
        df['ftMI'] = df['ftA'] - df['ftMA']
        df['ftProduction'] = df['ftMA'] - df['ftMI']
        
        if original_len_of_df + 6 == length_of_df(df):
            print('\nStep 5 Completed: Shooting production stats have been calculated.')
            return df
        else:
            print("Error adding columns")
            

    def efficiency(df):
        length = length_of_df(df)
        df['twoEfficiency'] = round(((df['twoMA'] / df['twoA'])*100), 2)
        df['threeEfficiency'] = round(((df['threeMA'] / df['threeA']) * 100),2)
        df['ftEfficiency'] = round(((df['ftMA'] / df['ftA'])* 100), 2)
        if length_of_df(df) !=  length + 3:
            print(f'Error \'production. py\': Calculating efficiency. Columns not added')
        else:
            print(f'Efficiency have been calculated successfully.\n')
            return df
        
    def effectiveness(df):
        length = length_of_df(df)
        df['teamTwoProduction'] = sum(df['twoProduction']) 
        df['teamThreeProduction'] = sum(df['threeProduction'])
        df['teamFtProduction'] = sum(df['ftProduction'])
        df['twoEffective'] = (df['twoProduction'] / df['teamTwoProduction'])*100
        df['threeEffective'] = (df['threeProduction'] / df['teamThreeProduction'])*100
        df['ftEffective'] = (df['ftProduction'] / df['teamFtProduction'])*100
        return df

    production(df)
    efficiency(df)
    effectiveness(df)

    return df