from oneM2M_functions import *

if __name__ == "__main__":
    server = "http://127.0.0.1:8383"
    cse = "/~/mn-cse3/isolation_ward"

uri_cse = server + cse
    

# create crowd monitoring application entity (AE_CM) and its respective containers. 


descriptor1  ="""<obj> <str name=\"Node ID\" val=\"Crowd Monitoring Node\"/>
            <str name=\"Crowd Monitoring Node Location\" val=\"'Latitude': 11.222, 'Longitude': 22.333\"/>
            <str name=\"Device Model\" val=\"{'Controller': 'ESP8266', 'Device': 'Temperature, CO2 concentration, 'Sensors': ['(Temperature = DHT22, id=1.0)', '(CO2 concentration = MH-Z14']}\"/>
           <str name=\"Measuring Parameters\" val=\"['Temperature', 'CO2 concentration']\"/>
           <str name=\"Parameters Description\" val=\"Data Description, [datatype], [Units], [Resolution], [Accuracy]\"/>
           <str name=\"Temperature\" val=\"Instantaneous value of Temperature, minimum value is -40 &#0176;C and maximum value is 80 &#0176;C, [float], [&#0176;C], [0.1 &#0176;C], [&#0177; 0.5 &#0176;C]\"/>
           <str name=\"CO2\" val=\"Instantaneous value of CO2 concentration, minimum value is 1 ppm and maximum value is 5000 ppm, [float] [ppb], [100 ppb], [± 15%] \"/>
                       </obj>"""

create_ae(uri_cse, 'AE_CM', '', ['crowd-monitoring','isolation_ward'], data_format="json")

create_cnt(uri_cse + '/' + 'AE_CM', 'Floor_1', ['crowd-monitoring','isolation_ward'], data_format="json")
create_cnt(uri_cse +  '/' + 'AE_CM' + '/' + 'Floor_1', 'Descriptor',  ['crowd-monitoring','isolation_ward'], data_format="json")
create_cin(uri_cse +  '/' + 'AE_CM' + '/' + 'Floor_1' + '/' + 'Descriptor', descriptor1, ['crowd-monitoring','isolation_ward', 'descriptor'], data_format="json")
create_flex_cnt(uri_cse +  '/' + 'AE_CM' + '/' + 'Floor_1', 'Data',  ['crowd-monitoring','isolation_ward'], data_format="json")
create_cnt(uri_cse +  '/' + 'AE_CM' + '/' + 'Floor_1', 'Descriptor',  ['crowd-monitoring','isolation_ward'], data_format="json")
create_cin(uri_cse +  '/' + 'AE_CM' + '/' + 'Floor_1' + 'Descriptor', descriptor1, ['crowd-monitoring','isolation_ward', 'descriptor'], data_format="json")
create_flex_cnt(uri_cse +  '/' + 'AE_CM' + '/' + 'Floor_1', 'Data',  ['crowd-monitoring','isolation_ward'], data_format="json")


create_cnt(uri_cse + '/' + 'AE_CM', 'Floor_2', ['crowd-monitoring','isolation_ward'], data_format="json")
create_cnt(uri_cse +  '/' + 'AE_CM' + '/' + 'Floor_2', 'Descriptor',  ['crowd-monitoring','isolation_ward'], data_format="json")
create_cin(uri_cse +  '/' + 'AE_CM' + '/' + 'Floor_2' + '/' + 'Descriptor', descriptor1, ['crowd-monitoring','isolation_ward', 'descriptor'], data_format="json")
create_flex_cnt(uri_cse +  '/' + 'AE_CM' + '/' + 'Floor_2', 'Data',  ['crowd-monitoring','isolation_ward'], data_format="json")
create_cnt(uri_cse +  '/' + 'AE_CM' + '/' + 'Floor_2', 'Descriptor',  ['crowd-monitoring','isolation_ward'], data_format="json")
create_cin(uri_cse +  '/' + 'AE_CM' + '/' + 'Floor_2' + 'Descriptor', descriptor1, ['crowd-monitoring','isolation_ward', 'descriptor'], data_format="json")
create_flex_cnt(uri_cse +  '/' + 'AE_CM' + '/' + 'Floor_2', 'Data',  ['crowd-monitoring','isolation_ward'], data_format="json")



"""
	Point of access (poa) : enter the access URL as per the point of access of the application
	Ex. If the toggleLED application (AE_AW) running on ESP1 has IP = 123.234.345.456 then replace the 'poa' inside ae_list will be : http://123.234.345.456/toggleLED. Similarly for exp2_ip.

"""


# create automatic window application entity
poa1 = 'http://192.156.123.235/buzzer'
create_ae(uri_cse, 'AE_AS', poa1, ['alert-system-application','isolation_ward'], data_format="json")
