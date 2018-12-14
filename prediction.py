from joblib import  load


def random_forest(test_data):
    # import the trained model
    model = load('rf_solo1.joblib')

    # Passing the input data to the trained model
    rank = model.predict(test_data)
    rank = rank[0]
    rank = float("{0:.4f}".format(rank))
    return rank