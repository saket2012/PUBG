import numpy as np
import pandas as pd

def import_data(file, is_train):
    if is_train:
        # Import training data set
        data_frame = pd.read_csv("training_data.csv", low_memory = False)

    else:
        # Passing the input file for prediction
        data_frame = pd.read_csv(file)
    return data_frame


# feature_engineering function will process the training dataset. Processing includes
# creating new features form existing ones, finding missing values, dropping unnecessary
# columns from the dataset.
def feature_engineering(data_frame, is_train):
    data_frame = data_frame.loc[data_frame['matchType'] == 'solo']
    # Adding all travelling distances and created new feature
    data_frame['totalDistance'] = data_frame['rideDistance'] + data_frame["walkDistance"] + \
                                  data_frame["swimDistance"]

    # Dropping the unnecessary features from the dataset
    data_frame.drop(
        ["Id", "matchId", "groupId", "matchType", "rideDistance", "walkDistance", "swimDistance", "vehicleDestroys"],
        axis = 1, inplace = True)

    target_feature = 'winPlacePerc'

    y = None
    if is_train:
        y = np.array(data_frame[target_feature], dtype = np.float64)
        data_frame.drop(["winPlacePerc"], axis = 1, inplace = True)
    X = np.array(data_frame, dtype = np.float64)
    return X, y
