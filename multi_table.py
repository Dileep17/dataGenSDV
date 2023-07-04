import pandas as pd
from sdv.multi_table import HMASynthesizer
from sdv.metadata import MultiTableMetadata

users_file = './input_data/users.csv'
company_file = './input_data/company.csv'

# Load the dataset
users_data = pd.read_csv(users_file)
company_data = pd.read_csv(company_file)

# Metadata
metadata = MultiTableMetadata()
metadata.detect_table_from_dataframe(table_name='users',data=users_data)
metadata.detect_table_from_dataframe(table_name='company',data=company_data)

# update metadata
metadata.update_column(table_name='users',column_name='id',sdtype='id',regex_format='[0-9]{3}')
metadata.update_column(table_name='users',column_name='name',sdtype='first_name')
metadata.update_column(table_name='users',column_name='companyId',sdtype='id')
metadata.set_primary_key(table_name='users',column_name='id')

metadata.update_column(table_name='company',column_name='id',sdtype='id',regex_format='[0-9]{3}')
metadata.update_column(table_name='company',column_name='name',sdtype='company')
metadata.update_column(table_name='company',column_name='address',sdtype='address')
metadata.set_primary_key(table_name='company',column_name='id')

metadata.add_relationship(parent_table_name='company',child_table_name='users',parent_primary_key='id',child_foreign_key='companyId')

# load metadata
synthesizer = HMASynthesizer(metadata, locales=['en_US'])

# create dictonary of data with multiple dataframes
data = {
    'users': users_data,
    'company': company_data
}

# learn from data
synthesizer.fit(data)

# create data
synthetic_data = synthesizer.sample(scale=2)

synthetic_user_data = synthetic_data.get('users')
synthetic_company_data = synthetic_data.get('company')

synthetic_user_data['name'] = "testdata " + synthetic_user_data['name']
synthetic_company_data['name'] = "testdata " + synthetic_company_data['name']

# Write data to files
synthetic_user_data.to_csv("./output/users_op.csv", index=False, sep=',', encoding='utf-8')
synthetic_company_data.to_csv("./output/company_op.csv", index=False, sep=',', encoding='utf-8')
