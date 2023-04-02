import datetime

import mlflow.sklearn
import numpy as np
import pandas_datareader.data as web
import yfinance as yf
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split

yf.pdr_override()


def acquire_training_data():

    start = datetime.datetime(2019, 7, 1)
    end = datetime.datetime(2019, 9, 30)
    df = web.get_data_yahoo("BTC-USD", start, end)

    return df


def digitize(n):

    if n > 0:
        return 1
    return 0


def rolling_window(a, window):

    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)

    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)


def prepare_training_data(data):

    data["Delta"] = data["Close"] - data["Open"]
    data["to_predict"] = data["Delta"].apply(lambda d: digitize(d))

    return data


if __name__ == "__main__":

    with mlflow.start_run():
        training_data = acquire_training_data()
        prepared_training_data_df = prepare_training_data(training_data)
        btc_mat = prepared_training_data_df.values
        WINDOW_SIZE = 14
        X = rolling_window(btc_mat[:, 7], WINDOW_SIZE)[:-1, :]
        Y = prepared_training_data_df["to_predict"].values[WINDOW_SIZE:]
        X_train, X_test, y_train, y_test = train_test_split(
            X, Y, test_size=0.2, random_state=4284, stratify=Y
        )
        clf = RandomForestClassifier(
            bootstrap=True,
            criterion="gini",
            min_samples_split=2,
            min_weight_fraction_leaf=0.0,
            n_estimators=50,
            random_state=4284,
            verbose=0,
        )
        clf.fit(X_train, y_train)
        predicted = clf.predict(X_test)
        mlflow.sklearn.log_model(clf, "model_random_forest")
        mlflow.log_metric(
            "precision_label_0", precision_score(y_test, predicted, pos_label=0)
        )
        mlflow.log_metric(
            "recall_label_0", recall_score(y_test, predicted, pos_label=0)
        )
        mlflow.log_metric("f1score_label_0", f1_score(y_test, predicted, pos_label=0))
        mlflow.log_metric(
            "precision_label_1", precision_score(y_test, predicted, pos_label=1)
        )
        mlflow.log_metric(
            "recall_label_1", recall_score(y_test, predicted, pos_label=1)
        )
        mlflow.log_metric("f1score_label_1", f1_score(y_test, predicted, pos_label=1))
