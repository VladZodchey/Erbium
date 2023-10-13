import socket
import threading
import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

HOST = socket.gethostname()
PORT = 3245

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

class Layout(GridLayout):
    def __init__(self, **kwargs):
        self.cols = 2
        send = Button(text='Send!')
        send.bind(on_press=send_message)
        self.add_widget(self.send)
        msg = TextInput(multiline=False)
        self.add_widget(self.msg)
    def send_message(self, instance):
        try:
            message = self.msg.text
            print(message)
            client_socket.send(message.encode("utf-8"))
            self.msg.text = ''
        except Exception as e:
            print(f"Error sending data to the server: {str(e)}")

class Erbi(App):
    def build(self):
        return Layout()

def receive_message():
    while True:
        try:
            data = client_socket.recv(1024).decode("utf-8")
            if not data:
                break
            print(f"Received from server: {data}")
        except Exception as e:
            print(f"Error receiving data from the server: {str(e)}")
            break

receive_thread = threading.Thread(target=receive_message)
receive_thread.start()
