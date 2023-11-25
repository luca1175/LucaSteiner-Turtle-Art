#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd


from scipy.stats import zscore
import matplotlib.pyplot as plt
from matplotlib.pyplot import *


import io
import requests
import os

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping
import tensorflow.keras.backend as K
from tensorflow.keras.utils import get_file
import seaborn as sns
import datetime as dt

from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, roc_auc_score

xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.25, random_state=42)

path = get_file('kddcup.data_10_percent.gz', 
                origin='http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz')

df = pd.read_csv(path, header=None)

df.columns = [
    'duration',
    'protocol_type',
    'service',
    'flag',
    'src_bytes',
    'dst_bytes',
    'land',
    'wrong_fragment',
    'urgent',
    'hot',
    'num_failed_logins',
    'logged_in',
    'num_compromised',
    'root_shell',
    'su_attempted',
    'num_root',
    'num_file_creations',
    'num_shells',
    'num_access_files',
    'num_outbound_cmds',
    'is_host_login',
    'is_guest_login',
    'count',
    'srv_count',
    'serror_rate',
    'srv_serror_rate',
    'rerror_rate',
    'srv_rerror_rate',
    'same_srv_rate',
    'diff_srv_rate',
    'srv_diff_host_rate',
    'dst_host_count',
    'dst_host_srv_count',
    'dst_host_same_srv_rate',
    'dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate',
    'dst_host_srv_diff_host_rate',
    'dst_host_serror_rate',
    'dst_host_srv_serror_rate',
    'dst_host_rerror_rate',
    'dst_host_srv_rerror_rate',
    'outcome'
]
df[0:19289]

df.drop_duplicates(keep='first', inplace = True)
df.dropna(inplace=True,axis=1) 


def encode_numeric_zscore(df, name, mean=None, sd = None):
    if mean is None:
        mean = df[name].mean()
        
    if sd is None:
        sd = df[name].std()
    
    df[name] = (df[name]-mean)/sd
    
def encode_text_dummy(df, name):
    dummy = pd.get_dummies(df[name])
    for _ in dummy.columns:
        dummyname = f"{name}- {_}"
        df[dummyname] = dummy[_]
    df.drop(name, axis = 1, inplace=True)

    
encode_numeric_zscore(df, 'duration')
encode_text_dummy(df, 'protocol_type')
encode_text_dummy(df, 'service')
encode_text_dummy(df, 'flag')
encode_numeric_zscore(df, 'src_bytes')
encode_numeric_zscore(df, 'dst_bytes')
encode_text_dummy(df, 'land')
encode_numeric_zscore(df, 'wrong_fragment')
encode_numeric_zscore(df, 'urgent')
encode_numeric_zscore(df, 'hot')
encode_numeric_zscore(df, 'num_failed_logins')
encode_text_dummy(df, 'logged_in')
encode_numeric_zscore(df, 'num_compromised')
encode_numeric_zscore(df, 'root_shell')
encode_numeric_zscore(df, 'su_attempted')
encode_numeric_zscore(df, 'num_root')
encode_numeric_zscore(df, 'num_file_creations')
encode_numeric_zscore(df, 'num_shells')
encode_numeric_zscore(df, 'num_access_files')
encode_numeric_zscore(df, 'num_outbound_cmds')
encode_text_dummy(df, 'is_host_login')
encode_text_dummy(df, 'is_guest_login')
encode_numeric_zscore(df, 'count')
encode_numeric_zscore(df, 'srv_count')
encode_numeric_zscore(df, 'serror_rate')
encode_numeric_zscore(df, 'srv_serror_rate')
encode_numeric_zscore(df, 'rerror_rate')
encode_numeric_zscore(df, 'srv_rerror_rate')
encode_numeric_zscore(df, 'same_srv_rate')
encode_numeric_zscore(df, 'diff_srv_rate')
encode_numeric_zscore(df, 'srv_diff_host_rate')
encode_numeric_zscore(df, 'dst_host_count')
encode_numeric_zscore(df, 'dst_host_srv_count')
encode_numeric_zscore(df, 'dst_host_same_srv_rate')
encode_numeric_zscore(df, 'dst_host_diff_srv_rate')
encode_numeric_zscore(df, 'dst_host_same_src_port_rate')
encode_numeric_zscore(df, 'dst_host_srv_diff_host_rate')
encode_numeric_zscore(df, 'dst_host_serror_rate')
encode_numeric_zscore(df, 'dst_host_srv_serror_rate')
encode_numeric_zscore(df, 'dst_host_rerror_rate')
encode_numeric_zscore(df, 'dst_host_srv_rerror_rate')


df.dropna(inplace=True,axis=1)
df[0:5]

xcolumns = df.columns.drop('outcome')
x = df[xcolumns].values
dummy = pd.get_dummies(df['outcome'])
outcomes = dummy.columns
outcomelen = len(outcomes)
y = dummy.values

df.groupby('outcome')['outcome'].count()

model = Sequential()
model.add(Dense(10, input_dim = x.shape[1],kernel_initializer='normal', activation = 'relu'))
model.add(Dense(50, input_dim = x.shape[1],kernel_initializer='normal', activation = 'relu'))
model.add(Dense(10, input_dim = x.shape[1],kernel_initializer='normal', activation = 'relu'))
model.add(Dense(1, kernel_initializer='normal'))
model.add(Dense(y.shape[1],activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')
monitor = EarlyStopping(monitor='val_loss', min_delta=1e-3, patience=5, verbose=1, mode='auto')
model.fit(xtrain,ytrain,validation_data=(xtest,ytest),callbacks=[monitor],verbose=2,epochs=10)


print('Learning Rate = ')
print(K.eval(model.optimizer.lr)) 
print('\n')

model.summary()


def confusion_matrix_func(ytest, y_test_pred):
    
    '''
    This function computes the confusion matrix using Predicted and Actual values and plots a confusion matrix heatmap
    '''
    C = confusion_matrix(ytest, y_test_pred)
    cm_df = pd.DataFrame(C)
    labels = ['back', 'butter_overflow', 'loadmodule', 'guess_passwd', 'imap', 'ipsweep', 'warezmaster', 'rootkit', 
'multihop', 'neptune', 'nmap', 'normal', 'phf', 'perl', 'pod', 'portsweep', 'ftp_write', 'satan', 'smurf', 'teardrop', 'warezclient', 'land']
    plt.figure(figsize=(20,15))
    sns.set(font_scale=1.4)
    sns.heatmap(cm_df, annot=True, annot_kws={"size":12}, fmt='g', xticklabels=labels, yticklabels=labels)
    plt.ylabel('Actual Class')
    plt.xlabel('Predicted Class')
    
    plt.show()
    




def multiclass_roc_auc_score(ytest, pred, average="macro"):
    lb = preprocessing.LabelBinarizer()
    lb.fit(ytest)
    ytest = lb.transform(ytest)
    pred = lb.transform(pred)
    return roc_auc_score(ytest, pred, average=average)
print('Train data')
print(xtrain.shape)
print(ytrain.shape)
print('\n')
print('Test data')
print(xtest.shape)
print(ytest.shape)
print('\n')


print('Predicting on the test data:')
start = dt.datetime.now()
escore = model.evaluate(xtest, ytest, batch_size=32)
pred = model.predict(xtest)
pred = np.argmax(pred,axis=1)
y_eval = np.argmax(ytest,axis=1)

vscore = metrics.accuracy_score(y_eval, pred)

rscore = recall_score(y_eval, pred, average='weighted')

ascore = precision_score(y_eval, pred, average='weighted')

f1score= f1_score(y_eval, pred, average='weighted') #F1 = 2 * (precision * recall) / (precision + recall) for manual

roc_auc_socre = multiclass_roc_auc_score(y_eval, pred)


print('Completed')
print(f'Time taken: {dt.datetime.now()-start}')

print(f'Validation score: {vscore}')

print(f'Evaluation score: {escore}')

print(f'Recall score: {rscore}')

print(f'Precision score: {ascore}')

print(f'F1 score: {f1score}')

print(f'ROC-AUC score: {roc_auc_socre}')


## confusion matrix
confusion_matrix_func(y_eval, pred)


# In[2]:





# In[3]:





# In[ ]:





# In[ ]:





# In[6]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




