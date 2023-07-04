'''
this is sample test
'''
from sdv.datasets.demo import download_demo

real_data, metadata = download_demo(
    modality='single_table',
    dataset_name='fake_hotel_guests'
)


x = real_data.head()
print(x)
