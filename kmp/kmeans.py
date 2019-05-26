import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from collections import Counter

def kmeans(k, X, max_iter=300):
    X_size, n_features = X.shape

    # ランダムに重心の初期値を初期化
    centroids = X[np.random.choice(X_size, k)]

    # 前の重心と比較するために、仮に新しい重心を入れておく配列を用意
    new_centroids = np.zeros((k, n_features))
    #print(centroids)
    # 各データ所属クラスタ情報を保存する配列を用意
    cluster = np.zeros(X_size)

    # ループ上限回数まで繰り返し
    for epoch in range(max_iter):
        print("epoch:",epoch)
        # 入力データ全てに対して繰り返し
        for i in range(X_size):
            # データから各重心までの距離を計算（ルートを取らなくても大小関係は変わらないので省略）
            distances = np.sum((centroids - X[i]) ** 2, axis=1)
            #print(distances)
            # データの所属クラスタを距離の一番近い重心を持つものに更新
            cluster[i] = np.argsort(distances)[0]
            #print(np.argsort(distances))
            #print(cluster)
        # すべてのクラスタに対して重心を再計算
        for j in range(k):
            new_centroids[j] = X[cluster == j].mean(axis=0)

        # もしも重心が変わっていなかったら終了
        if np.sum(new_centroids == centroids) == k:
            print("break")
            break
        centroids = new_centroids
    return cluster



iris = datasets.load_iris()       # irisを読み込む関数
df = pd.DataFrame(
    iris.data,                    # データフレームの要素
    columns = iris.feature_names  # 各列の名前に特徴名を使う
)
df["label"] = iris.target         # わかりやすくするためにlabel列を追加、ここにクラス番号を入れておきます。

data_sample=df.head()                         # データフレームの先頭5行を表示してみましょう。
print(data_sample)

input_data = df.iloc[:,:-1].values
#print(input_data)
data_label=df.iloc[:,4:].values
print(len(data_label))
#print(data_label[:51])

cluster=kmeans(3, input_data,max_iter=10000)
# for i in range(len(cluster)):
#     if cluster[i]==data_label[i]:
#         j+=1

print(cluster)
cluster_1=cluster[:50]
res_1 = Counter(cluster_1).most_common(1)[0][1]
print(res_1)
cluster_2=cluster[51:100]
res_2 = Counter(cluster_2).most_common(1)[0][1]
print(res_2)
cluster_3=cluster[101:150]
res_3 = Counter(cluster_3).most_common(1)[0][1]
print(res_3)
successrate=(res_1+res_2+res_3)/150
print(successrate)
# print(len(cluster))
# print(cluster[0])
# print(cluster[149])
# df["cluster"] = cluster
# df.plot(kind="scatter", x=0, y=1, c="label", cmap="winter")  # cmapで散布図の色を変えられます。
# plt.title("true label")

#epoch=10000 and 300 get the same result =0.88