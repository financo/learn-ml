import numpy as np
from math import sqrt
from collections import Counter


def kNN_classify(k, X_train, y_train, x):

    assert 1 <= k <= X_train.shape[0], "k must be valid"
    assert X_train.shape[0] == y_train.shape[0], "the size of X_train must equal to the size of y_train"
    assert X_train.shape[1] == x.shape[0], "the feature number of x must be equal to X_train"

    distance = [sqrt(sum((x_train - x) ** 2)) for x_train in X_train]
    most_common = Counter(y_train[np.argsort(distance)[:k]]).most_common(1)
    predict = most_common[0][0]
    return predict


if __name__ == '__main__':
    raw_data_X = [[3.393533211, 2.331273381],
                  [3.110073483, 1.781539638],
                  [1.343808831, 3.368360954],
                  [3.582294042, 4.679179110],
                  [2.280362439, 2.866990263],
                  [7.423436942, 4.696522875],
                  [5.745051997, 3.533989803],
                  [9.172168622, 2.511101045],
                  [7.792783481, 3.424088941],
                  [7.939820817, 0.791637231]
                  ]
    raw_data_y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

    X_train = np.array(raw_data_X)
    y_train = np.array(raw_data_y)

    x = np.array([8.093607318, 3.365731514])

    print(kNN_classify(6, X_train, y_train, x))