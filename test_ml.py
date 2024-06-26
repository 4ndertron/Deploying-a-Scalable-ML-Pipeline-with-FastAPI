import os
import pytest
import pandas as pd
from pathlib import Path
from ml.model import train_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


@pytest.fixture
def census_file() -> Path:
    return Path(__file__).parent.resolve() / 'data' / 'census.csv'


# First test
def test_train_test_split_size(census_file):
    """
    Assert that the train_test_split function slices the census data into a suitable size.
    """
    data = pd.read_csv(str(census_file))
    train, test = train_test_split(data, test_size = 0.2)
    assert len(test) >= 2000


# Second test
def test_census_column_names(census_file):
    """
    Assert that all expected columns are present in the census file.
    """
    data = pd.read_csv(census_file)

    features = {
        'age',
        'workclass',
        'fnlgt',
        'education',
        'education-num',
        'marital-status',
        'occupation',
        'relationship',
        'race',
        'sex',
        'capital-gain',
        'capital-loss',
        'hours-per-week',
        'native-country',
        'salary'
    }

    assert set(data.columns) == features


# Third test
def test_train_model_return_type():
    """
    # Check that the model is the RandomForestClassifier.
    """
    sample_x = [[0, 1, 2], [3, 4, 5]]
    sample_y = ['col1', 'col2']

    model = train_model(sample_x, sample_y)

    assert isinstance(model, RandomForestClassifier)
