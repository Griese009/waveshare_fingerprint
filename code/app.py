import serial


class Reader:
    def __init__(self):
        self.port = ["COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM9", "ttyUSB0", "ttyUSB1",
                     "ttyUSB2", "ttyUSB3", "ttyUSB4", "ttyUSB5", "ttyUSB6", "ttyUSB7", "ttyUSB8"]
        self.baudrate = 19200
        self.ser = None
        self.befehle = {"user_amount": [0xF5, 0x09,
                                            0x00,  # Null
                                            0x00,  # Null
                                            0x00,  # Null
                                            0x00,  # Null
                                            0x09,  # CHK (Build up through Byte 2 to Byte 6 as a XOR-Operation)
                                            0xF5],
                        "ask_1_to_N": [0xF5, 0x0C,
                                         0x00,  # Null
                                         0x00,  # Null
                                         0x00,  # Null
                                         0x00,  # Null
                                         0x0C,  # CHK (Build up through Byte 2 to Byte 6 as a XOR-Operation)
                                         0xF5],
                        "ask_1_to_1": [0xF5, 0x0B,
                                         0x00,  # Nutzer_ID 1Byte
                                         0x00,  # Nutzer_ID 2Byte
                                         0x00,  # Null
                                         0x00,  # Null
                                         0x00,  # CHK
                                         0xF5],
                        "fingerabdruck": [0xF5, 0x24, 0x00, 0x00, 0x00, 0x00, 0x24, 0xF5],
                        "delete_all": [0xF5, 0x05, 0x00, 0x00, 0x00, 0x00, 0x05, 0xF5],
                        "delete_user": [0xF5, 0x04,
                                          0x00,  # Nutzer_ID 1-Byte (hohe Zahl bsp. ID = 1000)
                                          0x00,  # Nutzer_ID 2-Byte (kleine Zahl, bsp. ID = 1)
                                          0x00,  # Null
                                          0x00,  # Null
                                          0x00,  # CHK
                                          0xF5],
                        "add_user": [[0xF5, 0x01,
                                      0x00,  # User-ID
                                      0x00,  # User-ID
                                      0x00,  # Privileges (0x01, 0x02, 0x03)
                                      0x00,  # Null
                                      0x00,  # CHK
                                      0xF5],
                                     [0xF5, 0x02,
                                      0x00,  # User-ID
                                      0x00,  # User-ID
                                      0x00,  # Privileges (0x01, 0x02, 0x03)
                                      0x00,  # Null
                                      0x00,  # CHK
                                      0xF5],
                                     [0xF5, 0x03,
                                      0x00,  # User-ID
                                      0x00,  # User-ID
                                      0x00,  # Privileges (0x01, 0x02, 0x03)
                                      0x00,  # Null
                                      0x00,  # CHK
                                      0xF5]]}

    def open_connection(self):
        try:
            if self.ser == None:
                for port in self.port:
                    try:
                        self.ser = serial.Serial(port=port, baudrate=self.baudrate)
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
            if self.ser == None:
                pass
            else:
                self.ser.close()
                self.ser = None
            return True
        except Exception as e:
            print('Die Verbindung konnte aufgrund von: "' + str(e) + '" nicht geschlossen werden.')
            return False

    def sende_befehl_mit_nutzer(self, befehl, user=None, privileges=None):
        if user is None:
            user = [0x00, 0x00]
        else:
            pass

        if privileges is None:
            privileges = 0x00
        else:
            pass

        assert isinstance(privileges, int)
        assert isinstance(user[0], int)
        assert isinstance(user[1], int)
        assert isinstance(befehl, str)
        try:
            if befehl == "add_user":
                for i in self.befehle[befehl]:
                    if self.ser == None:
                        self.open_connection()
                        a = i
                        self.ser.write([a[0], a[1], user[0], user[1], privileges, a[5],
                                a[1] ^ user[0] ^ user[1] ^ privileges ^ a[5], a[7]])
                        self.daten_erhalten()
                        self.close_connection()
                    else:
                        a = self.befehle[befehl]
                        self.ser.write([a[0], a[1], user[0], user[1], privileges, a[5],
                                a[1] ^ user[0] ^ user[1] ^ privileges ^ a[5], a[7]])
                        self.daten_erhalten()
            else:
                if self.ser == None:
                    self.open_connection()
                    a = self.befehle[befehl]
                    self.ser.write([a[0], a[1], user[0], user[1], privileges, a[5],
                                a[1] ^ user[0] ^ user[1] ^ privileges ^ a[5], a[7]])
                    self.daten_erhalten()
                    self.close_connection()
                else:
                    a = self.befehle[befehl]
                    self.ser.write([a[0], a[1], user[0], user[1], privileges, a[5],
                                a[1] ^ user[0] ^ user[1] ^ privileges ^ a[5], a[7]])
                    self.daten_erhalten()
            return True
        except Exception as e:
            print(e)
            return False

    def daten_erhalten(self):
        try:
            a = self.ser.read(8)
            print(str(a))
            a = str(a)
        except Exception as e:
            print(e)

    def test(self):
        if self.open_connection():
            print("Open connection: ok")
        else:
            print("Open connection: failed")

        if self.close_connection():
            print("Close connection: ok")
        else:
            print("Close connection: failed")
        if self.sende_befehl_mit_nutzer(befehl="ask_1_to_N"):
            print("Read fingerprint 1 to N: ok")
        else:
            print("Read fingerprint 1 to N: failed")
        if self.sende_befehl_mit_nutzer(befehl="add_user", user=[0x00, 0x05], privileges=0x01):
            print("Add User: ok")
        else:
            print("Add user: failed")
        if self.sende_befehl_mit_nutzer(befehl="delete_user", user=[0x00, 0x05]):
            print("User deleted: ok")
        else:
            print("User deleted: failed")
        if self.sende_befehl_mit_nutzer(befehl="ask_1_to_1", user=[0x00, 0x01]):
            print("Read fingerprint 1 to 1: ok")
        else:
            print("Read fingerprint 1 to 1: failed")


if __name__ == "__main__":
    Reader().test()
