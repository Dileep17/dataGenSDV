import pandas as pd
from sdv.lite import SingleTablePreset
from sdv.metadata import SingleTableMetadata
from sdv.constraints import create_custom_constraint_class


# Load the dataset
data = pd.read_csv('/Users/dileepbellamkonda/Documents/GitHub/dataGenSDV/datagen/dataset.csv')
metadata = SingleTableMetadata()
metadata.detect_from_csv(filepath='/Users/dileepbellamkonda/Documents/GitHub/dataGenSDV/datagen/dataset.csv')
metadata.update_column(
    column_name='id',
    sdtype='id',
    regex_format='[0-9]{3}')

metadata.update_column(
    column_name='name',
    sdtype='name')

metadata.save_to_json('/Users/dileepbellamkonda/Documents/GitHub/dataGenSDV/datagen/meta.json')
# Create a SDV instance
synthesizer = SingleTablePreset(metadata, name='FAST_ML')



def is_valid(column_names, data, extra_parameter):
    validity = [True]*data.shape[0]
    return pd.Series(validity)

def transform(column_names, data, extra_parameter):
    # TODO implement your transformation logic
    # data['name'] = "testdata_" + data["name"]
    # print('************************** -- transform')
    # print(data)
    for column_name in column_names:
        if column_name in data:
            if column_name == 'name':
                data['name'] = "testdata_" + data["name"]

    transformed_data = data 
    return transformed_data

def reverse_transform(column_names, transformed_data, extra_parameter):
    # TODO implement your reverse transformation logic
    # print('************************** -- reverse_transform')
    # print(column_names)
    # print(transformed_data)
    # transformed_data['name'] = transformed_data['name'].str.replace('testdata_', '')
    # transformed_data['name'] = "testdata_" + transformed_data["name"]
    # for column_name in column_names:
    #     print('column name ' + column_name)
    #     if column_name in transformed_data:
    #         print('column name in dataframe')
    #         if column_name == 'name':
    #             print('column name is name')
    #             transformed_data['name'] = transformed_data['name'].str.replace('testdata_', '')   
    reversed_data = transformed_data
    print('-------------')
    print(transformed_data)
    print('-------------')
    # print('************************** -- after reverse_transform')
    # print(reversed_data) 
    return reversed_data

# Create your constraint class
# TODO rename your class to a descriptive name
MyCustomConstraintClass = create_custom_constraint_class(
    is_valid_fn=is_valid,
    transform_fn=transform, # optional
    reverse_transform_fn=reverse_transform # optional
)

synthesizer._synthesizer.add_custom_constraint_class(
    class_object=MyCustomConstraintClass, # your constraint class
    class_name='MyCustomConstraintClass' # the name you use to refer to it
)

my_constraint = {
    'constraint_class': 'MyCustomConstraintClass',
    'constraint_parameters': {
        'column_names': ['name'],
        'extra_parameter': None
    }
}
synthesizer.add_constraints([my_constraint])
synthesizer.

# Fit the SDV model to the dataset
synthesizer.fit(data)

# Generate synthetic data
synthetic_data = synthesizer.sample(num_rows=10)

# Output the synthetic data
synthetic_data.to_csv("/Users/dileepbellamkonda/Documents/GitHub/dataGenSDV/datagen/op.csv", index=False, sep=',', encoding='utf-8')
