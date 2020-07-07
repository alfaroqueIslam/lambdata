import pandas as pd
def list_to_series(lst,df,col_name):
    lst = pd.Series(lst)
    df[col_name] = lst
    return df


