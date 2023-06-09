# -*- coding: utf-8 -*-
"""LING 513.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YijUbU1tH10EH9YQA_xubU1chXJYuiWV
"""

!pip install librosa

import librosa
import librosa.display
import IPython.display as ipd
import numpy as np
import os
import pandas as pd

for file in os.listdir('/content/NativeDifferent/it'):
  print(file)

ipd.Audio('Native1/Native1_i_2_.wav')

def feature_extraction(file_path):
  # Load the audio file
  x, sample_rate = librosa.load(file_path)
  # Extract features from the audio
  mfcc = np.mean(librosa.feature.mfcc(y=x, sr=sample_rate, n_mfcc=13).T, axis=0)

  return mfcc

# res_type='kaiser_fast'

# !pip install llvmlite==0.31.0

# !pip install resampy

# pip install resampy==0.2

features = {}
directory = '/content/NativeDifferent/it/'
for audio in os.listdir(directory):
  audio_path = directory+audio
  features[audio_path] = feature_extraction(audio_path)

set_features = []
features = {}
directory = '/content/NativeDifferent/it/'
for audio in os.listdir(directory):
  audio_path = directory+audio
  features[audio_path] = feature_extraction(audio_path)
  set_features.append(features[audio_path])

print(set_features)

df_NativeDif_it = pd.DataFrame(set_features, index=['Native_it1','Native_it2','Native_it3'], columns=['MFCC1', 'MFCC2', 'MFCC3','MFCC4', 'MFCC5', 'MFCC6', 'MFCC7', 'MFCC8', 'MFCC9', 'MFCC10', 'MFCC11', 'MFCC12', 'MFCC13'])

print(df_NativeDif_it)

df1_NativeDif_it = df_NativeDif_it.reset_index()
print(df1_NativeDif_it)

df1_NativeDif_it['word'] = 5
print(df1_NativeDif_it)

df1_NativeDif_it['participant number'] = 4
print(df1_NativeDif_it)

df1_NativeDif_it.to_csv(r'/content/NativeDif_it.csv', index=False)

# df3 = df1.append(df2, ignore_index=True)

# I=1, you=2, he=3, she=4, it=5, we=6, they=7

"""## Models"""

!pip install pyreadstat

#import library
import pickle
import pandas_profiling
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, log_loss
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from xgboost import XGBClassifier
import xgboost
import math
from sklearn import metrics
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import Perceptron

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV, KFold
import warnings
warnings.filterwarnings('ignore')

# To read from a csv file 
my_data_new = pd.read_csv('trainset new.csv')
my_data_new

my_data_new.columns.values.tolist()

scaler = RobustScaler()
features = [['MFCC1',
 'MFCC2',
 'MFCC3',
 'MFCC4',
 'MFCC5',
 'MFCC6',
 'MFCC7',
 'MFCC8',
 'MFCC9',
 'MFCC10',
 'MFCC11',
 'MFCC12',
 'MFCC13']]
for feature in features:
    my_data_new[feature] = scaler.fit_transform(my_data_new[feature])
my_data_new

my_data_new['word'].value_counts()

X = my_data_new.drop(['word', 'participant number', 'index'],axis=1).values
X

y = my_data_new['word'].values
y

#frequency for np array
unique, counts = np.unique(y, return_counts=True)
print(np.unique(y, return_counts=True))

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42, stratify=y)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# grid search and cross validation for SVM
from sklearn.svm import SVC
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import RandomizedSearchCV

# define model
model = SVC()

# define evaluation
cv = RepeatedStratifiedKFold(n_splits=5, n_repeats=1, random_state=2023)

# define search space
space = dict()
space['C'] = [0.1, 1, 10]
space['gamma'] = [1, 0.1, 0.01]
space['kernel'] = ['rbf', 'linear']

# define search
search = RandomizedSearchCV(model, space, n_iter=10, scoring='accuracy', n_jobs=-1, cv=cv, random_state=1)

# execute search
result = search.fit(X_train, y_train)
# summarize result
print('Best Score: %s' % result.best_score_)
print('Best Hyperparameters: %s' % result.best_params_)

# define model svm
# only from trainset
from sklearn.svm import SVC
model = SVC(kernel='rbf', C=10, gamma=0.1)
svm = model.fit(X_train, y_train)
y_pred = svm.predict(X_test)
print(accuracy_score(y_test, y_pred))

from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)

pd.crosstab(y_test, y_pred, rownames=['True'], colnames=['Predicted'], margins=True)

#import classification_report
from sklearn.metrics import classification_report

print(classification_report(y_test,y_pred))

# Cross-validation for LogisticRegression -- Ask about this from Maria!
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import loguniform

# define model
model = LogisticRegression()

# define evaluation
cv = RepeatedStratifiedKFold(n_splits=5, n_repeats=1, random_state=1)

# define search space
space = dict()
space['solver'] = ['newton-cg', 'lbfgs', 'liblinear']
space['penalty'] = ['none', 'l1', 'l2', 'elasticnet']
space['C'] = loguniform(0.01, 10)

# define search
search = RandomizedSearchCV(model, space, n_iter=500, scoring='accuracy', n_jobs=-1, cv=cv, random_state=1)

# execute search
result = search.fit(X_train, y_train)
# summarize result
print('Best Score: %s' % result.best_score_)
print('Best Hyperparameters: %s' % result.best_params_)

from sklearn.linear_model import LogisticRegressionCV
model = LogisticRegressionCV(multi_class='multinomial', penalty='l2', solver='lbfgs', cv=5, random_state=0)
log_reg = model.fit(X_train, y_train)
y_pred = log_reg.predict(X_test)
print(accuracy_score(y_test, y_pred))

#training accuracy
train_accuracy = model.score(X_train, y_train)
print(train_accuracy)

from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)

pd.crosstab(y_test, y_pred, rownames=['True'], colnames=['Predicted'], margins=True)

#import classification_report
from sklearn.metrics import classification_report

print(classification_report(y_test,y_pred))

"""# Non-Native Test"""

# reading the testset data
nonnative_testset = pd.read_csv('testset - Non-native.csv')
nonnative_testset

scaler = RobustScaler()
features = [['MFCC1',
 'MFCC2',
 'MFCC3',
 'MFCC4',
 'MFCC5',
 'MFCC6',
 'MFCC7',
 'MFCC8',
 'MFCC9',
 'MFCC10',
 'MFCC11',
 'MFCC12',
 'MFCC13']]
for feature in features:
    nonnative_testset[feature] = scaler.fit_transform(nonnative_testset[feature])
nonnative_testset

nonnative_testset['word'].value_counts()

X_nonnative = nonnative_testset.drop(['word', 'participant number', 'index'],axis=1).values
X_nonnative

y_nonnative = nonnative_testset['word'].values
y_nonnative

print(X_nonnative.shape)
print(y_nonnative.shape)

# testing the testset
model = SVC(kernel='rbf', C=10, gamma=0.1)
svm = model.fit(X_train, y_train)
y_pred_nonnative = svm.predict(X_nonnative)
print(accuracy_score(y_nonnative, y_pred_nonnative))

from sklearn.metrics import confusion_matrix
confusion_matrix_nonnative = confusion_matrix(y_nonnative, y_pred_nonnative)
print(confusion_matrix_nonnative)

pd.crosstab(y_nonnative, y_pred_nonnative, rownames=['True'], colnames=['Predicted'], margins=True)

#import classification_report
from sklearn.metrics import classification_report

print(classification_report(y_nonnative,y_pred_nonnative))

model = LogisticRegressionCV(multi_class='multinomial', penalty='l2', solver='lbfgs', cv=5, random_state=0)
log_reg = model.fit(X_train, y_train)
y_pred_nonnative = log_reg.predict(X_nonnative)
print(accuracy_score(y_nonnative, y_pred_nonnative))

confusion_matrix_nonnative = confusion_matrix(y_nonnative, y_pred_nonnative)
print(confusion_matrix_nonnative)

pd.crosstab(y_nonnative, y_pred_nonnative, rownames=['True'], colnames=['Predicted'], margins=True)

print(classification_report(y_nonnative,y_pred_nonnative))



"""## NativeDifferent test"""

# reading the testset data
nativedif_testset = pd.read_csv('testset - NativeDifferent.csv')
nativedif_testset

scaler = RobustScaler()
features = [['MFCC1',
 'MFCC2',
 'MFCC3',
 'MFCC4',
 'MFCC5',
 'MFCC6',
 'MFCC7',
 'MFCC8',
 'MFCC9',
 'MFCC10',
 'MFCC11',
 'MFCC12',
 'MFCC13']]
for feature in features:
    nativedif_testset[feature] = scaler.fit_transform(nativedif_testset[feature])
nativedif_testset

nativedif_testset['word'].value_counts()

X_nativedif = nativedif_testset.drop(['word', 'participant number', 'index'],axis=1).values
X_nativedif

y_nativedif = nativedif_testset['word'].values
y_nativedif

print(X_nativedif.shape)
print(y_nativedif.shape)

# testing the testset
model = SVC(kernel='rbf', C=10, gamma=0.1)
svm = model.fit(X_train, y_train)
y_pred_nativedif = svm.predict(X_nativedif)
print(accuracy_score(y_nativedif, y_pred_nativedif))

from sklearn.metrics import confusion_matrix
confusion_matrix_nativedif = confusion_matrix(y_nativedif, y_pred_nativedif)
print(confusion_matrix_nativedif)

pd.crosstab(y_nativedif, y_pred_nativedif, rownames=['True'], colnames=['Predicted'], margins=True)

#import classification_report
from sklearn.metrics import classification_report

print(classification_report(y_nativedif,y_pred_nativedif))

model = LogisticRegressionCV(multi_class='multinomial', penalty='l2', solver='lbfgs', cv=5, random_state=0)
log_reg = model.fit(X_train, y_train)
y_pred_nativedif = log_reg.predict(X_nativedif)
print(accuracy_score(y_nativedif, y_pred_nativedif))

confusion_matrix_nativedif = confusion_matrix(y_nativedif, y_pred_nativedif)
print(confusion_matrix_nativedif)

pd.crosstab(y_nativedif, y_pred_nativedif, rownames=['True'], colnames=['Predicted'], margins=True)

print(classification_report(y_nativedif,y_pred_nativedif))