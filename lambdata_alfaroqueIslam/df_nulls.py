def df_nulls(df,col_name):
    check_for_nan = df[col_name].isnull().values.any()
    print (check_for_nan)