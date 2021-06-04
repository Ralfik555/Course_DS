
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2


###--------------- definicja cross testów ----------
def get_mean_score(model, xs, ys):
    scores = []
    cv = KFold(n_splits=5)
    for train_i, test_i in cv.split(xs, ys):   
        x_train, y_train = xs.iloc[train_i], ys[train_i]
        x_test, y_test = xs.iloc[test_i], ys[test_i]
        model.fit(x_train, y_train)
        score = model.score(x_test, y_test)
        scores.append(score)
    return np.mean(scores)

data = pd.read_csv("gender_recognition_by_voice.csv")
y = data['label']

# ---------- Dane w oryginalnej postaci
X_org = data.drop('label', axis=1)

# ---------- Dane bez silnie skorelowanych cech, wpsółczynnik korelacji > 0.8

corr = X_org.corr().abs()
n_features = corr.shape[0]
strong_corr_features = []

for i in range(n_features):
    for j in range(n_features):
        if i != j:
            if corr.iloc[i, j] >= 0.8:
                strong_corr_features.append(corr.columns[i])

X_corr = X_org.drop(list(set(strong_corr_features)), axis=1)

# ---------- Dane zawierające tylko cechy wskazane przez test chi2

select_feature = SelectKBest(chi2).fit(X_org, y)
new_features = X_org.columns[select_feature.get_support()]
X_chi2 = X_org[new_features]

# ---------- Obliczenie skuteczność klasyfikacji za pomocą sprawdzianu krzyżowego z k-podziałami

model_log = LogisticRegression()
model_rf = RandomForestClassifier()
model_knn = KNeighborsClassifier()

models = [model_log,model_rf,model_knn]
models_names = ['Logistinc regression','Random Forest','KNN']
m = models[0]

for m,n in zip(models,models_names):
    print(n)
    print('All features: {:.3f}'.format(get_mean_score(m,X_org,y)))
    print('No correlated features: {:.3f}'.format(get_mean_score(m,X_corr,y)))
    print('Chi2 features: {:.3f}'.format(get_mean_score(m,X_chi2,y)))
    print()

