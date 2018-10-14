import numpy as np
from bs4 import BeautifulSoup
# _*_ coding: utf-8 _*_

#-----------------------------------Ex1.1-------------------------------------#
list1 = np.array([1,2,3,4])
list_M = np.square(list1)
#-----------------------------------Ex1.2-------------------------------------#
list = [1,2,3,4.0]
def function_return_interger(arr):
    arr_new =[]
    for i  in range(len(arr)):
        if (type(arr[i])==int):
            arr_new.append(arr[i])
    return arr_new
print(function_return_interger(list))
#-----------------------------------Ex1.3-------------------------------------#
f = open("file2read",'r')
list = []
for line in f:
    list = [int(x) for x in line.split()]
print(list)
#-----------------------------------Ex2.1-------------------------------------#
## for b = 1
Mg = np.array  ([[0  ,0  ,0  ,1  ,0  ,1  ],
                 [1/2,0  ,0  ,0  ,0  ,0  ],
                 [0  ,1  ,0  ,0  ,0  ,0  ],
                 [0  ,0  ,1  ,0  ,0  ,0  ],
                 [1/2,0  ,0  ,0  ,0  ,0  ],
                 [0  ,0  ,0  ,0  ,1  ,0  ]])
r = np.array([1/6,1/6,1/6,1/6,1/6,1/6]).transpose()
for i in range(200):
    r_old = r
    r = np.dot(Mg,r)
    r_diff = r-r_old
    r_diff_abs = np.abs(r_diff)
    if (sum(r_diff_abs)<1e-5):
        print(r)
        break
## for b =0.8
Mg = np.array  ([[0  ,0  ,0  ,1  ,0  ,1  ],
                 [1/2,0  ,0  ,0  ,0  ,0  ],
                 [0  ,1  ,0  ,0  ,0  ,0  ],
                 [0  ,0  ,1  ,0  ,0  ,0  ],
                 [1/2,0  ,0  ,0  ,0  ,0  ],
                 [0  ,0  ,0  ,0  ,1  ,0  ]])
r = np.array([1/6,1/6,1/6,1/6,1/6,1/6]).transpose()
b = 0.8
for i in range(200):
    r_old = r
    r = np.dot(Mg,r)*b+(1-b)*1/len(r)
    r_diff = r-r_old
    r_diff_abs = np.abs(r_diff)
    if (sum(r_diff_abs)<1e-5):
        print(r)
        break
#-----------------------------------Ex2.2-------------------------------------#
import os
i = 0
list_all =[]
dict = {}
for path in os.listdir('./toyset'):
    print(path)
    with open('./toyset/'+path,'rb') as wb_data:
        Soup = BeautifulSoup(wb_data,"html.parser")
    list_html = []
    list_html.append(path)
    if (path not in dict.keys()):
        dict.setdefault(path,i)
        i=i+1
    for k in Soup.find_all('a'):
        website = k.get('href')
        if (website):
            list_html.append(website)
            if (website not in dict.keys()):
                dict.setdefault(website,i)
                i=i+1

    print('list_html   ',list_html)
    list_all.append(list_html)
print('list_all \n',list_all)
len_dict=len(dict)
print('len of dic',len_dict)
print('dic ',dict)

#create an array with the dimension lenth_set^2
array_empty = np.zeros(shape=[len_dict,len_dict])
print(array_empty)

for a in range(len_dict):
    len_ligne = len(set(list_all[a]))
    for key in set(list_all[a]):
        array_empty[a,dict[key]] = 1/len_ligne
    print(array_empty[a])
    print('sum ', sum(array_empty[a]))
vect = []
for k in range(len_dict):
    vect.append(1/len_dict)
vect = np.array(vect).transpose()
array_empty = np.transpose(array_empty)
for i in range(50):
    vect_old = vect
    vect = np.dot(array_empty,vect)
    diff = vect - vect_old
    if (sum(abs(diff))<1e-5):
        break
print('vect is : ',vect)
np.set_printoptions(threshold=np.inf)
print('matrix  MG : \n', array_empty)
print('the sum is :',sum(vect))
#-----------------------------------Ex2.3-------------------------------------#








#-----------------------------------Ex2.4-------------------------------------#
#略