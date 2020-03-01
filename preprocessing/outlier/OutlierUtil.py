import numpy as np
def iqr_outlier_treatment(df,numerical_columns):
	print()
	print('Before iqr outler treatment the stats are as below')
	print(df.describe())
	for col in df.columns:
		if col in numerical_columns:
			q1 = np.quantile(df[col].values,0.25)
			q3 = np.quantile(df[col].values,0.75)
			iqr = q3 - q1
			ltv = q1 - (1.5 * iqr)
			utv = q3 + (1.5 * iqr)
			fillval = []
			for val in df[col].values:
				if (val < ltv) or (val > utv):
					fillval.append(df[col].median())
				else:
					fillval.append(val)
			df[col] = fillval
	print('After iqr outler treatment the stats are as below')
	print(df.describe())
	return df