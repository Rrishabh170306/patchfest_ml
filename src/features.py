import pandas as pd

def add_time_features(df):
    df['date']=pd.to_datetime(df['date'])
    df['weekday']=df['date'].dt.weekday
    df['is_weekend']=df['weekday']>=5
    df['month']=df['date'].dt.month
    df['weekofyear']=df['date'].dt.isocalendar().week
    return df

def add_lag_features(df):
    df['lag_1']=df['count'].shift(1)
    df['lag_7']=df['count'].shift(7)
    return df
