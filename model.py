import warnings
from sklearn.ensemble import RandomForestRegressor
from joblib import dump


warnings.filterwarnings("ignore", category = DeprecationWarning)


def rf_model_solo(training_data, y):
    print("Training the model")
    model = RandomForestRegressor(n_estimators = 100, min_samples_leaf = 2, min_samples_split = 3, max_features = 0.5,
                                  n_jobs = -1)
    model.fit(training_data, y)
    dump(model, 'rf_solo1.joblib')
    print("Model training done")
    return model

