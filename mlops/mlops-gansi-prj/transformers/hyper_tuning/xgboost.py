from typing import Dict, Tuple, Union

import numpy as np
import xgboost as xgb
from pandas import Series, DataFrame

from mlops.utils.logging import track_experiment
from mlops.utils.models.xgboost_modified import build_data, tune_hyperparameters

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def hyperparameter_tuning(
    get_prepared_data: Dict[str, Union[Series, DataFrame]],
    **kwargs,
) -> Tuple[
    Dict[str, Union[bool, float, int, str]],
    DataFrame,
    Series,
]:
    X_train, X_val, _, y_train, y_val, _ = get_prepared_data['build_data_for_ml']

    training = build_data(X_train, y_train)
    validation = build_data(X_val, y_val)

    best_hyperparameters = tune_hyperparameters(
        training,
        validation,
        callback=lambda **opts: track_experiment(**{**opts, **kwargs}),
        max_evaluations=kwargs.get('max_evaluations'),
        random_state=kwargs.get('random_state'),
        early_stopping_rounds=kwargs.get('early_stopping_rounds')
#        **kwargs, # if you use this line then you dont need the above 3 lines as **kwargs will get all the variable settings from global
    )

    return best_hyperparameters, X_train, y_train
