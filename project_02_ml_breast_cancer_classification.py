# -*- coding: utf-8 -*-
"""Project_02_ML_Breast_cancer_classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tbywgMo17zBjuVU0ATctI2s-kzoLpBxu
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score
import warnings
warnings.filterwarnings('ignore')

breast_cancer_dataset = load_breast_cancer()

df = pd.DataFrame(breast_cancer_dataset.data, columns=breast_cancer_dataset.feature_names)
df['label'] = breast_cancer_dataset.target
df.head()

df.shape

df.info()

df.duplicated().sum()

print(df['label'].value_counts())
df['label'].value_counts().plot(kind='bar',color={'red','green'})

df.groupby('label').mean()

X = df.drop(columns='label', axis=1)
y = df['label']

X.shape, y.shape

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)

X_train.shape,y_train.shape,X_test.shape,y_test.shape

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

model = LogisticRegression()
model.fit(X_train,y_train)

y_train_pred = model.predict(X_train)
print("Accuracy score is: ",accuracy_score(y_train,y_train_pred))

y_pred = model.predict(X_test)
y_pred

print("Accuracy score is: ",accuracy_score(y_test,y_pred))

input_data = (13.54,14.36,87.46,566.3,0.09779,0.08129,0.06664,0.04781,0.1885,0.05766,0.2699,0.7886,2.058,23.56,0.008462,0.0146,0.02387,0.01315,0.0198,0.0023,15.11,19.26,99.7,711.2,0.144,0.1773,0.239,0.1288,0.2977,0.07259)

# change the input into numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the numpy array as we prediction for one data point
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# Standarized the input data
std_data = sc.transform(input_data_reshaped)

prediction = model.predict(std_data)

if(prediction == 0):
    print("The breast cancer is Malignant")
else:
    print("The breast cancer is Benign")