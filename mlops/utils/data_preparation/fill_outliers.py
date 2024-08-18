import pandas as pd


def fill_outliers(
    df: pd.DataFrame,
) -> pd.DataFrame:

    #filling negavtive values with the mean value for LV ActivePower (kW) as negative values are outliers
    df.loc[df['LV ActivePower (kW)'] < 0, 'LV ActivePower (kW)'] = df[df.columns[1]].mean()

    return df