from sklearn.preprocessing import LabelEncoder

def encode(df,cat):
	le = LabelEncoder()
	for i in cat:
		le.fit(df[i])
		x = le.transform(df[i])
		df[i]=x
	return df

def encode_train_test(df_train,df_test,cat):
	le = LabelEncoder()
	for i in cat:
		le.fit(df_train[i])
		x1 = le.transform(df_train[i])
		x2 = le.transform(df_test[i])
		df_train[i]=x1
		df_test[i]=x2
	return [df_train,df_test]