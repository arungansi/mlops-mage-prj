import pandas as pd


def feature_extract(
    df: pd.DataFrame,
) -> pd.DataFrame:
    #converting the date column object type from object to Datetime in order to extract components
    df['Date/Time'] = pd.to_datetime(df['Date/Time'], format='%d %m %Y %H:%M')
    
    #add more feature columns based on datetime components split    
    df['Month'] = df['Date/Time'].dt.month
    df['week'] = df['Date/Time'].dt.isocalendar().week
    df['day'] = df['Date/Time'].dt.day
    df['Hour']=df['Date/Time'].dt.hour

    #drop datetime column since we have extracted the components of it
    df.drop(columns=['Date/Time'], inplace=True)

    return df