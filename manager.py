from dataset import import_data, feature_engineering
from prediction import random_forest
from model import rf_model_solo

def model_training():
    dataset = import_data(None, True)
    x_train, y = feature_engineering(dataset, True)
    model = rf_model_solo(x_train, y)
    print(model)

def ramdon_forest_solo(file):
    dataset = import_data(file, False)
    df, _ = feature_engineering(dataset, False)
    ans = random_forest(df)
    return ans
