from sklearn.model_selection import train_test_split
from mlops.utils.data_preparation.feature_extract import feature_extract
from mlops.utils.data_preparation.fill_outliers import fill_outliers



if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    
    #extract date and time features from datetime column and add them as seperate features
    data = feature_extract(data)

    #fill negavtive values in the Target column "LV ActivePower (kW)" with the mean value of the dataset
    data = fill_outliers(data)

    return data

@test
def test_output(data, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert data is not None, 'The output is undefined'

    assert data['LV ActivePower (kW)'].min() >= 0, 'Negavtive values not alolowed'