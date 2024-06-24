from utils import length_of_df

def efficient(df):
        length = length_of_df(df)
        df['twoEfficiency'] = round(((df['twoMA'] / df['twoA'])*100), 2)
        df['threeEfficiency'] = round(((df['threeMA'] / df['threeA']) * 100),2)
        df['ftEfficiency'] = round(((df['ftMA'] / df['ftA'])* 100), 2)
        if length_of_df(df) !=  length + 3:
            print(f'Error \'production. py\': Calculating efficiency. Columns not added')
        else:
            print(f'Efficiency have been calculated successfully.\n')
            return df