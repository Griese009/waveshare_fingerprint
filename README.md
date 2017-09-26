# Waveshare_Fingerprint-Sensor
I had written a Python script for the UART Fingerprint-Sensor from Waveshare, because of a school project but also it is not supported by python.
First of all I had studied with my friend the datasheet of the sensor and the python package serial how we can build up a connection to it. After that I had begun to programm the code for a Windows system at the USB-port "COM1", later I implemented natuarally some more ports like "COM2" to "COM9" and for linux "ttyUSB0" to "ttyUSB8".
Now the code can handle all primary commands like adding and deliting (all and specific ones) fingerprints also the script can acquire a fingerprint and read the privileges number but at the end you are deciding for which purpose the privilege number is used.
# GUI
As I finished the main script i begun to wirte a GUI which can handle some input like the user-ID it can also convert it into two hex-numbers and you can decide the privilege number for a new fingerprint. Afterall I only implemented the main commands.
# Commands
First of all import the script and then u can call the following commands with this method "app.Reader().send_command(command=command, user=None, privilege=None) but replace these place holders (ps: Id do not recommend to go further than 255 (at user ID) because there is a bug which I had not fixed yet and prvilege id is from 1 to 3):
* user_amount
* ask_1_to_N
* asl_1_to_1 (user_id must be set)
* delete_all
* delete_user (user_id must be set)
* add_user (user_id and privilege must be set)
* acquire_privilege (user_id must be set)
* examples:
  * app.Reader().send_command(command="ask_1_to_1", user=[0x00, 0x01]) (here you are asking if the sensor has a user at user id 1 and if True he tries to acquire the fingerprint)
  * app.Reader().send_command(command="add_user", user=[0x01, 0x00], privileges=0x02) (here you are adding a user with the ID 256 and gives him the privilege number 2)<return><return>

-----------------------------------------------------------------------------------------------------------------------------------------
# Requiremets
Code Written in Python 3.6.2                                                                                                         
Needed Packages/ Hardware:                                                                                                                 
* pyserial
* UART to USB Adapter
* the UART Waveshare Sensor
