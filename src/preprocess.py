import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os

def fill_missing(df):
    for col in df.columns:
        if df[col].dtype!='object':
            df[col]=df[col].fillna(df[col].median())
        else:
            df[col]=df[col].fillna(df[col].mode()[0])
    return df

def normalize(df, cols):
    scaler=MinMaxScaler()
    df[cols]=scaler.fit_transform(df[cols])
    return df, scaler

def detect_duplicates(df, fields=['movie_name', 'date', 'time', 'seat', 'screen'], save_path='reports/duplicates.csv'):
    """
    Identify duplicate tickets using multi-field matching.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Input dataframe containing ticket data
    fields : list
        List of fields to use for duplicate detection
        Default: ['movie_name', 'date', 'time', 'seat', 'screen']
    save_path : str
        Path to save duplicate records
        Default: 'reports/duplicates.csv'
    
    Returns:
    --------
    pandas.DataFrame
        DataFrame containing all duplicate records (keeps all copies)
    """
    # Identify duplicates based on specified fields
    # Keep all duplicates (including first occurrence) using keep=False
    dup_mask = df.duplicated(subset=fields, keep=False)
    duplicates = df[dup_mask]
    
    # Count number of duplicates
    num_duplicates = len(duplicates)
    
    # Print duplicate statistics
    print(f"Number of duplicate records detected: {num_duplicates}")
    
    if num_duplicates > 0:
        # Create reports directory if it doesn't exist
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # Save duplicates to CSV
        duplicates.to_csv(save_path, index=False)
        print(f"Duplicates saved to: {save_path}")
        
        # Print additional statistics
        num_duplicate_groups = duplicates.groupby(fields).ngroup().nunique()
        print(f"Number of unique duplicate groups: {num_duplicate_groups}")
    else:
        print("No duplicates found.")
    
    return duplicates
