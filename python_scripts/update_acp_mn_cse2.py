#/usr/bin/env python
#coding: utf-8

# In[2]:


import requests
import json
from oneM2M_functions import *

session = requests.Session()
session.trust_env = False
##########################################################################################################

def update_acp(uri_acp, acr, data_format="json"):

    headers = {
        'X-M2M-Origin': 'admin:admin',
        'Content-type': 'application/{};ty=1'.format(data_format)}

    body = {
        "m2m:acp": {
		"pv": {
			"acr": acr,
			},
		"pvs": {
			"acr": {
				"acor": ["admin:admin"],
				"acop": "63"
				}
			}
     		   }
 	   }

    try:    
        response = requests.put(uri_acp, json=body, headers=headers)
    except TypeError:
        response = requests.put(uri_acp, data=json.dumps(body), headers=headers)

    print('Return code : {}'.format(response.status_code))
    print('Return Content : {}'.format(response.text))

###########################################################################################################


if __name__ == "__main__":
	pass
################################## TO CREATE New Access Control Policies ###############################################

ae_list = {
0:{'ae': "http://127.0.0.1:8080/~/in-cse/smart_campus/AE_Dashboard"},
1:{'ae': "http://127.0.0.1:8080/~/in-cse/smart_campus/AE_DataLake"},
2:{'ae': "http://127.0.0.1:8282/~/mn-cse2/dining_hall/AE_AW"}
}

ri_list = []
for i in range(3):
    ri = get_ri(ae_list[i]["ae"])
    ri_list.append(ri["m2m:ae"]["ri"])


acp_list  = [{"acor": ["admin:admin", "/in-cse"], "acop": "63"}, {"acor": "guest:guest", "acop": "34"}, {"acor": ri_list, "acop": "2"}]
acp_admin_ri = get_ri("http://127.0.0.1:8282/~/mn-cse2/dining_hall/acp_admin")
update_acp("http://127.0.0.1:8282/~"+ acp_admin_ri["m2m:acp"]["ri"], acp_list)




