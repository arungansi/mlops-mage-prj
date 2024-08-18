import pickle
from flask import Flask, request, jsonify
from typing import Dict, List, Tuple, Union
from sklearn.preprocessing import StandardScaler
from xgboost import Booster
import pandas as pd
from pandas import DataFrame, Series

from mlops.utils.data_preparation.feature_extract import feature_extract
from mlops.utils.models.xgboost_modified import build_data

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom


@custom
def predict(
    data_2: Booster,
    **kwargs,
) -> List[float]:


app = Flask('duration-prediction')


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride = request.get_json()

    features = prepare_features(ride)
    pred = predict(features)

    result = {
        'duration': pred
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
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
