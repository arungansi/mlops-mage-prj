from typing import Dict, List, Tuple, Union

from sklearn.preprocessing import StandardScaler
from xgboost import Booster

import pandas as pd
from pandas import DataFrame, Series

from mlops.utils.data_preparation.feature_extract import feature_extract
from mlops.utils.models.xgboost_modified import build_data

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom

# DEFAULT_INPUTS = [
#     {
#         "Date/Time": "01 01 2018 00:30",
#         "Wind Speed (m/s)": 5.659674,
#         "Theoretical_Power_Curve (KWh)": 516.127569,
#         "Wind Direction (°)": 271.258087
#     },
#     {
#         "Date/Time": "01 01 2018 00:40",
#         "Wind Speed (m/s)": 5.577941,
#         "Theoretical_Power_Curve (KWh)": 491.702972,
#         "Wind Direction (°)": 265.674286
#     }
# ]


@custom
def predict(
    data_2: Booster,
    **kwargs,
) -> List[float]:
    inputs: DataFrame = pd.DataFrame(kwargs.get('inputs'))

    col1 = kwargs.get('Date/Time')
    col2 = kwargs.get('Wind Speed')
    col3 = kwargs.get('Theory Power Curve')
    col4 = kwargs.get('Wind Dir')

    # print(col1,col2,col3,col4)

    if col1 is not None or col2 is not None or col3 is not None or col4 is not None:
        # print('inside')
        inputs = [
            {
                'Date/Time': col1,
                'Wind Speed (m/s)': col2,
                'Theoretical_Power_Curve (KWh)': col3,
                'Wind Direction (°)': col4
            },
        ]

    inputs = feature_extract(pd.DataFrame(inputs))
    
    scale = StandardScaler()
    inputs = pd.DataFrame(scale.fit_transform(inputs))

    model = data_2['xboost_tuned'][0]
    # exit()
    predictions = model.predict(build_data(inputs))
    
    for idx, input_feature in enumerate(predictions):
        print(f'Prediction of "LV ActivePower (kW)" using these features: {predictions[idx]}')
        # for key, value in inputs[idx].items():
        #     print(f'\t{key}: {value}')

    return predictions.tolist()
