import pandas as pd
from sdv.lite import SingleTablePreset
from sdv.metadata import SingleTableMetadata

users_file = './input_data/users.csv'

# Load the dataset
data = pd.read_csv(users_file)

# detect and update metadata
metadata = SingleTableMetadata()
metadata.detect_from_csv(filepath = users_file)
metadata.update_column(
    column_name='id',
    sdtype='id',
    regex_format='[0-9]{3}')

metadata.update_column(
    column_name='name',
    sdtype='name')

# Create a SDV instance
synthesizer = SingleTablePreset(metadata, name='FAST_ML')

# Fit the SDV model to the dataset
synthesizer.fit(data)

# Generate synthetic data
synthetic_data = synthesizer.sample(num_rows=10)

# Apply Transformation on DataFrame (not SDV)
synthetic_data['name'] = 'testdata ' + synthetic_data['name']

# Output the synthetic data
synthetic_data.to_csv("./output/op.csv", index=False, sep=',', encoding='utf-8')
