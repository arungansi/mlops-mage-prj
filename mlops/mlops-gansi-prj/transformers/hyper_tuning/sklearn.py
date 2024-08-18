from typing import Callable, Dict, Tuple, Union

from pandas import Series, DataFrame
from sklearn.base import BaseEstimator

from mlops.utils.logging import track_experiment
from mlops.utils.models.sklearn_modified import load_class, tune_hyperparameters

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def hyperparameter_tuning(
    get_prepared_data: Dict[str, Union[Series, DataFrame]],
    model_class_name: str,
    *args,
    **kwargs,
) -> Tuple[
    Dict[str, Union[bool, float, int, str]],
    DataFrame,
    Series,
    Callable[..., BaseEstimator],
]:
    X_train, X_val, _, y_train, y_val, _ = get_prepared_data['build_data_for_ml']

    model_class = load_class(model_class_name)

    hyperparameters = tune_hyperparameters(
        model_class,
        X_train=X_train,
        y_train=y_train,
        X_val=X_val,
        y_val=y_val,
        callback=lambda **opts: track_experiment(**{**opts, **kwargs}),
        max_evaluations=kwargs.get('max_evaluations'),
        random_state=kwargs.get('random_state'),
    )

    return hyperparameters, X_train, y_train, dict(cls=model_class, name=model_class_name)
