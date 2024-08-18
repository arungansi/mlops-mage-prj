from typing import Tuple, Union
from sklearn.model_selection import train_test_split
from pandas import DataFrame, Series


def train_val_test(
    df: DataFrame,
) -> Union[Tuple[DataFrame, DataFrame, DataFrame, Series, Series, Series]]:


    #split the data into Training and Validation
    df_train, df_val = train_test_split(df, test_size=0.3, random_state=42)

    #split the Validation data into Training Validation and Production Validation
    df_test, df_prod_test = train_test_split(df_val, test_size=0.4, random_state=42)

    #breaking the features in learning based on features and target feature
    columns = ['LV ActivePower (kW)', 'Wind Speed (m/s)', 'Theoretical_Power_Curve (KWh)','Wind Direction (°)']

    # Define the features (X) and the target (y)
    X_train = df_train.drop(columns='LV ActivePower (kW)')
    y_train = df_train['LV ActivePower (kW)']
    X_test = df_test.drop(columns='LV ActivePower (kW)')
    y_test = df_test['LV ActivePower (kW)']
    X_prod_test = df_prod_test.drop(columns='LV ActivePower (kW)')
    y_prod_test = df_prod_test['LV ActivePower (kW)']

    return X_train,X_test,X_prod_test,y_train, y_test,y_prod_test