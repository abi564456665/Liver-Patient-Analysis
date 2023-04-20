# -*- coding: utf-8 -*-
"""datacleaning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lk9X-IXQjYJPhH_G3rM_AUWVB_-E_Gxa
"""

# Importing rquired lib

import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Checking for available styles

plt.style.available

# Applying styles to notebook

plt.style.use('fivethirtyeight')

# Reading csv data

df = pd.read_csv('/content/indian_liver_patient.csv')
df.head()

# Checking data type

df.info()

"""

 Types of Analysis
 1) Univariate analysis
 2) Bivariate analysis
 3) Multivariate analysis
 4) Descriptive analysis / statistics
 """

# Univariate analysis - Extracting info from a single column

# Checking data distribution

plt.figure(figsize=(12,5))
plt.subplot(121)
sns.distplot(df['Age'])
plt.subplot(122)
sns.distplot(df['Albumin_and_Globulin_Ratio'], color='g')

# Creating dummy dataframe for numerical values

df_cat = df.select_dtypes(include='float')
df_cat.head()

for i,j in enumerate(df_cat):
  print(j)
  print(i)

# Visualizing counts in each variable

plt.figure(figsize=(18,4))
for i,j in enumerate(df_cat):
  plt.subplot(1,5,i+1)
  sns.countplot(df[j])

plt.figure(figsize=(12,5))
plt.subplot(121)
sns.countplot(x='Albumin_and_Globulin_Ratio',data=df)

# Bivariate analysis - Extracting info double column

# Visualizing thes relation between Total_Bilirubin, Direct_Bilirubin, Total_Protiens, Albumin, Albumin_and_Globulin Ratio

plt.figure(figsize=(12,5))
plt.subplot(121)
sns.countplot(df['Albumin_and_Globulin_Ratio'], hue=df['Total_Bilirubin'])
plt.subplot(122)
sns.countplot(df['Albumdin_and_Globulin_Ratio'], hue=df['Direct_Bilirubin'])
plt.subplot(123)
sns.countplot(df['Albumin_and_Globulin_Ratio'], hue=df[' Total_Protien'])
plt.subplot(124)
sns.countplot(df['Albumin_and_Globulin_Ratio'], hue=df['Albumin'])

df['Age'].min()

# Creating new column

df['Age_'] = ['15-30' if x<30 else "30-50" if x>30 and x<=50 else '50+' for x in df['Age']]

df.head()

# Removing Age_ column

df.drop('Age_',axis=1, inplace=True)
df.head()

# Multivariate analysis - Extract info from more than 2 columns

sns.swarmplot(df['Albumin_and_Globulin_Ratio'],df['Albumin''])

# Finding corr

sns.heatmap(df.corr())

# Descriptive analysis - descriptive stat

df.describe(include='all')

# Data preprocessing

# Finding the shape of data

df.shape

# Finding null values

df.isnull().sum()

# remove null values

print(df['Albumin_and_Globulin_Ratio'].mean())

print(df['Albumin_and_Globulin_Ratio'].mean())
df['Albumin_and_Globulin_Ratio'] = df['Albumin_and_Globulin_Ratio'].fillna(0.947)
print(df.isnull().sum())

df.isnull().sum()

# Finding dtype

df.info()

# Finding outliers

sns.boxplot(df['Albumin_and_Globulin_Ratio'])

# Finding the count of outliers

# IQR = q3-q1......, ub = q3+(1.5*IQR), lb = q1-(1.5*IQR)
q1 = np.quantile(df['Albumin_and_Globulin_Ratio'],0.25)
q3 = np.quantile(df['Albumin_and_Globulin_Ratio'],0.75)

print('Q1 = {}'.format(q1))
print('Q3 = {}'.format(q3))

IQR = q3-q1

print('IQR value is {}'.format(IQR))

upperBound = q3+(1.5*IQR)
lowerBound = q1-(1.5*IQR)

print('The upper bound value is {} & the lower bound value is{}'. format(upperBound,lowerBound))

print('Skwed data :',len(df['Albumin_and_Globulin_Ratio']>upperBound))

print('Skwed data :',len(df['Albumin_and_Globulin_Ratio']>upperBound))

df['Alkaline_Phosphotase']>upperBound

df['Albumin_and_Globulin_Ratio']>upperBound

# Handling outliers

from scipy import stats

sns.distplot(df['Albumin_and_Globulin_Ratio'])

stats.probplot(np.log(df['Albumin_and_Globulin_Ratio']),plot=plt)

# Handidng outliers

from scipy import stats
plt.figure(figsize=(15,4))
plt.subplot(131)
sns.distplot(df['Albumin_and_Globulin_Ratio'])
plt.subplot(132)
stats.probplot(np.log(df['Albumin_and_Globulin_Ratio']),plot=plt)
plt.subplot(133)
sns.distplot(np.log(df['Albumin_and_Globulin_Ratio']))

# Transforming normal values to log values

df['Albumin_and_Globulin_Ratio']=np.log(df['Albumin_and_Globulin_Ratio'])

df.head()

# Encoding with replace method

df['Gender'] = df['Gender'].replace({'F':0, 'M':1})

df.head()

# Spliting dependent & Independent variables

x = df.drop('Albumin',axis=1)
x.head()

y = df['Albumin']
y

"""Simple Linear Regression"""

# import necessary lib

import numpy as np
import pandas as pd

# Reading the data

df = pd.read_csv('/content/indian_liver_patient.csv')
df.head()

# Checking the datatype

df.info()

# Descriptive Stat

df.describe()

# Checking null values

df.isnull().sum()

print(df['Albumin_and_Globulin_Ratio'].mean())
df['Albumin_and_Globulin_Ratio'] = df['Albumin_and_Globulin_Ratio'].fillna(0.947)
print(df.isnull().sum())

# Checking null values

df.isnull().sum()

# Visualizing data points

import matplotlib.pyplot as plt

plt.scatter(df['Total_Bilirubin'],df['Direct_Bilirubin'])

# independent variable

x = df.iloc[:,0:3]
x.head()

# dependent variable

y = df.iloc[:,3]
y.head()

# split training & testing 

from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.2,random_state=11)

print(xtrain.shape)
print(xtest.shape)

# model building

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

from sklearn.metrics import r2_score

"""Multi Linear Regression"""

# Import req lib
import pandas as pd
import numpy as np

# Read the dataset

df = pd.read_csv('/content/indian_liver_patient.csv')
df.head()

# checking data type

df.info()

# Checking for null values

df.isnull().sum()

print(df['Albumin_and_Globulin_Ratio'].mean())
df['Albumin_and_Globulin_Ratio'] = df['Albumin_and_Globulin_Ratio'].fillna(0.947)
print(df.isnull().sum())

# Descriptive stat

df.describe(include='all')

# Checking unique values

df['Gender'].unique()

# Converting object datatype to float

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df['Gender'] = le.fit_transform(df['Gender'])

df.head()

# Independent variables

y = df.iloc[:,9:]
y.head()

# Spliting data into training and testing set

from sklearn.model_selection import train_test_split

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2,random_state=10)

print(xtrain.shape)
print(xtest.shape)

# Model building

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

# finding acc

from sklearn.metrics import r2_score

r2_score(ytest,ypred)

"""Polynomial Regression"""

# Importing req lib

import numpy as np # Numerical python
import pandas as pd # for data manupulation
import matplotlib.pyplot as plt # for visualization
from sklearn.preprocessing import PolynomialFeatures # Polynomial regression
from sklearn.linear_model import LinearRegression # for building the model
from sklearn.metrics import r2_score # Checking accuracy

# Reading csv data

df = pd.read_csv('/content/indian_liver_patient.csv')
df.head()

# Checking rows and columns

df.shape

# finding datatype for all variable

df.info()

# checking for unique values

df['Gender'].unique()

# checking for null values

df.isnull().sum()

print(df['Albumin_and_Globulin_Ratio'].mean())
df['Albumin_and_Globulin_Ratio'] = df['Albumin_and_Globulin_Ratio'].fillna(0.947)
print(df.isnull().sum())

# finding co-relation

df.corr()

# seperating in-dependent variables

x = df.iloc[:,2:4]
x.head()

# seperating dependent variable

y = df.iloc[:,9:]
y.head()

plt.scatter(df['Total_Bilirubin'],df['Albumin_and_Globulin_Ratio'])

# initializing polynomial regression/features

py = PolynomialFeatures()

# transforming x values

xp = py.fit_transform(x)
xp

# initializing linear regression

lr = LinearRegression()

# training the model

lr.fit(xp,y)

lr.predict(py.transform([[2,3]]))

"""**Logistic** **Regression**"""

# importing req lib

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('/content/indian_liver_patient.csv')
df.head(10)

# descriptive stat

df.describe()

df.shape

df.info()

df.isnull().sum()

df.head()

df.drop(columns=['Age'],inplace=True)

df['Gender'].unique()

# feature mapping

df['Gender'].replace({"Female":0,"Male":1},inplace=True)

# spliting independent & dependent variables

x = df.drop('Albumin_and_Globulin_Ratio',axis=1)
y = df['Albumin_and_Globulin_Ratio']

# spliting training data & testing data

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=10)

print("shape of independent training data is {}. shape of independent testing data is {}" .format(x_train.shape, x_test.shape))
print("shape of independent training data is {}. shape of independent testing data is {}" .format(y_train.shape, y_test.shape))

# initializing logistic reg

log_r = LogisticRegression()

# Training model
log_r.fit(ytrain,xtrain)

ytest

# evaluating model

from sklearn.metrics import classification_report, confusion_matrix

"""**Decision** **Random** **Tree** **Classification**"""

# importing req lib

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from scipy import stats

# read and run the data

df = pd.read_csv('/content/indian_liver_patient.csv')
df.head()

df.info()

"""

 Types of Analysis
 1) Univariate analysis
 2) Bivariate analysis
 3) Multivariate analysis
 4) Descriptive analysis / statistics
 """

# Univariate analysis - Extracting info from a single column

# Checking data distribution

plt.figure(figsize=(12,5))
plt.subplot(121)
sns.distplot(df['Albumin'])
plt.subplot(122)
sns.distplot(df['Albumin_and_Globulin_Ratio'], color='r')

# Creating dummy dataframe for numerical values

df_cat = df.select_dtypes(include='float')
df_cat.head()

# Visualizing counts in each variable

plt.figure(figsize=(18,4))
for i,j in enumerate(df_cat):
  plt.subplot(1,5,i+1)
  sns.countplot(df[j])

plt.figure(figsize=(12,5))
plt.subplot(121)
sns.countplot(x='Albumin_and_Globulin_Ratio',data=df)

# Bivariate analysis - Extracting info double column

# Visualizing thes relation between Total_Bilirubin, Direct_Bilirubin, Total_Protiens, Albumin, Albumin_and_Globulin Ratio

plt.figure(figsize=(12,5))
plt.subplot(121)
sns.countplot(df['Albumin_and_Globulin_Ratio'], hue=df['Total_Bilirubin'])
plt.subplot(122)
sns.countplot(df['Albumdin_and_Globulin_Ratio'], hue=df['Direct_Bilirubin'])
plt.subplot(123)
sns.countplot(df['Albumin_and_Globulin_Ratio'], hue=df[' Total_Protien'])
plt.subplot(124)
sns.countplot(df['Albumin_and_Globulin_Ratio'], hue=df['Albumin'])

df['Albumin'].min()

# Creating new column

df['Albumin_'] = ['2.4-3.1' if x<30 else "3.2-3.3" if x>30 and x<=50 else '3.4+' for x in df['Albumin']]

df.head()

# Removing Albumin_ column

df.drop('Albumin_',axis=1, inplace=True)
df.head()

# Multivariate analysis - Extract info from more than 2 columns

sns.swarmplot(df['Albumin_and_Globulin_Ratio'],df['Albumin''])

# Finding corr

sns.heatmap(df.corr())

# Descriptive analysis - descriptive stat

df.describe(include='all')

# Data preprocessing

df.shape

df.isnull().sum()

# remove null values

print(df['Albumin_and_Globulin_Ratio'].mean())

print(df['Albumin_and_Globulin_Ratio'].mean())
df['Albumin_and_Globulin_Ratio'] = df['Albumin_and_Globulin_Ratio'].fillna(0.947)
print(df.isnull().sum())

df.info()

sns.boxplot(df['Albumin_and_Globulin_Ratio'])

# finding for outliers

q1 = np.quantile(df['Albumin_and_Globulin_Ratio'],0.25)
q3 = np.quantile(df['Albumin_and_Globulin_Ratio'],0.75)

IQR = q3-q1

upper_bound = q3+(1.5*IQR)
lower_bound = q1-(1.5*IQR)

skewed_values = len(df[df['Albumin_and_Globulin_Ratio']>upper_bound])

print('Q1 = {}'.format(q1))
print('Q3 = {}'.format(q3))
print('IQR = {}'.format(IQR))
print('upper bound = {}'.format(upper_bound))
print('lower bound = {}'.format(lower_bound))
print('count of skewed data = {}'.format(skewed_values))

# Handling outliers

def transform(Albumin_and_Globulin_Ratio):
  plt.figure(figsize=(14,6))
  plt.subplot(131)
  sns.distplot(Albumin_and_Globulin_Ratio)
  plt.subplot(122)
  stats.probplot(Albumin_and_Globulin_Ratio,plot=plt)

transform(df['Albumin_and_Globulin_Ratio'])

transform(np.log(df['Albumin_and_Globulin_Ratio']))

df['Albumin_and_Globulin_Ratio'] = np.log(df['Albumin_and_Globulin_Ratio'])
df.head()

df['Gender'] = df['Gender'].replace({'Female':0,'Male':1})

df.head()

# spliting dep & indep

x = df.drop('Dataset',axis=1)
y = df['Dataset']

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2,random_state=20)

xtrain.shape,xtest.shape

# Decision tree

dt = DecisionTreeClassifier()

dt.fit(xtrain,ytrain)

ytest

pd.Series(dt.predict(xtest))

pd.DataFrame((ytest,pd.Series(dt.predict(xtest))),columns=['Actual','Predict'])

print(classification_report(ytest,dt.predict(xtest)))

confusion_matrix(ytest,dt.predict(xtest))

ytest

dt.predict(xtest)

a = pd.DataFrame([np.array(ytest),dt.predict(xtest)]).T

a.columns=['Actual','Predict']

a

# random forest

rf = RandomForestClassifier()

rf.fit(xtrain,ytrain)

print(classification_report(ytest,rf.predict(xtest)))

confusion_matrix(ytest,rf.predict(xtest))

rf.predict([[65,0,0.7,0.1,187,16,18,6.8,3.3,np.log(25)]])

rf.predict([[62,1,7.3,4.1,490,60,68,7.0,3.3,np.log(25)]])

"""**KNN**"""

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()

knn.fit(xtrain,ytrain)

print(classification_report(ytest,knn.predict(xtest)))

confusion_matrix(ytest,knn.predict(xtest))

"""**SVM**"""

from sklearn.svm import SVC

svc = SVC()

svc.fit(xtrain,ytrain)

print(classification_report(ytest,svc.predict(xtest)))

confusion_matrix(ytest,svc.predict(xtest))

"""**Naive** **Bayes**"""

from sklearn import naive_bayes

data = pd.read_csv('/content/indian_liver_patient.csv')
data.head()

data.shape

data.isnull().sum()

# remove null values

print(data['Albumin_and_Globulin_Ratio'].mean())

print(data['Albumin_and_Globulin_Ratio'].mean())
data['Albumin_and_Globulin_Ratio'] = data['Albumin_and_Globulin_Ratio'].fillna(0.947)
print(data.isnull().sum())

data.info()

# spliting dependent and independent

x = data.iloc[:,1:]
y = data.iloc[:,0]

x

col_name = x.columns

col_name

# manual encoding

x = np.where(x=='0.1',1,x)
x = np.where(x=='Female',0,x)

x = pd.DataFrame(x,columns=col_name)
x.head()

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2,random_state=0)

import numpy as np

xtrain.shape,ytrain.shape

nb = naive_bayes.GaussianNB()

nb.fit(xtrain,ytrain)

print(classification_report(ytest,nb.predict(xtest)))

confusion_matrix(ytest,nb.predict(xtest))

"""**ANN** **Regression** **Classification**"""

# import req lib

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# reading the data

df = pd.read_csv('/content/indian_liver_patient.csv')
df.head()

# checking data type

df.info()

# checking for null values

df.isnull().sum()

# remove null values

print(df['Albumin_and_Globulin_Ratio'].mean())

print(df['Albumin_and_Globulin_Ratio'].mean())
df['Albumin_and_Globulin_Ratio'] = df['Albumin_and_Globulin_Ratio'].fillna(0.947)
print(df.isnull().sum())

df.info()

# descriptive stat

df.describe()

# checking unique values in Gender column

df['Gender'].unique()

# converting object dtype into int dtype

from sklearn.preprocessing import LabelEncoder

# initializing label encoder(encoding is a technique which used to convert string dtype into numerical dtype)

le = LabelEncoder()

df['Gender'] = le.fit_transform(df['Gender'])

df.head()

# independent variable

x = df.drop('Albumin_and_Globulin_Ratio',axis=1)
x.head()

# dependent variable

y = df.iloc[:,9:]
y.head()

# spliting training and testing data

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2,random_state=10)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential() # initializing the model
model.add(Dense(10,activation='relu')) # input layer
model.add(Dense(350,activation='relu')) # hidden layer
model.add(Dense(1,activation='linear')) # output layer

model.compile(optimizer='rmsprop', loss='mse', metrics=['mse'])

model.fit(xtrain, ytrain, batch_size=2, epochs=20)

model.predict([[62,1,7.3,4.1,490,60,68,7.0,3.3,1]])

model.predict([[58,1,1.0,0.4,182,14,20,6.8,3.4,1]])

"""**ANN** **Classification**"""

data = pd.read_csv('/content/indian_liver_patient.csv')
data.head()

data.info()

data.isnull().sum()

# remove null values

print(data['Albumin_and_Globulin_Ratio'].mean())

print(data['Albumin_and_Globulin_Ratio'].mean())
data['Albumin_and_Globulin_Ratio'] = data['Albumin_and_Globulin_Ratio'].fillna(0.947)
print(data.isnull().sum())

data.isnull().sum()

data['Albumin_and_Globulin_Ratio'] = np.log(data['Albumin_and_Globulin_Ratio'])

data['Gender'].unique()

data['Gender'] = [0 if x == 'Male' else 1 for x in data['Gender']]

data.head()

data.info()

x = data.drop('Dataset',axis=1)
x.head()

y = data['Dataset']
y

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=11)

classification = Sequential()
classification.add(Dense(10,activation='relu'))
classification.add(Dense(60,activation='relu'))
classification.add(Dense(32,activation='relu'))
classification.add(Dense(10,activation='softmax'))

classification.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

classification.fit(x_train,y_train,batch_size=2,epochs=30,validation_data=(x_test,y_test))

classification.predict([[72,0,3.9,2.0,195,27,59,7.3,2.4,-0.916291]])

op = np.argmax(classification.predict([[72,0,3.9,2.0,195,27,59,7.3,2.4,-0.916291]]))

op

names = ['Female','Male']

names[op]