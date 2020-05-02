from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import numpy as np
import pandas as pd

algorithm = []
total_features = []
total_features_names = []
additional_infos = []
r2_scores = []
mae_score = []
mse_score = []
rmse_score = []
log_rmse_score = []

def performance_metrics(model,features, additional_info, y_true, y_pred):
	score = r2_score(y_true,y_pred)
	mae = mean_absolute_error(y_true,y_pred)
	mse = mean_squared_error(y_true,y_pred)
	rmse = np.sqrt(mse)
	log_rmse = np.sqrt(mean_squared_error(np.log(y_true),np.log(y_pred)))

	algorithm.append(str(model))
	total_features.append(len(features))
	total_features_names.append(str(features))
	additional_infos.append(additional_info)
	r2_scores.append(score)
	mae_score.append(mae)
	mse_score.append(mse)
	rmse_score.append(rmse)
	log_rmse_score.append(log_rmse)

	metrics_df = pd.DataFrame(data = [algorithm,total_features,total_features_names,additional_infos,r2_scores,mae_score,mse_score,rmse_score,log_rmse_score])
	metrics_df = metrics_df.T
	metrics_df.columns = ['algorithm','feature_count','features_names','additional_info','r2_score','mae_score','mse_score','rmse_score','log_rmse_score']
	return metrics_df