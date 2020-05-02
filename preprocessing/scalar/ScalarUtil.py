from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

def min_max_scalar(df,numerical_columns,skip_columns):
	print()
	print('Before MinMax treatment the stats are as below')
	print(df.describe())
	for col in df.columns:
		if col in skip_columns:
			continue
		if col in numerical_columns:
			mms = MinMaxScaler()
			mms.fit(df[[col]])
			x = mms.transform(df[[col]])
			df[col] = x
	print('After MinMax treatment the stats are as below')
	print(df.describe())
	return df
	
def standard_scalar(df,numerical_columns,skip_columns):
	print()
	print('Before StandardScaler treatment the stats are as below')
	print(df.describe())
	for col in df.columns:
		if col in skip_columns:
			continue
		if col in numerical_columns:
			mms = StandardScaler()
			mms.fit(df[[col]])
			x = mms.transform(df[[col]])
			df[col] = x
	print('After StandardScaler treatment the stats are as below')
	print(df.describe())
	return df

def min_max_scalar_train_test(train_df,test_df,numerical_columns,skip_columns):
	for col in train_df.columns:
		if col in skip_columns:
			continue
		if col in numerical_columns:
			mms = MinMaxScaler()
			mms.fit(train_df[[col]])
			x1 = mms.transform(train_df[[col]])
			x2 = mms.transform(test_df[[col]])
			train_df[col] = x1
			test_df[col] = x2
	return [train_df,test_df]
	
def standard_scalar_train_test(train_df,test_df,numerical_columns,skip_columns):
	for col in train_df.columns:
		if col in skip_columns:
			continue
		if col in numerical_columns:
			mms = StandardScaler()
			mms.fit(train_df[[col]])
			x1 = mms.transform(train_df[[col]])
			x2 = mms.transform(test_df[[col]])
			train_df[col] = x1
			test_df[col] = x2
	return [train_df,test_df]