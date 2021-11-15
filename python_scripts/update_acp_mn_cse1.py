#/usr/bin/env python
#coding: utf-8

# In[2]:


import requests
import json
from oneM2M_functions import *


################################## TO CREATE New Access Control Policies ###############################################

ae_list = {
0:{'ae': "http://127.0.0.1:8080/~/in-cse/smart_campus/AE_Dashboard"},
1:{'ae': "http://127.0.0.1:8080/~/in-cse/smart_campus/AE_DataLake"},
2:{'ae': "http://127.0.0.1:8181/~/mn-cse1/academic_block/AE_FA"},
3:{'ae': "http://127.0.0.1:8181/~/mn-cse1/academic_block/AE_AW"},
}

ri_list = []
for i in range(4):
    ri = get_ri(ae_list[i]["ae"])
    ri_list.append(ri["m2m:ae"]["ri"])


acp_list  = [{"acor": ["admin:admin", "/in-cse"], "acop": "63"}, {"acor": "guest:guest", "acop": "34"}, {"acor": ri_list, "acop": "2"}, {"acor": "test_acp:test_acp", "acop": "18"}]
acp_admin_ri = get_ri("http://127.0.0.1:8181/~/mn-cse1/academic_block/acp_admin")
update_acp("http://127.0.0.1:8181/~"+ acp_admin_ri["m2m:acp"]["ri"], acp_list)




if __name__ == "__main__":
	pass
