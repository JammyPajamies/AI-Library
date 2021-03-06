import math
import warnings
import pandas as pd
import numpy as np


def mse(predicted_values, known_values):
    # Check for correct datatype, fix if incorrect.
    if isinstance(known_values, pd.DataFrame):
        known_values = np.reshape(np.array(known_values), -1)
    # MSE: (SUM((y_n - y_n_pred)^2))/n_samples
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        return ((predicted_values - known_values) ** 2).mean() if ((predicted_values - known_values) ** 2).mean() > 0 else 0.0


def rmse(predicted_values, known_values):
    # Check for correct datatype, fix if incorrect.
    if isinstance(known_values, pd.DataFrame):
        known_values = np.reshape(np.array(known_values), -1)
    # RMSE: sqrt((SUM((y_n - y_n_pred)^2))/n_samples)
    return math.sqrt(mse(predicted_values, known_values))


def rsq(predicted_values, known_values):
    # Check for correct datatype, fix if incorrect.
    if isinstance(known_values, pd.DataFrame):
        known_values = np.reshape(np.array(known_values), -1)
    # Calculate and return the calculated r^2 score.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        return 1 - (mse(predicted_values, known_values) / ((known_values - known_values.mean()) ** 2).mean()) if \
            1 - (mse(predicted_values, known_values) / ((known_values - known_values.mean()) ** 2).mean()) > 0 \
            else 0.0


def print_scores(model, X_train, X_test, y_train, y_test):
    # Print scores in one line:
    # [Train MSE, test MSE, Train R^2, Test R^2]
    train_mse = mse(X_train, y_train)
    test_mse = mse(X_test, y_test)
    train_r2 = rsq(X_train, y_train)
    test_r2 = rsq(X_test, y_test)
    print(train_mse, ", ", test_mse, ", ", train_r2, ", ", test_r2)


def accuracy_score(y_pred, y_actual):
    # The accuracy score is the ratio of correct predictions over the total number of predictions.
    num_correct_pred = 0
    # Count the number of correct preditions.
    for i in range(y_pred):
        if y_pred[i] == y_actual[i]:
            num_correct_pred += 1
    # Return the ratio.
    return num_correct_pred/len(y_pred)
