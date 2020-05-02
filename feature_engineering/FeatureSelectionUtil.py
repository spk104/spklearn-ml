from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import pandas as pd

def correlated_features(df,target_variable,threshold):
	features = []
	value = []
	corrdata = df.corr()[target_variable]
	for i, index in enumerate(corrdata.index):
		if index == target_variable:
			continue
		if abs(corrdata[index]) > threshold:
			features.append(index)
			value.append(corrdata[index])

	df = pd.DataFrame(data = value, index = features, columns=['Correlation Values'])
	return df