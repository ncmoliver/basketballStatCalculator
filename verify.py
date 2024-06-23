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