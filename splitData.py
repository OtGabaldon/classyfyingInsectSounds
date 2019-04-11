#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pydub import AudioSegment
import os
import numpy as np


# In[3]:


workingDir = os.getcwd()
for insect in ["cicada","cricket","katydid"]:
    print(insect)
    for file in os.listdir(os.path.join(workingDir,"InsectData",insect)):
        if(not os.path.isdir(os.path.join(workingDir,"InsectData",insect,file))):
            sound = AudioSegment.from_file(os.path.join(workingDir,"InsectData",insect,file))
            numSegments = len(sound)/5000
            for i in np.arange(int(numSegments)-1):
                segment = sound[i*5000:(i+1)*5000]
                segment.export(os.path.join(workingDir,"InsectData",insect,"split",str(i)+"_"+file),format="mp3")


# In[ ]:
