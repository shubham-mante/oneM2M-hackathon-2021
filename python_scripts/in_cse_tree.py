from oneM2M_functions import *

if __name__ == "__main__":
    server = "http://127.0.0.1:8080"
    cse = "/~/in-cse/smart_campus/"

uri_cse = server + cse
"""
	Point of access (poa) : enter the access URL as per the point of access of the application
        FOr the testing purpose, we are using a basic HTTP server accepting notifications
"""


# create dashboard application entity
poa1 = 'http://127.0.0.1:1400/'
create_ae(uri_cse, 'AE_Dashboard', poa1, 'dashboard', data_format="json")


# create data-lake application entity
poa2 = 'http://127.0.0.1:1400/'
create_ae(uri_cse, 'AE_DataLake', poa2, 'data-lake', data_format="json")
