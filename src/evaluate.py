from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import json

def evaluate(y_true, y_pred, save_path):
    metrics={
        "rmse": mean_squared_error(y_true,y_pred)**0.5,
        "mae": mean_absolute_error(y_true,y_pred),
        "r2": r2_score(y_true,y_pred)
    }
    with open(save_path,'w') as f:
        json.dump(metrics,f,indent=4)
    return metrics
