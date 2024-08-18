from pandas import DataFrame
from sklearn.preprocessing import StandardScaler

def scale_data(X_train: DataFrame, X_test: DataFrame, X_prod_test: DataFrame):
# Standardize the features and normalize
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    X_prod_test_scaled = scaler.transform(X_prod_test)

    return DataFrame(X_train_scaled), DataFrame(X_test_scaled), DataFrame(X_prod_test_scaled)