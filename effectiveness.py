from utils import length_of_df
from statistics import mean

def effective(df):
        
        length = length_of_df(df)
        
        df['teamTwoProduction'] = sum(df['twoProduction']) 
        df['teamThreeProduction'] = sum(df['threeProduction'])
        df['teamFtProduction'] = sum(df['ftProduction'])

        df['twoEffective'] = round((df['twoProduction'] / df['teamTwoProduction'])*100, 2)
        df['threeEffective'] = round((df['threeProduction'] / df['teamThreeProduction'])*100, 2)
        df['ftEffective'] = round((df['ftProduction'] / df['teamFtProduction'])*100, 2)

        df['teamTwoEffective'] = mean(df['twoEffective'])
        df['teamThreeEffective'] = mean(df['threeEffective'])
        df['teamFtEffective'] = mean(df['ftEffective'])
       
        return df
