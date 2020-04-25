from sklearn.preprocessing import LabelEncoder

def encode(df,cat):
	le = LabelEncoder()
	for i in cat:
		le.fit(df[i])
		x = le.transform(df[i])
		df[i]=x
	return df