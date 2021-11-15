from oneM2M_functions import *

if __name__ == "__main__":
    server = "http://127.0.0.1:8181"
    cse = "/~/mn-cse1/academic_block"

uri_cse = server + cse


# create weather station application entity (AE_WS) and its respective containers. 

descriptor1  ="""<obj> <str name=\"Node ID\" val=\"Weather Station\"/> 
            <str name=\"Weather Node Location\" val=\"'Latitude': 11.222, 'Longitude': 22.333\"/>
            <str name=\"Device Model\" val=\"'Controller' : 'ESP8266', 'Sensors' : 'MH-Z14'\"/>
            <str name=\"Measuring Parameter\" val=\"CO2\"/>
            <str name=\"Measurement Sensor Parameters Description\" val=\"Data Description,{[ Units ], [ Resolution ], [ Accuracy ]\"/>
            <str name=\"CO2\" val=\"Instantaneous value of CO2 concentration, minimum value is 1 ppm and maximum value is 5000 ppm, [float] [ppb], [100 ppb], [± 15%] \"/> 
                       </obj>"""

create_ae(uri_cse, 'AE_WS', '', ['weather-station','academic_block'], data_format="json")
create_cnt(uri_cse + '/' + 'AE_WS', 'Descriptor', ['weather-station','academic_block', 'descriptor'], data_format="json")
create_cin(uri_cse +  '/' + 'AE_WS' + '/' + 'Descriptor', descriptor1, ['weather-station','academic_block', 'descriptor'], data_format="json")
create_cnt(uri_cse +  '/' + 'AE_WS', 'Data', ['weather-station','academic_block', 'data'], data_format="json")
    

# create air quality monitoring application entity (AE_WS) and its respective containers. 


descriptor2  ="""<obj> <str name=\"Node ID\" val=\"AQM Node\"/>
            <str name=\"AQM Node Location\" val=\"'Latitude': 11.222, 'Longitude': 22.333\"/>
            <str name=\"Device Model\" val=\"{'Controller': 'ESP8266', 'Device': 'AQ node with PM2.5, PM10, Temperature, CO2 concentration, 'Sensors': [ '(PM2.5 = SDS011, id=1.0)', '(PM10 = SDS011, id=1.0)', '(Temperature = DHT22, id=1.0)', '(CO2 concentration = MH-Z14']}\"/>
           <str name=\"Measuring Parameters\" val=\"['PM2.5', 'PM10', 'Temperature', 'CO2 concentration']\"/>
           <str name=\"Parameters Description\" val=\"Data Description, [datatype], [Units], [Resolution], [Accuracy]\"/>
           <str name=\"PM2.5\" val=\"Instantaneous value of PM2.5, maximum of &#0177; 15% of reading and &#0177; 10 ug/m3, [float], [ug/m3], [particle resolution 0.um and Mass Measurement resolution 0.1 ug/m3], [maximum of &#0177; 15% of reading and &#0177; 10 ug/m3]\"/>
           <str name=\"PM10\" val=\"Instantaneous value of PM10, minimum value is 0 ug/m3 and maximum value is 999.9 ug/m3, [float], [ug/m3], [particle resolution 0.um and Mass Measurement resolution 0.1 u/m3, maximum of &#0177; 15% of reading and &#0177; 10 ug/m3]\"/>
           <str name=\"Temperature\" val=\"Instantaneous value of Temperature, minimum value is -40 &#0176;C and maximum value is 80 &#0176;C, [float], [&#0176;C], [0.1 &#0176;C], [&#0177; 0.5 &#0176;C]\"/>
           <str name=\"CO2\" val=\"Instantaneous value of CO2 concentration, minimum value is 1 ppm and maximum value is 5000 ppm, [float] [ppb], [100 ppb], [± 15%] \"/>
                       </obj>"""

create_ae(uri_cse, 'AE_AQM', '', ['air-quality-monitoring','academic_block'], data_format="json")

create_cnt(uri_cse + '/' + 'AE_AQM', 'Floor_1', ['air-quality-monitoring','academic_block'], data_format="json")
create_cnt(uri_cse +  '/' + 'AE_AQM' + '/' + 'Floor_1', 'Room_1',  ['air-quality-monitoring','academic_block'], data_format="json")
create_cnt(uri_cse +  '/' + 'AE_AQM' + '/' + 'Floor_1' + '/' + 'Room_1', 'Descriptor',  ['air-quality-monitoring','academic_block'], data_format="json")
create_cin(uri_cse +  '/' + 'AE_AQM' + '/' + 'Floor_1' + '/' + 'Room_1' + '/' + 'Descriptor', descriptor2, ['air-quality-monitoring','academic_block', 'descriptor'], data_format="json")
create_flex_cnt(uri_cse +  '/' + 'AE_AQM' + '/' + 'Floor_1' + '/' + 'Room_1', 'Data',  ['air-quality-monitoring','academic_block'], data_format="json")
create_cnt(uri_cse +  '/' + 'AE_AQM' + '/' + 'Floor_1', 'Room_2',  ['air-quality-monitoring','academic_block'], data_format="json")
create_cnt(uri_cse +  '/' + 'AE_AQM' + '/' + 'Floor_1' + '/' + 'Room_2', 'Descriptor',  ['air-quality-monitoring','academic_block'], data_format="json")
create_cin(uri_cse +  '/' + 'AE_AQM' + '/' + 'Floor_1' + '/' + 'Room_2'+ '/' + 'Descriptor', descriptor2, ['air-quality-monitoring','academic_block', 'descriptor'], data_format="json")
create_flex_cnt(uri_cse +  '/' + 'AE_AQM' + '/' + 'Floor_1' + '/' + 'Room_2', 'Data',  ['air-quality-monitoring','academic_block'], data_format="json")

create_cnt(uri_cse + '/' + 'AE_AQM', 'Floor_2', ['air-quality-monitoring','academic_block'], data_format="json")
create_cnt(uri_cse +  '/' + 'AE_AQM' + '/' + 'Floor_2', 'Room_1',  ['air-quality-monitoring','academic_block'], data_format="json")
create_cnt(uri_cse +  '/' + 'AE_AQM' + '/' + 'Floor_2' + '/' + 'Room_1', 'Descriptor',  ['air-quality-monitoring','academic_block'], data_format="json")
create_cin(uri_cse +  '/' + 'AE_AQM' + '/' + 'Floor_2' + '/' + 'Room_1'+ '/' + 'Descriptor', descriptor2, ['air-quality-monitoring','academic_block', 'descriptor'], data_format="json")
create_flex_cnt(uri_cse +  '/' + 'AE_AQM' + '/' + 'Floor_2' + '/' + 'Room_1', 'Data',  ['air-quality-monitoring','academic_block'], data_format="json")
create_cnt(uri_cse +  '/' + 'AE_AQM' + '/' + 'Floor_2', 'Room_2',  ['air-quality-monitoring','academic_block'], data_format="json")
create_cnt(uri_cse +  '/' + 'AE_AQM' + '/' + 'Floor_2' + '/' + 'Room_2', 'Descriptor',  ['air-quality-monitoring','academic_block'], data_format="json")
create_cin(uri_cse +  '/' + 'AE_AQM' + '/' + 'Floor_2' + '/' + 'Room_2'+ '/' + 'Descriptor', descriptor2, ['air-quality-monitoring','academic_block', 'descriptor'], data_format="json")
create_flex_cnt(uri_cse +  '/' + 'AE_AQM' + '/' + 'Floor_2' + '/' + 'Room_2', 'Data',  ['air-quality-monitoring','academic_block'], data_format="json")



"""
	Point of access (poa) : enter the access URL as per the point of access of the application
	Ex. If the toggleLED application (AE_AW) running on ESP1 has IP = 123.234.345.456 then replace the 'poa' inside ae_list will be : http://123.234.345.456/. Similarly for exp2_ip. I Here, we have used a simple http server that acts as a listener.

"""
# create fire alarm application entity
poa1 = 'http://127.0.0.1:1400/' # change the poa value 
create_ae(uri_cse, 'AE_FA', poa1, ['fire-alarm-application','academic_block'], data_format="json")


# create automatic window application entity
poa2 = 'http://127.0.0.1:1400/'
create_ae(uri_cse, 'AE_AW', poa2, ['automatic-window-application','academic_block'], data_format="json")
