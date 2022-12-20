from datetime import datetime

import numpy as np
import pandas as pd
import lightgbm as lgb
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns

def analyze_diabetes(HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack,
                     PhysActivity, Fruits, Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth, MentHlth,
                     PhysHlth, DiffWalk, Sex, Age, Education):
    px_template = "simple_white"
    data = pd.read_csv('analyze/export_diabet.csv')
    data.head()
    data.isna().sum()
    Q = "Diabetes_012"
    df0 = data

    plt.figure(figsize=(3, 4))
    ax = sns.countplot(x=df0[Q], data=df0)
    plt.title("Countplot of Participants' Diabetes")
    for i in ax.containers:
        ax.bar_label(i, ),
    data.Diabetes_012[data.Diabetes_012 == 2] = 1
    data.Diabetes_012.unique()
    plt.figure(figsize=(3, 4))
    ax = sns.countplot(x=df0[Q], data=df0)
    plt.title("Countplot of Participants' Diabetes")

    for i in ax.containers:
        ax.bar_label(i, ),

    data.drop('Diabetes_012', axis=1).corrwith(data.Diabetes_012).sort_values(
        ascending=False).plot(kind='bar', grid=True, figsize=(12, 4), title="Correlation with Diabetes")
    data = data.drop('Income', axis=1)
    data.drop('Diabetes_012', axis=1).corrwith(data.Diabetes_012).sort_values(
        ascending=False).plot(kind='bar', grid=True, figsize=(12, 4), title="Correlation with Diabetes")

    x = data.drop(['Diabetes_012', 'Label', 'Date'], axis=1)
    y = data['Diabetes_012']
    x_train, xx, y_train, yy = train_test_split(x, y, test_size=0.8, random_state=23)
    clf = lgb.LGBMClassifier(boosting_type='gbdt', objective='binary', learning_rate=0.07, n_estimators=4000,
                             reg_lambda=2,
                             max_depth=5, num_leaves=20)
    clf.fit(x_train, y_train)
    train_predict = clf.predict(x_train)
    test_predict = clf.predict(xx)
    im = clf.feature_importances_
    col = np.array(x.columns)

    dd = pd.DataFrame(im, columns=['importance'])
    dd.insert(1, 'feature name', value=col)
    dd.sort_values(by='importance', ascending=False, inplace=True)
    data.to_csv('export_diabet.csv', index=False, header=True)
    label = "Capchered_site"
    dt_string = datetime.now()
    new_vector = [[HighBP, HighChol, CholCheck, BMI, Smoker,
                   Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies,
                   HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth,
                   MentHlth, PhysHlth, DiffWalk, Sex, Age, Education]]
    Diabetes_Prediction = clf.predict(new_vector)
    if Diabetes_Prediction == 2:
        result = "Positive"
    else:
        result = "Negative"
    data0 = data[data["Age"] == Age]
    pd.crosstab(data0.Age, data0.Diabetes_012)
