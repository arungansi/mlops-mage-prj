from typing import Dict, List, Tuple, Union

from sklearn.preprocessing import StandardScaler
from xgboost import Booster

import pandas as pd

from mlops.utils.data_preparation.feature_extract import feature_extract
from mlops.utils.models.xgboost_modified import build_data

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom

DEFAULT_INPUTS = [
    {
        "Date/Time": "01 01 2018 00:30",
        "Wind Speed (m/s)": 5.659674,
        "Theoretical_Power_Curve (KWh)": 516.127569,
        "Wind Direction (°)": 271.258087 
    },
    {
        "Date/Time": "01 01 2018 00:40",
        "Wind Speed (m/s)": 5.577941,
        "Theoretical_Power_Curve (KWh)": 491.702972,
        "Wind Direction (°)": 265.674286
    }
]


@custom
def predict(
    model_settings: Booster,
    **kwargs,
) -> List[float]:
    #print(type(model_settings))
    inputs: List[Dict[str, Union[float, int]]] = kwargs.get('inputs', DEFAULT_INPUTS)
    inputs = feature_extract(pd.DataFrame(inputs))

    # DOLocationID = kwargs.get('DOLocationID')
    # PULocationID = kwargs.get('PULocationID')
    # trip_distance = kwargs.get('trip_distance')

    # if DOLocationID is not None or PULocationID is not None or trip_distance is not None:
    #     inputs = [
    #         {
    #             'DOLocationID': DOLocationID,
    #             'PULocationID': PULocationID,
    #             'trip_distance': trip_distance,
    #         },
    #     ]
    
    model = model_settings
    scale = StandardScaler()
    vectors = scale.fit_transform(inputs)

    predictions = model.predict(build_data(vectors))

    for idx, input_feature in enumerate(inputs):
        print(f'Prediction of "LV ActivePower (kW)" using these features: {predictions[idx]}')
        for key, value in inputs[idx].items():
            print(f'\t{key}: {value}')

    return predictions.tolist()
