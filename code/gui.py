import tkinter as tk
import hex_try
import app


class App:
    def __init__(self):
        self.reader = app.Reader()
        self.window = tk.Tk()
        self.window.geometry("400x150+30+30")
        self.button_1 = tk.Button(self.window, text="read Fingerprint 1 to N", command=lambda
            *args: self.command("ask_1_to_N"))
        self.button_1.place(x=20, y=10)
        self.button_2 = tk.Button(self.window, text="read Fingerprint 1 to 1", command=lambda
            *args: self.command("ask_1_to_1"))
        self.button_2.place(x=20, y=40)
        self.button_3 = tk.Button(self.window, text="add Fingerprint", command=lambda
            *args: self.command("add_user"))
        self.button_3.place(x=20, y=70)
        self.button_4 = tk.Button(self.window, text="delete User", command=lambda
            *args: self.command("delete_user"))
        self.button_4.place(x=155, y=10)
        self.button_5 = tk.Button(self.window, text="acquire_priviliege", command=lambda
            *args: self.command("acquire_priviliege"))
        self.button_5.place(x=155, y=40)
        self.button_6 = tk.Button(self.window, text="open connection", command=lambda
            *args: self.command("open"))
        self.button_6.place(x=155, y=70)
        self.button_7 = tk.Button(self.window, text="close connection", command=lambda
            *args: self.command("close"))
        self.button_7.place(x=270, y=10)
        self.label1 = tk.Label(self.window, text="Befehl war:")
        self.label1.place(x=20, y=100)
        self.label2 = tk.Label(self.window, text="Rechte:")
        self.label2.place(x=20, y=120)
        self.label3 = tk.Label(self.window, text="Trage ID ein:")
        self.label3.place(x=270, y=40)
        self.entry1 = tk.Entry(self.window)
        self.entry1.place(x=270, y=65)
        self.label4 = tk.Label(self.window, text="Rechte eintragen:")
        self.label4.place(x=270, y=90)
        self.entry2 = tk.Entry(self.window)
        self.entry2.place(x=270, y=115)
        self.button_8 = tk.Button(self.window, text="delete all", command=lambda
            *args: self.command("delete_all"))
        self.button_8.place(x=155, y=100)
        self.window.mainloop()

    def command(self, command):
        assert isinstance(command, str)
        try:
            a = self.entry1.get()
            b = self.entry2.get()
            if command == "ask_1_to_1" or command == "delete_user":
                try:
                    a = int(a)
                    if a > 255:
                        user_id = hex_try.wert_tauschen(a)
                    else:
                        user_id = [0x00, a]
                    if self.reader.send_command(command, user=user_id):
                        self.label1.config(text="Befehl war: erfolgreich", bg="green")
                    else:
                        self.label1.config(text="Befehl war: nicht erfolgreich", bg="red")
                except Exception as e:
                    self.entry1.delete(0, tk.END)
                    return False
            elif command == "add_user":
                a = int(a)
                b = int(b)
                try:
                    if b <= 3 and b >= 1:
                        if a > 255:
                            user_id = hex_try.wert_tauschen(a)
                        else:
                            user_id = [0x00, a]
                        if self.reader.send_command(command, user=user_id, privileges=b):
                            self.label1.config(text="Befehl war: erfolgreich", bg="green")
                        else:
                            self.label1.config(text="Befehl war: nicht erfolgreich", bg="red")
                    else:
                        self.entry1.delete(0, tk.END)
                        self.entry2.delete(0, tk.END)
                except Exception as e:
                    print(e)
            elif command == "acquire_priviliege":
                try:
                    a = int(a)
                    if a > 255:
                        user_id = hex_try.wert_tauschen(a)
                    else:
                        user_id = [0x00, a]
                    rechte = self.reader.send_command(command, user=user_id)
                    if rechte:
                        self.label1.config(text="Befehl war: erfolgreich", bg="green")
                        self.label2.config(text="Rechte: " + rechte)
                    else:
                        self.label1.config(text="Befehl war: nicht erfolgreich", bg="red")
                except Exception as e:
                    print(e)
            elif command == "open" or command == "close":
                if command == "open":
                    if self.reader.open_connection():
                        self.label1.config(text="Befehl war: erfolgreich", bg="green")
                    else:
                        self.label1.config(text="Bfehl war: nicht erfolgreich", bg="red")
                elif command == "close":
                    if self.reader.close_connection():
                        self.label1.config(text="Befehl war: erfolgreich", bg="green")
                    else:
                        self.label1.config(text="Bfehl war: nicht erfolgreich", bg="red")
            else:
                try:
                    a = int(a)
                    if a > 255:
                        user_id = hex_try.wert_tauschen(a)
                    else:
                        user_id = [0x00, a]
                    if self.reader.send_command(command, user=user_id):
                        self.label1.config(text="Befehl war: erfolgreich", bg="green")
                    else:
                        self.label1.config(text="Befehl war: nicht erfolgreich", bg="red")
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    App()