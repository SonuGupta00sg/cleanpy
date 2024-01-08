import pandas as pd
from cleanpy import (
    fill_missing,
    normalize_column,
    encode_categorical,
    remove_outliers,
    detect_outliers
)

# Sample DataFrame with some missing values, categorical data, and a potential outlier
df = pd.DataFrame({
    'A': [1, 2, None, 4, 100],
    'B': ['red', 'blue', 'red', None, 'green']
})

print("Original DataFrame:")
print(df)

df = fill_missing(df, strategy='mean', columns=['A'])
print("\nDataFrame after filling missing values:")
print(df)

df = normalize_column(df, 'A')
print("\nDataFrame after normalization:")
print(df)

df = encode_categorical(df, 'B')
print("\nDataFrame after encoding categorical values:")
print(df)

df = remove_outliers(df, 'A', method='z_score', threshold=2)
print("\nDataFrame after removing outliers:")
print(df)

outliers = detect_outliers(df, 'A', method='z_score', threshold=2)
print("\nDetected Outliers:")
print(outliers)