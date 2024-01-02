from re import X
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from django.conf import settings
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
# pip install chefboost
import os
path = os.path.join(settings.MEDIA_ROOT, "xAPI_Edu_Data.csv")
name = pd.read_csv(path)
name.drop(['NationalITy', 'PlaceofBirth', 'StageID'],axis=1)
df = name.drop(['NationalITy', 'PlaceofBirth','SectionID', 'Topic', 'Semester', 'Relation',],axis=1)
# x = df.iloc[:,:-1].values
# y = df.iloc[:,-1].values
# x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.25, random_state=27)
y = df['Class']
x = df.drop(['Class'], axis=1)
x=pd.get_dummies(x)
y=pd.get_dummies(y)
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.25, random_state=27)

def process_RandomForest():
    # Fitting Decision Tree classifier to the training set
    from sklearn.ensemble import RandomForestClassifier
    random = RandomForestClassifier()
    random = random.fit(x_train, y_train)
    ypred = random.predict(x_test)
    rf_cr = classification_report(y_test, ypred, output_dict=True)
    rf_cr = pd.DataFrame(rf_cr).transpose()
    rf_cr = pd.DataFrame(rf_cr)
    rf_cr = rf_cr.to_html
    rf_acc = accuracy_score(y_test,ypred)
    return rf_cr,rf_acc




def MLP():
    from sklearn.neural_network import MLPClassifier
    mlp = MLPClassifier()
    mlp.fit(x_train, y_train)
    y_pred = mlp.predict(x_test)
    mlp_cr = classification_report(y_test, y_pred, output_dict=True)
    mlp_cr = pd.DataFrame(mlp_cr).transpose()
    mlp_cr = pd.DataFrame(mlp_cr)
    mlp_cr = mlp_cr.to_html
    mlp_acc = accuracy_score(y_test, y_pred)
    return mlp_cr, mlp_acc

def C45():
    from chefboost import Chefboost as chef
    X = df.iloc[:, 0:10].values
    y = df.iloc[:, -1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)  # ,stratify='y')
    config = {'algorithm': 'C4.5'}
    model = chef.fit(df, config=config, target_label="Class")
    #y_pred = chef.predict(model, y_test)
    y_pred = []
    for row in range(len(X_test)):
        pred = chef.predict(model, X_test[row])
        y_pred.append(pred)
    c45_acc = accuracy_score(y_test, y_pred)
    c45_cr = classification_report(y_test, y_pred, output_dict=True)
    c45_cr = pd.DataFrame(c45_cr).transpose()
    c45_cr = pd.DataFrame(c45_cr)
    c45_cr = c45_cr.to_html
    return c45_cr, c45_acc



def process_rbf_kernel():
    path = os.path.join(settings.MEDIA_ROOT, "xAPI_Edu_Data.csv")
    name = pd.read_csv(path)
    name.drop(['NationalITy', 'PlaceofBirth', 'StageID'], axis=1)
    df = name.drop(['NationalITy', 'PlaceofBirth', 'SectionID', 'Topic', 'Semester', 'Relation', ], axis=1)
    # x = df.iloc[:,:-1].values
    # y = df.iloc[:,-1].values
    # x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.25, random_state=27)
    y = df['Class']
    x = df.drop(['Class'], axis=1)
    x = pd.get_dummies(x)
    # y = pd.get_dummies(y)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=27)
    print("Data:",x_train.iloc[1])
    from sklearn.svm import LinearSVC
    svm = LinearSVC()
    svm = svm.fit(x_train, y_train)
    ypred = svm.predict(x_test)
    svm_cr = classification_report(y_test, ypred, output_dict=True)
    svm_cr = pd.DataFrame(svm_cr).transpose()
    svm_cr = pd.DataFrame(svm_cr)
    svm_cr = svm_cr.to_html
    svm_acc = accuracy_score(y_test,ypred)
    return svm_cr,svm_acc



def process_browserInput(testset):
    # Fitting Decision Tree classifier to the training set
    from sklearn.ensemble import RandomForestClassifier
    random = RandomForestClassifier()
    random = random.fit(x_train, y_train)
    testset.append(1)
    # testset = testset.reshape(1, -1)
    result = random.predict([testset])
    return result

