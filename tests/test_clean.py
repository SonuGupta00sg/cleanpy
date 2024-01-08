import pytest
import pandas as pd
import numpy as np
from cleanpy import clean

@pytest.fixture
def sample_dataframe():
    return pd.DataFrame({
        'A': [1, 2, np.nan, 4],
        'B': [4, np.nan, 6, 6],
    })

def test_fill_missing(sample_dataframe):
    result = clean.fill_missing(sample_dataframe.copy(), strategy='mean')
    assert not result.isnull().values.any()

def test_normalize_column(sample_dataframe):
    result = clean.normalize_column(sample_dataframe.copy(), 'A')
    assert result['A'].min() == 0 and result['A'].max() == 1

def test_encode_categorical(sample_dataframe):
    result = clean.encode_categorical(sample_dataframe.copy(), 'B')
    assert result['B'].dtype == 'int32' or result['B'].dtype == 'int64'

def test_remove_outliers_z_score(sample_dataframe):
    # Add a known outlier
    sample_dataframe.loc[4] = [100, 100]
    result = clean.remove_outliers(sample_dataframe.copy(), 'A', method='z_score')
    assert 100 not in result['A'].values

def test_detect_outliers_iqr(sample_dataframe):
    # Add a known outlier
    sample_dataframe.loc[4] = [100, 100]
    outliers = clean.detect_outliers(sample_dataframe.copy(), 'A', method='iqr')
    assert outliers[4] == True