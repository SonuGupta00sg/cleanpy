import pandas as pd
from scipy import stats
from sklearn import preprocessing
import numpy as np

def fill_missing(df, strategy='mean', columns=None):
    """
    Fill missing values in specified columns using a given strategy.
    Supported strategies: mean, median, most_frequent
    """
    if columns is None:
        columns = df.columns
    
    for column in columns:
        if df[column].isnull().any():
            if strategy == 'mean':
                fill_value = df[column].mean()
            elif strategy == 'median':
                fill_value = df[column].median()
            elif strategy == 'most_frequent':
                fill_value = df[column].mode()[0]
            else:
                raise ValueError("strategy not supported")
            df[column] = df[column].fillna(fill_value)
    return df

def normalize_column(df, column):
    """
    Normalize the data in a dataframe column using MinMaxScaler.
    """
    min_max_scaler = preprocessing.MinMaxScaler()
    df[column] = min_max_scaler.fit_transform(df[[column]])
    return df

def encode_categorical(df, column):
    """
    Convert a column of categorical data into numerical using Label Encoding.
    """
    label_encoder = preprocessing.LabelEncoder()
    df[column] = label_encoder.fit_transform(df[column])
    return df

def remove_outliers(df, column, method='z_score', threshold=3):
    """
    Remove outliers from a column based on a z_score or IQR method.
    """
    if method == 'z_score':
        df = df[(np.abs(stats.zscore(df[column])) < threshold)]
    elif method == 'iqr':
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - (1.5 * IQR)
        upper_bound = Q3 + (1.5 * IQR)
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    else:
        raise ValueError("method not supported")
    return df

def detect_outliers(df, column, method='z_score', threshold=3):
    """
    Return a boolean series with True indicating if the value is an outlier based on a z_score or IQR method.
    """
    if method == 'z_score':
        return (np.abs(stats.zscore(df[column])) > threshold)
    elif method == 'iqr':
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - (1.5 * IQR)
        upper_bound = Q3 + (1.5 * IQR)
        return ~df[column].between(lower_bound, upper_bound)
    else:
        raise ValueError("method not supported")