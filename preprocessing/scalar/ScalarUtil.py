from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

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
	
def standard_scalar(df,numerical_columns):
	print()
	print('Before StandardScaler treatment the stats are as below')
	print(df.describe())
	for col in df.columns:
		if col in numerical_columns:
			mms = StandardScaler()
			mms.fit(df[[col]])
			x = mms.transform(df[[col]])
			df[col] = x
	print('After StandardScaler treatment the stats are as below')
	print(df.describe())
	return df