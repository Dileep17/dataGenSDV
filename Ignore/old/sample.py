import pandas as pd

# Create a sample DataFrame
data = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['testdata_John', 'testdata_Jane', 'testdata_Mark'],
    'class': ['A', 'B', 'C']
})

# Remove the prefix from the name column
data['name'] = data['name'].str.replace('testdata_', '')

# Output the modified DataFrame
print(data)