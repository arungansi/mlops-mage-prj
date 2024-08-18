from typing import Callable, Dict, Tuple, Union

from pandas import Series, DataFrame
from sklearn.base import BaseEstimator

from mlops.utils.models.sklearn_modified import load_class, train_model

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def train(
    settings: Tuple[
        Dict[str, Union[bool, float, int, str]],
        DataFrame,
        Series,
        Dict[str, Union[Callable[..., BaseEstimator], str]],
    ],
    **kwargs,
) -> Tuple[BaseEstimator, Dict[str, str]]:
    hyperparameters, X, y, model_info = settings
    model_class = model_info['cls']
    model = model_class(**hyperparameters)
    model.fit(X, y)

    return model, model_info
