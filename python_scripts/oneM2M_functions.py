# coding=utf-8

import requests
import json
import time


def create_ae(uri_cse, ae_name, poa, ae_labels="", data_format="json"):
    """
        Method description:
        Create an application entity(AE) inside the OneM2M framework/tree
        under the specified CSE

        Parameters:
        uri_cse : [str] URI of parent CSE
        ae_name : [str] name of the AE
        data_format : [str] payload format
    """
    headers = {
        'X-M2M-Origin': 'admin:admin',
        'Content-type': 'application/{};ty=2'.format(data_format)}
    
    body = {
        "m2m:ae": {
            "rn": "{}".format(ae_name),
            "api": "app-id",
            "poa": poa,
            "rr": "true", #resource reachable from CSE
            "lbl": ae_labels
        }
    }

    try:
        response = requests.post(uri_cse, json=body, headers=headers)
    except TypeError:
        response = requests.post(uri_cse, data=json.dumps(body), headers=headers)
    print('Return code : {}'.format(response.status_code))
    print('Return Content : {}'.format(response.text))
    return

def create_cnt(uri_ae, cnt_name, cnt_labels="", data_format="json"):
    """
        Method description:
        Creates a container(CON) in the OneM2M framework/tree
        under the specified AE

        Parameters:
        uri_ae : [str] URI for the parent AE
        cnt_name : [str] name of the container (DESCRIPTOR/DATA)
        data_format : [str] body format
    """

    headers = {
        'X-M2M-Origin': 'admin:admin',
        'Content-type': 'application/{};ty=3'.format(data_format)}

    body = {
        "m2m:cnt": {
            "rn": "{}".format(cnt_name),
            "mni": 100000,
            "lbl": cnt_labels
        }
    }

    try:    
        response = requests.post(uri_ae, json=body, headers=headers)
    except TypeError:
        response = requests.post(uri_ae, data=json.dumps(body), headers=headers)

    print('Return code : {}'.format(response.status_code))
    print('Return Content : {}'.format(response.text))

def create_flex_cnt(uri_ae, cnt_name, cnt_labels="", data_format="json"):
    """
        Method description:
        Creates a flex container(fcnt) in the OneM2M framework/tree
        under the specified AE

        Parameters:
        uri_ae : [str] URI for the parent AE
        cnt_name : [str] name of the container (DATA)
        data_format : [str] body format
    """

    headers = {
        'X-M2M-Origin': 'admin:admin',
        'Content-type': 'application/{};ty=28'.format(data_format)}

    body = {
        "m2m:fcnt": {
            "rn": "{}".format(cnt_name),
            "cnd": "org.eclipse.om2m.mydef",
            "lbl": cnt_labels
        }
    }

    try:    
        response = requests.post(uri_ae, json=body, headers=headers)
    except TypeError:
        response = requests.post(uri_ae, data=json.dumps(body), headers=headers)

    print('Return code : {}'.format(response.status_code))
    print('Return Content : {}'.format(response.text))

def create_subs(uri_cnt, rn, ri, data_format="json"):
    """
        Method description:
        create a content instance inside a container

        Parameters:
        uri_cse : [str] URI of parent CSE
        fmt_ex : [str] payload format
    """
    headers = {
        'X-M2M-Origin': 'admin:admin',
        'Content-type': 'application/{};ty=23'.format(data_format)}

    body = {
        "m2m:sub": {
            "rn": rn,
            "nu": ri,
            "nct": 2
        }
    }
    
    try:
        response = requests.post(uri_cnt, json=body, headers=headers)
    except TypeError:
        response = requests.post(uri_cnt, data=json.dumps(body), headers=headers)
    print('Return code : {}'.format(response.status_code))
    print('Return Content : {}'.format(response.text))


def create_group(uri_cse, group_name, uri_list):
    """
        Method description:
        Creates an AE that groups various other specifies AEs in the OneM2M framework/tree
        under the specified DATA CON

        Parameters:
        uri : [str] URI for the parent DATA CON appended by "la" or "ol"
        fmt_ex : [str] payload format (json/XML)
    """

    headers = {
        'X-M2M-Origin': 'admin:admin',
        'Content-type': 'application/json;ty=9'
    }

    payload = {
        "m2m:grp":
            {
                "rn": group_name,
                "mt": 3,
                "mid": uri_list,
                "mnm": 10
            }
    }

    try:
        response = requests.post(uri_cse, json=payload, headers=headers)
    except TypeError:
        response = requests.post(uri_cse, data=json.dumps(payload), headers=headers)

    print('Return code : {}'.format(response.status_code))
    print('Return Content : {}'.format(response.text))

def create_cin(uri_cnt, value, cin_labels="", data_format="json"):
    """
        Method description:
        Deletes/Unregisters an application entity(AE) from the OneM2M framework/tree
        under the specified CSE

        Parameters:
        uri_cse : [str] URI of parent CSE
        ae_name : [str] name of the AE
        fmt_ex : [str] payload format
    """
    headers = {
        'X-M2M-Origin': 'admin:admin',
        'Content-type': 'application/{};ty=4'.format(data_format)}

    body = {
        "m2m:cin": {
            "con": "{}".format(value),
            "lbl": cin_labels,
            "cnf": "text"
        }
    }
    
    try:
        response = requests.post(uri_cnt, json=body, headers=headers)
    except TypeError:
        response = requests.post(uri_cnt, data=json.dumps(body), headers=headers)
    print('Return code : {}'.format(response.status_code))
    print('Return Content : {}'.format(response.text))





################################################# Data retrieval #########################################################

def get_data(uri, data_format="json"):
    """
        Method description:
        Deletes/Unregisters an application entity(AE) from the OneM2M framework/tree
        under the specified CSE

        Parameters:
        uri_cse : [str] URI of parent CSE
        ae_name : [str] name of the AE
        fmt_ex : [str] payload format
    """
    headers = {
        'X-M2M-Origin': 'admin:admin',
        'Content-type': 'application/{}'.format(data_format)}

    response = requests.get(uri, headers=headers)
    print('Return code : {}'.format(response.status_code))
    print('Return Content : {}'.format(response.text))
    _resp = json.loads(response.text)
    return response.status_code, _resp["m2m:cin"]["con"] ## To get latest (entered data) instance
    #return response.status_code, _resp["m2m:cnt"]#["con"] ## to get whole data of container
    
def get_group_data(uri, data_format="json"):
    """
        Method description:
        Deletes/Unregisters an application entity(AE) from the OneM2M framework/tree
        under the specified CSE

        Parameters:
        uri_cse : [str] URI of parent CSE
        ae_name : [str] name of the AE
        fmt_ex : [str] payload format
    """
    headers = {
        'X-M2M-Origin': 'admin:admin',
        'Content-type': 'application/{}'.format(data_format)}

    response = requests.get(uri, headers=headers)
    print('Return code : {}'.format(response.status_code))
    print('Return Content : {}'.format(response.text))
    _resp = json.loads(response.text)
    return response.status_code, _resp["m2m:grp"]["lt"] ## To get latest (entered data) instance
	
def get_filtered_uri(uri, filter=""):
    """
        Method description:
        Splits the string into a list of URIs

        Parameters:
        uri : [str] URI for the parent DATA CON appended by "la" or "ol"
        fmt_ex : [str] payload format (json/XML)
    """
    _, filtered_uri = discovery(uri)
    filtered_uri_list = filtered_uri.split(" ")
    print(filtered_uri_list)
    return filtered_uri_list

def get_ri(uri, data_format="json"):
    """
        Method description:
        Deletes/Unregisters an application entity(AE) from the OneM2M framework/tree
        under the specified CSE

        Parameters:
        uri_cse : [str] URI of parent CSE
        ae_name : [str] name of the AE
        fmt_ex : [str] payload format
    """
    headers = {
        'X-M2M-Origin': 'admin:admin',
        'Content-type': 'application/{}'.format(data_format)}

    response = requests.get(uri, headers=headers)
    print('Return code : {}'.format(response.status_code))
    print('Return Content : {}'.format(response.text))
    _resp = json.loads(response.text)
    return _resp ## To get resource identifier
############################################# Delete a resource ##############################################################

def delete(uri, data_format="json"):
    """
        Method description:
        Deletes/Unregisters an application entity(AE) from the OneM2M framework/tree
        under the specified CSE

        Parameters:
        uri_cse : [str] URI of parent CSE
        ae_name : [str] name of the AE
        fmt_ex : [str] payload format
    """
    headers = {
        'X-M2M-Origin': 'admin:admin',
        'Content-type': 'application/{}'.format(data_format)}

    response = requests.delete(uri, headers=headers)
    print('Return code : {}'.format(response.status_code))
    print('Return Content : {}'.format(response.text))
    return

############################################## Data discovery #############################################################

def discovery(uri="", data_format="json"):
    """
        Method description:
        Deletes/Unregisters an application entity(AE) from the OneM2M framework/tree
        under the specified CSE

        Parameters:
        uri_cse : [str] URI of parent CSE
        ae_name : [str] name of the AE
        fmt_ex : [str] payload format
    """
    headers = {
        'X-M2M-Origin': 'admin:admin',
        'Content-type': 'application/{}'.format(data_format)}

    response = requests.delete(uri, headers=headers)
    print('Return code : {}'.format(response.status_code))
    print('Return Content : {}'.format(response.text))
    _resp = json.loads(response.text)
    return response.status_code, _resp["m2m:uril"]

############################################## Update Access Control Policies ############################################

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
# ====================================================



if __name__ == "__main__":
    server = "http://127.0.0.1:8080"

    cse = "/~/in-cse/in-name/"
