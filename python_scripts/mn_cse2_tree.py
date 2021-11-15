from oneM2M_functions import *

if __name__ == "__main__":
    server = "http://127.0.0.1:8282"
    cse = "/~/mn-cse2/dining_hall"

uri_cse = server + cse
    

# create crowd monitoring application entity (AE_CM) and its respective containers. 


descriptor1  ="""<obj> <str name=\"Node ID\" val=\"CO2 Monitoring Node\"/>
            <str name=\"CO2 Monitoring Node Location\" val=\"'Latitude': 11.222, 'Longitude': 22.333\"/>
            <str name=\"Device Model\" val=\"{'Controller': 'ESP8266', 'Device': 'CO2 concentration, 'Sensors': ['(CO2 concentration = MH-Z14']}\"/>
           <str name=\"Measuring Parameter\" val=\"['CO2 concentration']\"/>
           <str name=\"Parameters Description\" val=\"Data Description, [datatype], [Units], [Resolution], [Accuracy]\"/>
           <str name=\"CO2\" val=\"Instantaneous value of CO2 concentration, minimum value is 1 ppm and maximum value is 5000 ppm, [float] [ppb], [100 ppb], [± 15%] \"/>
                       </obj>"""

create_ae(uri_cse, 'AE_CO2', '', ['crowd-monitoring','isolation_ward'], data_format="json")

create_cnt(uri_cse + '/' + 'AE_CO2', 'Floor_1', ['co2-monitoring','dining_hall'], data_format="json")
create_cnt(uri_cse +  '/' + 'AE_CO2' + '/' + 'Floor_1', 'Descriptor',  ['co2-monitoring','dining_hall'], data_format="json")
create_cin(uri_cse +  '/' + 'AE_CO2' + '/' + 'Floor_1' + '/' + 'Descriptor', descriptor1, ['co2-monitoring','dining_hall', 'descriptor'], data_format="json")
create_flex_cnt(uri_cse +  '/' + 'AE_CO2' + '/' + 'Floor_1', 'Data',  ['co2-monitoring','dining_hall'], data_format="json")
create_cnt(uri_cse +  '/' + 'AE_CO2' + '/' + 'Floor_1', 'Descriptor',  ['co2-monitoring','dining_hall'], data_format="json")
create_cin(uri_cse +  '/' + 'AE_CO2' + '/' + 'Floor_1' + 'Descriptor', descriptor1, ['co2-monitoring','dining_hall', 'descriptor'], data_format="json")
create_flex_cnt(uri_cse +  '/' + 'AE_CO2' + '/' + 'Floor_1', 'Data',  ['co2-monitoring','dining_hall'], data_format="json")


create_cnt(uri_cse + '/' + 'AE_CO2', 'Floor_2', ['co2-monitoring','dining_hall'], data_format="json")
create_cnt(uri_cse +  '/' + 'AE_CO2' + '/' + 'Floor_2', 'Descriptor',  ['co2-monitoring','dining_hall'], data_format="json")
create_cin(uri_cse +  '/' + 'AE_CO2' + '/' + 'Floor_2' + '/' + 'Descriptor', descriptor1, ['co2-monitoring','dining_hall', 'descriptor'], data_format="json")
create_flex_cnt(uri_cse +  '/' + 'AE_CO2' + '/' + 'Floor_2', 'Data',  ['co2-monitoring','dining_hall'], data_format="json")
create_cnt(uri_cse +  '/' + 'AE_CO2' + '/' + 'Floor_2', 'Descriptor',  ['co2-monitoring','dining_hall'], data_format="json")
create_cin(uri_cse +  '/' + 'AE_CO2' + '/' + 'Floor_2' + 'Descriptor', descriptor1, ['co2-monitoring','dining_hall', 'descriptor'], data_format="json")
create_flex_cnt(uri_cse +  '/' + 'AE_CO2' + '/' + 'Floor_2', 'Data',  ['co2-monitoring','dining_hall'], data_format="json")



"""
	Point of access (poa) : enter the access URL as per the point of access of the application
	Ex. If the toggleLED application (AE_AS) running on ESP has IP = 123.234.345.456 then replace the 'poa' inside ae_list will be : http://123.234.345.456/toggleLED.

"""


# create automatic window application entity
poa1 = 'http://192.156.456.111/toggleLED'
create_ae(uri_cse, 'AE_AW', poa1, ['automatic-window-application','dining_hall'], data_format="json")
