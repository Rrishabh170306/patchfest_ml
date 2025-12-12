from xgboost import XGBRegressor

def train_xgb(X,y):
    model=XGBRegressor()
    model.fit(X,y)
    return model
