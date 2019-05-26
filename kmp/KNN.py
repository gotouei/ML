import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

from collections import Counter


def knn(k, train_data, test_data):
    labels = []

    for test in test_data:

        # 1. すべてのトレインデータとtest（このループステップでラベルを予測したいデータ）との距離を計算したリストを作る
        distances = np.sum((train_data[: ,:-1 ] -test[:-1] )**2, axis=1)
        #print(distances)
        # 2. 距離リストの値が小さい順に並べた、トレインデータのインデックスを持つリストを作る
        sorted_train_indexes = np.argsort(distances)

        # 3. インデックスリストを元に、testから近いk個のトレインデータのラベルを取り出す
        sorted_k_labels = train_data[sorted_train_indexes, -1][:k]
        #print(Counter(sorted_k_labels).most_common(1))
        # 4. sorted_k_labelsの中で最も数の多かったlabelを取り出す
        label = Counter(sorted_k_labels).most_common(1)[0][0]#??
        labels.append(label)
    return labels

# sss=[1,3,2,1,1,1]
# # tmp=Counter(sss).most_common()#[(1, 4), (3, 1), (2, 1)]
# tmp=Counter(sss).most_common(1)[0][1]#4
# print(tmp)

iris = datasets.load_iris()
df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)
df["label"] = iris.target

df.head()
df = df.sample(frac=1).reset_index(drop=True)
df.head()


train_size = 75
train_data = df.iloc[:train_size].values
# train_data = df.iloc[:train_size].values
test_data = df.iloc[train_size:].values

print(train_data)
print(test_data)
pred_labels = knn(2, train_data, test_data)
#beacuse train and test data are different in each time, so the result will change each time
aa=np.sum(pred_labels == test_data[:,-1]) / len(test_data)
print(aa)
# test_df = df.iloc[train_size:].copy()
# test_df["pred_label"] = pred_labels
#
# test_df.plot(kind="scatter", x=0, y=1, c="label", cmap="winter")
# plt.title("true label")
# test_df.plot(kind="scatter", x=0,y=1,c="pred_label", cmap="winter")
# plt.title("prediction label")