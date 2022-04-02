#!/usr/bin/env python
# coding: utf-8

# In[114]:


import numpy as np
import time
from IPython.display import clear_output


# In[91]:


def initialize_env():
    env = np.zeros((3,4))
    env[1,1] = 25
    env[1,2] = -10
    env[2,3] = 10
    return env

def initialize_position(row, col, env):
    env[row, col] = 1
    return env

def action_space():
    return np.array([0,1,2,3])

def take_action(action, env, render=False):
    reward = 0
    done = False
    position = np.where(env==1)
    row_thres = env.shape[0]
    col_thres = env.shape[1]
    row_start = position[0][0]
    col_start = position[1][0]
    env[row_start][col_start] = 0
    
    row_end = row_start
    col_end = col_start
    
    if(action==0 or action=='kiri'):
        if(col_end-1 < 0):
            pass
        else:
            col_end = col_end-1
    
    if(action==1 or action=='kanan'):
        if(col_end+1 >= col_thres):
            pass
        else:
            col_end = col_end+1
            
    if(action==2 or action=='atas'):
        if(row_end-1 < 0):
            pass
        else:
            row_end = row_end - 1
            
    
    if(action==3 or action=='bawah'):
        if(row_end+1 >= row_thres):
            pass
        else:
            row_end = row_end+1
            
    if (env[row_end][col_end]==0):
        reward = -1
    elif (env[row_end][col_end] == -10):
        reward = -10
        done = True
    elif (env[row_end][col_end] == 10):
        reward = 10
        done = True
    elif (env[row_end][col_end]== 25):
        reward = 25
        done = True
    else:
        reward = -1
        
        
    env[row_end][col_end] = 1
    next_state = [row_end, col_end]
    if(render):
        print(env)
    
    return next_state, reward, done, env
            
    