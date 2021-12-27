import pandas
from pandas import read_csv

def get_dataframe_views_base(text):
    r_cols = ['id', 'user_id', 'item_id', 'views']
    views = pandas.read_csv(text, sep=',', names=r_cols, encoding='utf-8')
    views = views.drop('id', 1)
    Y_data =views.values
    return Y_data