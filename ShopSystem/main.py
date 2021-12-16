import read_data_func
import collab_filtering

if __name__ == '__main__':
    data_matrix = read_data_func.get_dataframe_views_base('CF.csv')
    cf_rs = collab_filtering.CF(data_matrix, k=2, uuCF=1)
    cf_rs.fit()
    print(cf_rs.recommend_top(3, top_x=2))
