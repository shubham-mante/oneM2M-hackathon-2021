# oneM2M Resource Tree structure
We have created a decentralised IoT solution consisting of a central IN-CSE and 3 MN-CSEs. This type of architecture is easily scalable for large scale systems
such as Smart City and enables seamless interaction between heterogeneous applications independent of underlying communication technologies.

# Step-1: Clone the repository locally on your system
$ git clone https://github.com/shubham-mante/oneM2M-hackathon-2021.git

# Step-2: CSE registration 
* Go to oneM2M_platform directory
* To create the resource tree, first initialise the IN-CSE and then the three MN-CSEs by executing the "start.bat" script on Windows or "start.sh" on Linux and Mac OS. 
* Open the following URL in your browser and access the oneM2M platform web interface (IN-CSE): http://127.0.0.1:8080/webpage 
* ![in-cse1.png](https://github.com/shubham-mante/oneM2M-hackathon-2021/blob/main/Diagrams/in-cse1.png)

# Step-3: Resource creation under CSEs
* Go to python_scripts directory which contains all the necessary source codes to create the resource tree
* Install the "requests" and "json" modules (skip this step if already installed)
* Run in_cse_tree.py file to create the application entities under IN-CSE
![in-cse.png](https://github.com/shubham-mante/oneM2M-hackathon-2021/blob/main/Diagrams/in-cse.png)
* Run $ python3 mn_cse1_tree.py file to create the application entities under MN-CSE1
![academic-block.png](https://github.com/shubham-mante/oneM2M-hackathon-2021/blob/main/Diagrams/academic_block.png)
* Run $ python3 mn_cse2_tree.py file to create the application entities under MN-CSE2
![dining_hall.png](https://github.com/shubham-mante/oneM2M-hackathon-2021/blob/main/Diagrams/dining-hall.png)
* Run $ python3 mn_cse3_tree.py file to create the application entities under MN-CSE3
![isolation_ward](https://github.com/shubham-mante/oneM2M-hackathon-2021/blob/main/Diagrams/isolation_ward.png)
Note-1: New resources can be created under a CSE with the help of oneM2M_functions.py file.
Note-2: Labels are added to the resources which will be used during the **Discovery** based data retrieval.
Note-3: Containers are used to store the descriptor content instances which helps add meaning to the data users due to the provision of added semantics.
Note-4: Flex containers are used as data containers to provide flexible key-value pairs. 
![flex_cnt](https://github.com/shubham-mante/oneM2M-hackathon-2021/blbo/main/Diagrams/flex_cnt.png)

# Step-4: Start the Interworking Proxy Entity (IPE)
* An IPE is developed and integrated with the oneM2M platform for communication between a non-oneM2M device and oneM2M platform
* The IPE parses required value from a non-oneM2M data model and store it as a content instance as per oneM2M data model.
* non-oneM2M data model
![thingSpeak](https://github.com/shubham-mante/oneM2M-hackathon-2021/blob/main/Diagrams/thingSpeak.png)
* oneM2M data model storing CO value as a content instance
![ipe_om2m](https://github.com/shubham-mante/oneM2M-hackathon-2021/blob/main/Diagrams/ipe_om2m.png)
* To start the IPE (inside MN-CSE1 in this case), enter **start 49** in the MN-CSE1 terminal. A message **Starting Sample Ipe** will appear on the terminal.
* New content instances will be created under **Data** container of AE_WS as shown below
![WS_data](https://github.com/shubham-mante/oneM2M-hackathon-2021/blob/main/Diagrams/WS_data.png)
* To stop the IPE, enter **stop 49**
 
# Step-5: Update access control policies (ACPs) to allow read access to allowed application entities (AEs) and other applications with the help of ACP creation rule
![ACPs.png](https://github.com/shubham-mante/oneM2M-hackathon-2021/blob/main/Diagrams/ACPs.png)

* Run $ python3 update_acp_mn_cse1.py file to update the privilages of acp_admin of MN-CSE1
![update_acp_mn_cse1](https://github.com/shubham-mante/oneM2M-hackathon-2021/blob/main/Diagrams/update_acp_mn_cse1.png)

* Similarly, run $ python3 update_acp_mn_cse2.py file to update the privilages of acp_admin of MN-CSE2
* Similarly,  $ python3 update_acp_mn_cse3.py file to update the privilages of acp_admin of MN-CSE3

# Step-6: Start a listener server that accepts notification
* To test the setup, run the http_server.py ($ python3 http_server.py) file on the terminal. **INFO:root:Starting httpd...** message will appear on the terminal. This will initialize a simple listner server (http://127.0.0.1:1400/) that responds to notifications received from the oneM2M platform. 
* The listner is used as point of access (poa) of AEs during the testing phase. Later, the POA should be changed as per the application's poa.

# Step-7: Subscribe to the Data containers
* As the ACPs are updated previously, therefore only authorised applications can access the data
* Run $ python3 subscribe_mn_cse1.py file to create subscription resource under the data containers of MN-CSE1
* Subscription resource creation inside same CSE
![same_cse_subscription](https://github.com/shubham-mante/oneM2M-hackathon-2021/blob/main/Diagrams/cross_cse_subscription.png)
* Subscription resource creation for a AE hosted under remote CSE
![cross_cse_subscription](https://github.com/shubham-mante/oneM2M-hackathon-2021/blob/main/Diagrams/cross_cse_subscription.png)
* Similarly, run $ python3 subscribe_mn_cse2.py file to create subscription resource under the data containers of MN-CSE2
* Similarly, run $ python3 subscribe_mn_cse3.py file to create subscription resource under the data containers of MN-CSE3

Note: As, the http_server is used as listener for the validation of subscription resource creation, below message will appear on the server's terminal.
![subs_response1](https://github.com/shubham-mante/oneM2M-hackathon-2021/blob/main/Diagrams/subs_response1.png)
