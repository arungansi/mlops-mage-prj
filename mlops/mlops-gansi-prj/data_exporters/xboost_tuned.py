from typing import Dict, Tuple, Union

from pandas import Series, DataFrame
from xgboost import Booster

from mlops.utils.models.xgboost_modified import build_data, fit_model

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def train(
#    get_prepared_data: Dict[str, Union[Series, DataFrame]],
    settings: Tuple[
        Dict[str, Union[bool, float, int, str]],
        DataFrame,
        Series
    ],
    **kwargs,
) -> Booster:
    hyperparameters, X, y = settings

    # Test training a model with low max depth
    # so that the output renders a reasonably sized plot tree.
    if kwargs.get('max_depth'):
        hyperparameters['max_depth'] = int(kwargs.get('max_depth'))

    model = fit_model(
        build_data(X, y),
        hyperparameters,
        verbose_eval=kwargs.get('verbose_eval')
    )
    print(type(model))
    return model
