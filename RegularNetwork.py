#!/usr/bin/env python
# coding: utf-8

# In[8]:


import librosa
import librosa.display as display
import os
import pandas as pd
import librosa
import glob
import IPython.display as ipd
import numpy as np


# In[9]:


cicadas = []
crickets = []
katydids = []


# In[10]:


workingDir = os.getcwd()
for insect in ["cicada","cricket","katydid"]:
    for file in os.listdir(os.path.join(workingDir,"InsectData",insect,"split")):
        if(insect == "cicada"):
            cicadas.append(os.path.join(workingDir,"InsectData",insect,"split",file))
        elif(insect == "cricket"):
            crickets.append(os.path.join(workingDir,"InsectData",insect,"split",file))
        else:
            katydids.append(os.path.join(workingDir,"InsectData",insect,"split",file))


# In[11]:


X = []
Y = []
for i,cicada in enumerate(cicadas):
    x,sample_rate = librosa.load(cicada)
    y = [1,0,0]
    mfcc = np.mean(librosa.feature.mfcc(y=x,sr=sample_rate,n_mfcc=40).T,axis=0)
    X.append(mfcc)
    Y.append(y)
for i,cricket in enumerate(crickets):
    x,sample_rate = librosa.load(cricket)
    y = [0,1,0]
    mfcc = np.mean(librosa.feature.mfcc(y=x,sr=sample_rate,n_mfcc=40).T,axis=0)
    X.append(mfcc)
    Y.append(y)
for i,katydid in enumerate(katydids):
    x,sample_rate = librosa.load(katydid)
    y = [0,0,1]
    mfcc = np.mean(librosa.feature.mfcc(y=x,sr=sample_rate,n_mfcc=40).T,axis=0)
    X.append(mfcc)
    Y.append(y)


# In[124]:

xVector = np.array(X)
yVector = np.array(Y)
indices = np.random.permutation(447)
trainPerm = indices[:300]
testPerm = indices[301:]
xVectorTrain = xVector[trainPerm]
yVectorTrain = yVector[trainPerm]

xVectorTest = xVector[testPerm]
yVectorTest = yVector[testPerm]

# In[125]:


import keras
from keras.models import Sequential
from keras.layers import Dense,Activation,Flatten
from keras.optimizers import Adam


# In[126]:


keras.backend.clear_session()
model = Sequential()


# In[127]:


model.add(Dense(128, input_shape=(40,)))
model.add(Activation('relu'))
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dense(3))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',metrics=['accuracy'],optimizer='adam')


# In[128]:


output = model.fit(xVectorTrain,yVectorTrain,epochs=100)
print("OUTPUT:", output)

# In[123]:


loss,acc = model.evaluate(xVectorTest,yVectorTest, verbose=1)
print("LOSS:", loss)
print("ACCURACY:", acc)

# In[ ]:
