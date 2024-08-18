from typing import Dict, Tuple, Union

from pandas import Series, DataFrame
from sklearn.base import BaseEstimator
from xgboost import Booster

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom


@custom
def source(
    xboost_tuned: Booster,
    settings: Tuple[
        Dict[str, Union[bool, float, int, str]],
        DataFrame,
        Series,
    ],
    **kwargs,
) -> Tuple[Booster, DataFrame, Series]:
    model = xboost_tuned
    _, X_train, y_train = settings

    return model, X_train, y_train
