#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from environment import robot_env
import random
import time
import os


# In[2]:


#inisialisasi hyperparameter
num_episodes = 1000
max_steps_per_episode = 100

learning_rate = 0.1
discount_rate = 0.99

epsilon = 1
max_epsilon = 1
min_epsilon = 0.1
epsilon_decay_rate = 0.1

#Change to true if you want render training process
render = False
#Membuat Environment
env = robot_env.initialize_env()

#menginisialisasi posisi robot pertama kali (row_start, row_end, env)
env = robot_env.initialize_position(0, 0, env)

#Membuat array yang berisikan action apa saja yang bisa diambil
actions = robot_env.action_space()
# kiri = 0, kanan = 1, atas = 2, bawah = 3

#Initiaslisasi Q-Table
q_table = np.zeros((env.size, actions.size))

#inisialisasi reward
#Reward :
#Empty = -1
#Fire = -10
#2 Harta = +25
#1 Harta = +10
reward_all_episode = []


# In[3]:


def choose_action(epsilon, state):
    random_num = random.uniform(0, 1)
    if (random_num < epsilon):
        action = np.random.choice(actions, 1)[0]
        
    else:
        index_state = state[0] + (state[0]*3) + state[1]
        action = np.argmax(q_table[index_state, :])
       
    return action

def update_q_table(state_, new_state):
    index_state = state_[0] + (state_[0]*3) + state_[1]
    index_new_state = new_state[0] + (new_state[0]*3) + new_state[1]
    
    
    q_table[index_state, action] = q_table[index_state, action] + (learning_rate * (reward + (discount_rate * np.max(q_table[index_new_state, :]) - q_table[index_state, action])))


# In[4]:


for episode in range(num_episodes):
    env = robot_env.initialize_env()
    env = robot_env.initialize_position(0, 0, env)
    state = (0,0)
    done = False
    rewards_current_episode = 0
    
    for step in range(max_steps_per_episode):
        #choose action  (epislon greedy)
        action = choose_action(epsilon, state)
        #take action and get reward and next state
        new_state, reward, done, env = robot_env.take_action(action, env, render)
        if render :
            time.sleep(0.1)
            os.system('cls')

        #update q table
        update_q_table(state, new_state)
        #change current state
        state = new_state
        rewards_current_episode += reward 
        
        #check if already on termination state
        if done:
            break
       
    
    # Exploration rate decay
    epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-epsilon_decay_rate*episode)
    
    #Add current episode reward to all episode reward
    reward_all_episode.append(rewards_current_episode)


# In[5]:



# In[6]:


def play_with_optimal_q_table():
    done = False
    env = robot_env.initialize_env()
    env = robot_env.initialize_position(0, 0, env)
    state = (0,0)
    rewards_current_episode = 0
    print(env)
    print("Envinronemnt Awal")
    time.sleep(3)
    os.system('cls')
    while(not done):
        index_state = state[0] + (state[0]*3) + state[1]
        action = np.argmax(q_table[index_state, :])
        new_state, reward, done, env = robot_env.take_action(action, env, True)
        print(f"Take Action {action}")
        print("Action : \n0 = Kiri 1 = Kanan 2 = Atas 3 = Bawah")
        time.sleep(3)
        os.system('cls')
        state = new_state
        rewards_current_episode += reward 
        if(state == [1,1] or state == [1,2] or state == [2,3]):
            done = True
            print("Win!")
            


# In[8]:


play_with_optimal_q_table()
print("Optimal Q Table : \n", q_table)




# In[ ]:




