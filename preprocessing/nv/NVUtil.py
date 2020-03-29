def nv_treatment(df,nv_threshold):
    print()
    print('Before NV treatment the stats are as below')
    print(df.isna().sum())
    null_value_exclude_filter = (df.isna().sum()/df.shape[0])*100
    selected_columns = null_value_exclude_filter[null_value_exclude_filter < nv_threshold]
    excluded_columns = null_value_exclude_filter[null_value_exclude_filter > nv_threshold]
    selected_columns = selected_columns.index
    excluded_columns = excluded_columns.index
    
    df.drop(excluded_columns,axis=1,inplace=True)
    
    #numerical_columns = df.mean().index
    # changed from mean() to describe() because , boolean values are considered as integers while using mean()
    numerical_columns = df.describe().columns.values
    categorical_columns = []

    for col in df.columns:
        if col not in numerical_columns:
            categorical_columns.append(col)
    
    for col in df.columns:
        if col in numerical_columns:
            df[col].fillna(df[col].median(),inplace=True)
        else:
            df[col].fillna(df[col].value_counts().index[0],inplace=True)
    print('Before NV treatment the stats are as below')
    print(df.isna().sum())
    return [excluded_columns,selected_columns,numerical_columns,categorical_columns,df]