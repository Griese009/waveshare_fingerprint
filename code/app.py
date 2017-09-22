import serial


class Reader:
    def __init__(self):
        self.port = ["COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM9", "ttyUSB0", "ttyUSB1",
                     "ttyUSB2", "ttyUSB3", "ttyUSB4", "ttyUSB5", "ttyUSB6", "ttyUSB7", "ttyUSB8"]
        self.baudrate = 19200
        self.bytemode = serial.EIGHTBITS
        self.ser = None
        self.befehle = {"user_amount": [0xF5,
                                        0x09,  # Command code
                                        0x00,  # Null
                                        0x00,  # Null
                                        0x00,  # Null
                                        0x00,  # Null
                                        0x09,  # CHK (Build up through Byte 2 to Byte 6 as a XOR-Operation)
                                        0xF5],
                        "ask_1_to_N": [0xF5,
                                       0x0C,  # Command code
                                       0x00,  # Null
                                       0x00,  # Null
                                       0x00,  # Null
                                       0x00,  # Null
                                       0x0C,  # CHK (Build up through Byte 2 to Byte 6 as a XOR-Operation)
                                       0xF5],
                        "ask_1_to_1": [0xF5,
                                       0x0B,  # Command code
                                       0x00,  # Nutzer_ID 1Byte
                                       0x00,  # Nutzer_ID 2Byte
                                       0x00,  # Null
                                       0x00,  # Null
                                       0x00,  # CHK
                                       0xF5],
                        "get_fingerprint": [0xF5, 0x24, 0x00, 0x00, 0x00, 0x00, 0x24, 0xF5],  # Not implemented yet
                        "delete_all": [0xF5, 0x05, 0x00, 0x00, 0x00, 0x00, 0x05, 0xF5],
                        "delete_user": [0xF5,
                                        0x04,  # Command code
                                        0x00,  # Nutzer_ID 1-Byte (hohe Zahl bsp. ID = 1000)
                                        0x00,  # Nutzer_ID 2-Byte (kleine Zahl, bsp. ID = 1)
                                        0x00,  # Null
                                        0x00,  # Null
                                        0x00,  # CHK
                                        0xF5],
                        "add_user": [[0xF5,
                                      0x01,  # Command code
                                      0x00,  # User-ID
                                      0x00,  # User-ID
                                      0x00,  # Privileges (0x01, 0x02, 0x03)
                                      0x00,  # Null
                                      0x00,  # CHK
                                      0xF5],
                                     [0xF5,
                                      0x02,  # Command code
                                      0x00,  # User-ID
                                      0x00,  # User-ID
                                      0x00,  # Privileges (0x01, 0x02, 0x03)
                                      0x00,  # Null
                                      0x00,  # CHK
                                      0xF5],
                                     [0xF5,
                                      0x03,  # Command code
                                      0x00,  # User-ID
                                      0x00,  # User-ID
                                      0x00,  # Privileges (0x01, 0x02, 0x03)
                                      0x00,  # Null
                                      0x00,  # CHK
                                      0xF5]],
                        "acquire_priviliege": [0xF5,
                                               0x0A,  # Command
                                               0x00,  # User-ID 1st Byte
                                               0x00,  # User-ID 2nd Byte
                                               0x00,  # None
                                               0x00,  # None
                                               0x00,  # CHK
                                               0xF5]}

    def open_connection(self):
        try:
            if self.ser is None:
                for port in self.port:  # just open the serial port if possible
                    try:
                        self.ser = serial.Serial(port=port, baudrate=self.baudrate, bytesize=self.bytemode)
                        return True
                    except Exception as e:
                        print(e)
            else:
                return True
        except Exception as e:
            print('Die verbindung konnte aufgrund von: "' + str(e) + '"  nicht geöffnet werden.')
            return False

    def close_connection(self):
        try:
            if self.ser is None:  # just closing the connection
                pass
            else:
                self.ser.close()
                self.ser = None
            return True
        except Exception as e:
            print('Die Verbindung konnte aufgrund von: "' + str(e) + '" nicht geschlossen werden.')
            return False

    def send_command(self, command, user=None, privileges=None):
        if user is None:  # adjust command for the sensor if not set
            user = [0x00, 0x00]
        else:
            pass

        if privileges is None:  # adjust command for the sensor if not set
            privileges = 0x00
        else:
            pass

        assert isinstance(privileges, int)  # controll values if these are correct
        assert isinstance(user[0], int)
        assert isinstance(user[1], int)
        assert isinstance(command, str)
        try:
            if command == "add_user":  # add_user is a special command
                for i in self.befehle[command]:
                    if self.ser is None:
                        self.open_connection()
                        a = i
                        self.ser.write([a[0], a[1], user[0], user[1], privileges, a[5],  # rebuild command
                                a[1] ^ user[0] ^ user[1] ^ privileges ^ a[5], a[7]])  # and do the XOR-Operation
                        if self.receive_data(command):
                            pass
                        else:
                            self.close_connection()
                            return False
                        self.close_connection()
                    else:
                        a = self.befehle[command]
                        self.ser.write([a[0], a[1], user[0], user[1], privileges, a[5],  # see previous comment
                                a[1] ^ user[0] ^ user[1] ^ privileges ^ a[5], a[7]])
                        if self.receive_data(command):
                            pass
                        else:
                            return False
            elif command == "acquire_priviliege":
                if self.ser is None:
                    self.open_connection()
                    a = self.befehle[command]
                    self.ser.write([a[0], a[1], user[0], user[1], privileges, a[5],  # see previous comment
                                a[1] ^ user[0] ^ user[1] ^ privileges ^ a[5], a[7]])
                    result = self.receive_data(command)
                    if result:
                        pass
                    else:
                        self.close_connection()
                        return False
                    self.close_connection()
                else:
                    a = self.befehle[command]
                    self.ser.write([a[0], a[1], user[0], user[1], privileges, a[5],  # see previous comment
                                a[1] ^ user[0] ^ user[1] ^ privileges ^ a[5], a[7]])
                    result = self.receive_data(command)
                    if result:
                        pass
                    else:
                        return False
                return result
            else:
                if self.ser is None:
                    self.open_connection()
                    a = self.befehle[command]
                    self.ser.write([a[0], a[1], user[0], user[1], privileges, a[5],  # see previous comment
                                a[1] ^ user[0] ^ user[1] ^ privileges ^ a[5], a[7]])
                    if self.receive_data(command):
                        pass
                    else:
                        self.close_connection()
                        return False
                    self.close_connection()
                else:
                    a = self.befehle[command]
                    self.ser.write([a[0], a[1], user[0], user[1], privileges, a[5],  # see previous comment
                                a[1] ^ user[0] ^ user[1] ^ privileges ^ a[5], a[7]])
                    if self.receive_data(command):
                        pass
                    else:
                        return False
            return True
        except Exception as e:
            print(e)
            return False

    def receive_data(self, command):
        assert isinstance(command, str)
        print(command)
        try:
            a = self.ser.read(8)  # receive data from sensor
            b = str(a).split("\\")  # reformat these data and split them
            if command != "acquire_priviliege" and command != "ask_1_to_N":
                if b[5] == "x00":  # Check if command was succesfull else return False
                    # the fifth byte shows if the command was successfull or not
                    pass
                elif b[5] == "x01" or b[5] == "x05" or b[5] == "x07" or b[5] == "x08" or b[5] == "x04":
                    if b[5] == "x01":
                        print("Operation failed")
                    elif b[5] == "x04":
                        print("Fingerprint database is full")
                    elif b[5] == "x05":
                        print("No such user")
                    elif b[5] == "x07":
                        print("User already exists")
                    elif b[5] == "x08":
                        print("Acquisition timeout")
                    return False
            elif command == "acquire_priviliege":
                if b[5] == "x01":
                    return "Admin"
                elif b[5] == "x02":
                    return "User"
                elif b[5] == "x03":
                    return "Guest"
                else:
                    return False
            else:
                if b[5] == "x05":
                    print("No such user")
                    return False
                elif b[5] == "x08":
                    print("Acquisition timeout")
            return True
        except Exception as e:
            print(e)
            return False

    def test(self):
        if self.open_connection():
            print("Open connection: ok")
        else:
            print("Open connection: failed")

        if self.close_connection():
            print("Close connection: ok")
        else:
            print("Close connection: failed")
        if self.send_command(command="ask_1_to_N"):
            print("Read fingerprint 1 to N: ok")
        else:
            print("Read fingerprint 1 to N: failed")
        if self.send_command(command="add_user", user=[0x00, 0x05], privileges=0x01):
            print("Add User: ok")
        else:
            print("Add user: failed")
        if self.send_command(command="delete_user", user=[0x00, 0x05]):
            print("User deleted: ok")
        else:
            print("User deleted: failed")
        if self.send_command(command="ask_1_to_1", user=[0x00, 0x01]):
            print("Read fingerprint 1 to 1: ok")
        else:
            print("Read fingerprint 1 to 1: failed")

        result = self.send_command(command="acquire_priviliege", user=[0x00, 0x01])
        print(result)
        if result == "Admin" or result == "User" or result == "Guest":
            print("success", "privileges are:", result)
        else:
            print("error")


if __name__ == "__main__":
    Reader().test()
