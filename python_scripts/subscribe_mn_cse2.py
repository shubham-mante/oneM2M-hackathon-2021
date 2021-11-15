#/usr/bin/env python
#coding: utf-8

# In[2]:


import requests
import json
from oneM2M_functions import *

ae_list = {
0:{'ae': "http://127.0.0.1:8080/~/in-cse/smart_campus/AE_Dashboard"},
1:{'ae': "http://127.0.0.1:8080/~/in-cse/smart_campus/AE_DataLake"},
2:{'ae': "http://127.0.0.1:8282/~/mn-cse2/dining_hall/AE_AW"}
}

subs_rn_list = {
0: {'rn':'SUB_Dashboard'},
1: {'rn':'SUB_DataLake'},
2: {'rn':'SUB_AW'}
}
ri_list = []
for i in range(3):
    ri = get_ri(ae_list[i]["ae"])
    ri_list.append(ri["m2m:ae"]["ri"])



for i in range(3):
    create_subs("http://127.0.0.1:8282/~/mn-cse2/dining_hall/AE_CO2/Floor_1/Data/", subs_rn_list[i]["rn"], ri_list[i])
    create_subs("http://127.0.0.1:8282/~/mn-cse2/dining_hall/AE_CO2/Floor_2/Data/", subs_rn_list[i]["rn"], ri_list[i])



if __name__ == "__main__":
	pass
