#Import library yang dibutuhkan
import numpy as np
import time


def initialize_env():
    """
    Inisilisasi Environment. Pada Game Robot Orbit environmentnya berbentuk sebuah matriks 3*4
    Dimana pada titik-titik tertentu terdapat harta karun dan api neraka
    
    ======Return======
    :return env: (array 2D) environment yang sudah dilakukan modifkasi
    """
    
    env = np.zeros((3,4))
    env[1,1] = 25
    env[1,2] = -10
    env[2,3] = 10
    return env

def initialize_position(row, col, env):
    """
    Inisilisasi Posisi Agent. Fungsi ini bertujuan untuk menginisialisasi posis agent pada awal permainan
    ======Parameter======
    :param row: (int) baris dimana agent memulai permainan
    :param col: (int) kolom dimana agent akan memulai permainan
    :param env: (array 2D) envinronment yg agent pakai
    
    ======Return======
    :return env: (array 2D) environment yang sudah dilakukan modifkasi
    """
    
    env[row, col] = 1
    return env

def action_space():
    """
    Fungsi ini akan mengembalikan action apa saja yang tersedia pada permainan robot orbit
    ======Return======
    :return array([0,1,2,3]): (array 1D) Kumpulan action yang dapat dieksekusi pada game ini
    """
    return np.array([0,1,2,3])

def take_action(action, env, render=False):
    """
    Fungsi ini bertujuan untuk mengambil action pada environment dan mengembalikan 
    ======Parameter======
    :param action: (int) action yang akan dieksekusi
    :param env: (array 2D) envinronment yg agent pakai
    :param render: (bool : default = False) Jika True akan menampilkan proses pengambilan action, Jika False sebaliknya
    
    ======Return======
    :return next_state : (array 1D) state selanjutnya
    :return reward : (int) reward yang didapatkan ketika sebuah action dieksekusi
    :return done: (bool) Jika bernilai True maka artinya agent sudah sampe terminate state, Jika False sebaliknya
    """
    rewards = 0
    done = False
    position = np.where(env==1)
    row_thres = env.shape[0]
    col_thres = env.shape[1]
    row_start = position[0][0]
    col_start = position[1][0]
    env[row_start][col_start] = 0

    row_end = row_start
    col_end = col_start

    #Take Action Kiri
    if(action==0):
        if(col_end-1 < 0):
            pass
        else:
            col_end = col_end-1

    #Take Action Kanan
    elif(action==1):
        if(col_end+1 >= col_thres):
            pass
        else:
            col_end = col_end+1

    #Take Action Atas
    elif(action==2):
        if(row_end-1 < 0):
            pass
        else:
            row_end = row_end - 1

    #Take Action Bawah
    elif(action==3):
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

    