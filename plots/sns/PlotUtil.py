import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def draw_distribution_plot(rows,columns,df,figsize = (16,8),selected_features=None):
	fig, ax = plt.subplots(nrows = rows, ncols = columns, figsize = figsize)
	if selected_features is not None:
		features = selected_features
	else:
		features = df.columns

	index = 0
	for i in range(rows):
		for j in range(columns):
			_ = sns.distplot(df[features[index]], ax = ax[i][j])
			index = index + 1
			if index == len(features):
				break	

	plt.tight_layout()


def draw_scatter_plot(rows,columns,df,target_variable,figsize = (16,8),selected_features=None):
	fig, ax = plt.subplots(nrows = rows, ncols = columns, figsize = figsize)
	if selected_features is not None:
		features = selected_features
	else:
		features = df.columns
	
	index = 0

	for i in range(rows):
		for j in range(columns):
			if index == len(features):
				break
			_ = sns.scatterplot(x = features[index], y = target_variable,data=df, ax = ax[i][j])
			index = index + 1

	plt.tight_layout()

def draw_correlation_heatmap(df,figsize = (40,40)):
	fig, ax = plt.subplots(figsize = figsize)
	sns.heatmap(df.corr(), annot = True, annot_kws = {'size':12},cmap='viridis')
	bottom, top = ax.get_ylim()
	ax.set_ylim(bottom + 0.5, top - 0.5)
	
	plt.tight_layout()