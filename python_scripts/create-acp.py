#/usr/bin/env python
#coding: utf-8

# In[2]:


import requests
import json
#import time

session = requests.Session()
session.trust_env = False
##########################################################################################################

def create_acp(uri_cse, rn, acr, data_format="json"):

    headers = {
        'X-M2M-Origin': 'admin:admin',
        'Content-type': 'application/{};ty=1'.format(data_format)}

    body = {
        "m2m:acp": {
		"rn": rn,
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
        response = requests.post(uri_cse, json=body, headers=headers)
    except TypeError:
        response = requests.post(uri_cse, data=json.dumps(body), headers=headers)

    print('Return code : {}'.format(response.status_code))
    print('Return Content : {}'.format(response.text))

###########################################################################################################


if __name__ == "__main__":
	pass
################################## TO CREATE New Access Control Policies ###############################################

server_list = {
0:{'server': "http://127.0.0.1:8080",'cse': "/~/in-cse/smart-campus"},
1:{'server': "http://127.0.0.1:8181",'cse': "/~/mn-cse1/academic_block"},
2:{'server': "http://127.0.0.1:8282",'cse': "/~/mn-cse2/dining_hall"},
3:{'server': "http://127.0.0.1:8383",'cse': "/~/mn-cse3/isolation_ward"},
}


acp_list  = [{"acor": ["admin:admin", "/in-cse"], "acop": "63"}, {"acor": "guest:guest", "acop": "34"}, {"acor": "test:test", "acop": "43"}]

for i in range(4):
    server =  server_list[i]['server']
    cse =  server_list[i]['cse']
    create_acp(server+cse,"acp_test",acp_list)




