# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 14:23:54 2022

@author: Uwei
"""
#%%
    # import package
import glob
import os

import random

import shutil
from shutil import  copy2
#%%
# 數據來源與分割資料夾路徑設定
train_dir = "D:/10979104/碩論程式整理/train_data"
valid_dir = "D:/10979104/碩論程式整理/valid_data"
test_dir = "D:/10979104/碩論程式整理/test_data"
d_path = "D:/10979104/Thesis/Database/image"
#%%
    #修改檔案名稱(Viral Pneumonia -> Viral_Pneumonia)
images = glob.glob(d_path + "/Viral_Pneumonia/*")
n = 1
for i in images:
    os.rename(i, f'{d_path}/Viral_Pneumonia/Viral_Pneumonia-{n:01d}.png')
    n = n+1
    
#%%
# 資料分割 (訓練集、測試集)
def data_split(path):
    floder = os.listdir(path)
    for i in floder:
        floder_name = path
        d_dir = os.path.join(floder_name, i)
        trainfiles = os.listdir(d_dir) # 計算資料筆數與標籤
        num_train = 1300 # 需要的資料總筆數
        print("num : " + str(num_train))
        index_list = list(range(num_train)) # 資料標籤數量
        num = 0
        random.shuffle(index_list) # 隨機打亂資料
        for i in index_list:
            filename = os.path.join(d_dir, trainfiles[i])
            if num < num_train*0.8:
                print(str(filename))
                copy2(filename, train_dir)
            else:
                print(str(filename))
                copy2(filename, test_dir)
            # print(num)
            num += 1
#%%
#　data分割
data = data_split(d_path)
#%%
# 檢查分割後圖片總數
print(len(os.listdir(train_dir)))
print(len(os.listdir(test_dir)))
#%%
# 刪除檔案
def data_delete(path):
    file_name = os.listdir(path)
    for i in file_name:
        file = os.path.join(path, i)
        os.unlink(file)
            
data_delete(train_dir)
data_delete(test_dir)     
data_delete(valid_dir)   
#%%
# 定義項目資料夾中檔案名稱
def get_filenames_by_prefix(source_dir, prefix_name):
    #source_dir:獲取所有文件名子。 prefix_name:具有特定文件名的文件處理出來
    all_files = os.listdir(source_dir) #獲取所有文件名
    results = []
    for filename in all_files: #對每個文件做判斷
        if filename.startswith(prefix_name):
            #判斷方式為startwith,若他的開頭為prefix_name則添加到results裡面
            results.append(os.path.join(source_dir, filename))
            #核對他的source_dir添加他的數據
    return results
#%%
#取得項目資料夾檔案名稱
COVID_filenames = get_filenames_by_prefix(train_dir, "COVID")
Lung_Opacity_filenames = get_filenames_by_prefix(train_dir, "Lung_Opacity")
Normal_filenames = get_filenames_by_prefix(train_dir, "Normal")
Viral_Pneumonia_filenames = get_filenames_by_prefix(train_dir, "Viral_Pneumonia")
#%%
# import pprint
# pprint.pprint(COVID_filenames)
# pprint.pprint(Lung_Opacity_filenames)
# pprint.pprint(Normal_filenames)
# pprint.pprint(Viral_Pneumonia_filenames)
#%%
# 定義valid資料
def valid_split(get_filename):
    random.shuffle(get_filename)
    num = 0
    num_train = len(get_filename)
    index_list = list(range(num_train))
    for i in index_list:
        fileName = os.path.join(train_dir, get_filename[i])
        if num < num_train * 0.2:
            print(str(fileName))
            shutil.move(fileName, valid_dir)
        num += 1
#%%
# 取得valid資料
valid_split(COVID_filenames)
valid_split(Lung_Opacity_filenames)
valid_split(Normal_filenames)
valid_split(Viral_Pneumonia_filenames)
#%%
# 分割後各集資料數
print(len(os.listdir(train_dir)))
print(len(os.listdir(valid_dir)))
print(len(os.listdir(test_dir)))
