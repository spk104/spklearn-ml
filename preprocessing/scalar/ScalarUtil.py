from sklearn.preprocessing import MinMaxScaler

def min_max_scalar(df,numerical_columns):
	print()
	print('Before MinMax treatment the stats are as below')
	print(df.describe())
	for col in df.columns:
		if col in numerical_columns:
			mms = MinMaxScaler()
			mms.fit(df[[col]])
			x = mms.transform(df[[col]])
			df[col] = x
	print('After MinMax treatment the stats are as below')
	print(df.describe())
	return df