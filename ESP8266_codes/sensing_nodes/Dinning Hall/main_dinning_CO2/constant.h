// pin for pwm reading
#define CO2_IN D6

// pin for uart reading
#define MH_Z19_RX D4  // D7
#define MH_Z19_TX D0  // D6


#define SDS25_INT D8
#define SDS10_INT D7

#define WIFI_SSID "Your-SSID"
#define WIFI_PASS "Your Password"

#define MAX_STRING_LEN 255

#define LED D5


/*
   OneM2M connection details
*/
#define CSE_IP      "Your-CSE-IP"
#define CSE_PORT    8282
#define HTTPS     true
#define FINGER_PRINT  "10 3D D5 4E B1 47 DB 4B 5C B0 89 08 41 A7 A4 14 87 10 7F E8"
#define OM2M_ORGIN    "abcd:abcd"
#define OM2M_MN       "/~/in-cse/dining_hall/"      // as per resourse treee structure
#define OM2M_AE       "AE_AQM/Floor_1"          //change the Floor according to your requirement

#define OM2M_DATA_CONT  "Data"
#define LBL   "Building_1"


/*
   Error Handling Codes
*/
#define E_OM2M_NW -101
#define E_OM2M_CONNECT -102
#define E_OM2M_CONNECTION -103
#define E_OM2M_NO_RESPONSE -104
#define E_OM2M_EMPTY_RESPONSE -105


/*
   Success Codes
*/
#define SUCCESS_OM2M 400
