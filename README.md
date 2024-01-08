

# Cleanpy

Cleanpy is a simple data cleaning and preprocessing library created to assist data engineers and data scientists in preparing their data for analysis and machine learning. It includes basic functionality for filling missing values, normalizing data, encoding categorical variables, and handling outliers.

## Installation

Clone this repository:
```bash
git clone https://github.com/your-username/cleanpy.git
cd cleanpy
```

Install the library:
```bash
pip install .
```

## Usage

Here are some basic examples of how `cleanpy` can be used:

### Fill Missing Values
```python
import pandas as pd
import cleanpy as cp

df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6]})
df_filled = cp.fill_missing(df)
```

### Normalize Column
```python
df_normalized = cp.normalize_column(df, 'A')
```

### Encode Categorical Data
```python
df_encoded = cp.encode_categorical(df, 'B')
```

### Remove Outliers
```python
df_no_outliers = cp.remove_outliers(df, 'A')
```

### Detect Outliers
```python
df['A_outliers'] = cp.detect_outliers(df, 'A')
```

Note: Always make sure to inspect the result after applying these functions, as every dataset is unique and may require specialized handling.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes or improvements.

```
