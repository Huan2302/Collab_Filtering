import pandas
from pandas import read_csv

def get_dataframe_views_base(text):
    r_cols = ['user_id', 'item_id', 'views']
    views = pandas.read_csv(text, sep=',', names=r_cols, encoding='utf-8')
    Y_data =views.values
    return Y_data