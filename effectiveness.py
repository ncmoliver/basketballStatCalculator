from utils import length_of_df
from statistics import mean

def effective(df):
        
        length = length_of_df(df)
        
        df['teamTwoProduction'] = sum(df['twoProduction']) 
        df['teamThreeProduction'] = sum(df['threeProduction'])
        df['teamFtProduction'] = sum(df['ftProduction'])
        df['twoEffective'] = (df['twoProduction'] / df['teamTwoProduction'])*100
        df['teamTwoEffective'] = mean(df['twoEffective'])
        df['threeEffective'] = (df['threeProduction'] / df['teamThreeProduction'])*100
        df['teamThreeEffective'] = mean(df['threeEffective'])
        df['ftEffective'] = (df['ftProduction'] / df['teamFtProduction'])*100
        df['teamFtEffective'] = mean(df['ftEffective'])
       
        return df
