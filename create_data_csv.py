# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 12:30:35 2023

@author: Uwei
"""

#%%
# import package
import pandas as pd

import glob
import os
# from pathlib import Path
#%%
# create image csv
# 創建三個資料集的csv
def data_csv(data_dir, dt_set_name):
    # 取得該路徑中，結尾為png的路徑
    img_path = glob.glob(data_dir + "*png") # *表示匹配的所有內容
    name = ["file_name"]
    data = pd.DataFrame(img_path, columns=name)
    data.to_csv(dt_set_name + "_data_name.csv", index=False)

data_csv("./train_data/", "train")
data_csv("./valid_data/", "valid")
data_csv("./test_data/", "test")
#%%
# create lable csv
# 定義標籤檔案
def data_label(csv, prefix_name, data_set_name):
    data = pd.read_csv(csv)
    
    # 取得圖檔名稱(刪除路徑只留圖檔名稱)
    file_names = list(data['file_name'])
    file_names_2=[]
    for i in file_names:
        if data_set_name == "train" or data_set_name == "valid":
            a = i[13:]
            file_names_2.append(a)
        else:
            b = i[12:]
            file_names_2.append(b)
    
    # 將空格改為下底線    
    for i in range(len(file_names_2)):
        if file_names_2[i].startswith("Viral Pneumonia"):
            file_names_2[i] = file_names_2[i].replace(" ","_")
            
    df = pd.DataFrame(columns = prefix_name)
    
    # 先將標籤符合的表示為1
    for i in prefix_name:
        for j in file_names_2:
            if j.startswith(i):
                df = df.append({i:1}, ignore_index=True)
    # 將其他不符合的(nan)填補為0
    df = df.fillna(0)
    file_names_2_df = pd.DataFrame(file_names_2, columns=["File_name"])
    df1 = pd.concat([file_names_2_df, df], axis=1)
    # return df
    df.to_csv(data_set_name + "_label.csv", index=False)
    df1.to_csv(data_set_name + "_image.csv", index=False)
#%%
# 獲得標籤檔案
prefix_n = ["COVID", "Lung_Opacity", "Normal", "Viral_Pneumonia"]
data_label("D:/10979104/碩論程式整理/data_csv/train_data_name.csv", prefix_n, "train")
data_label("D:/10979104/碩論程式整理/data_csv/valid_data_name.csv", prefix_n, "valid")
data_label("D:/10979104/碩論程式整理/data_csv/test_data_name.csv", prefix_n, "test")
