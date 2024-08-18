from typing import List, Tuple, Union
import numpy
import pandas as pd
from mlops.utils.data_preparation.train_val_test import train_val_test
from mlops.utils.data_preparation.scale_data import scale_data

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(data, *args, **kwargs):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    # Specify your data exporting logic here

    #split the input data into training, validation and testing
    
    X_train,X_test,X_prod_test,y_train, y_test,y_prod_test = train_val_test(data)

    #scale and normalize the input feature columns and not the target column

    X_train_scaled, X_test_scaled, X_prod_test_scaled  = scale_data(X_train,X_test,X_prod_test)
    return X_train_scaled, X_test_scaled, X_prod_test_scaled,y_train, y_test,y_prod_test

@test
def test_output(
    data1:numpy.ndarray,
    data2:numpy.ndarray,
    data3:numpy.ndarray,
    data4:pd.Series,
    data5:pd.Series,
    data6:pd.Series,
    *args,
    **kwargs ) -> None:
    """
    Template code for testing the output of the block.
    """
    # print(type(data))
    assert ((data1.min()).any() >= -2 and (data1.max()).any() <= 2 ), 'Data1 is not normalized'
    assert ((data2.min()).any() >= -2 and (data2.max()).any() <= 2 ), 'Data2 is not normalized'
    assert ((data3.min()).any() >= -2 and (data3.max()).any() <= 2 ), 'Data3 is not normalized'
    
    test_size = kwargs.get('test_size')
    val_size = kwargs.get('val_size')
    train_size = kwargs.get('train_size')
    assert (len(data1) == train_size and len(data4) == train_size)
    assert (len(data2) == val_size and len(data5) == val_size)
    assert (len(data3) == test_size and len(data6) == test_size)
