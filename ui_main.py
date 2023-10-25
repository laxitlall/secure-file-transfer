from interface import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from users import active_users
import socket
import json

'''class DictionaryTableWidget(QTableWidget):
    def __init__(self, data_dict):
        super().__init__()
        self.data_dict = data_dict
        self.setColumnCount(1)
        self.setRowCount(len(data_dict))
        self.setHorizontalHeaderLabels(["Keys"])
        self.populate_table()

    def populate_table(self):
        row = 0
        for key in self.data_dict.keys():
            item = QTableWidgetItem(key)
            self.setItem(row, 0, item)
            row += 1

class active_users(QMainWindow):
    def __init__(self, data_dict):
        super().__init__()
        self.data_dict = data_dict
        self.setWindowTitle("Dictionary Keys Table")
        self.setGeometry(100, 100, 400, 300)
        widget = QWidget()
        layout = QVBoxLayout()
        self.table_widget = DictionaryTableWidget(data_dict)
        layout.addWidget(self.table_widget)
        widget.setLayout(layout)
        self.setCentralWidget(widget)'''

class second_window(QMainWindow):
    def __init__(self,data_dict):
        super().__init__()
        self.data_dict = data_dict
        self.ui = active_users(data_dict)
        self.ui.setupUi(self)
        self.ui.reset.clicked.connect(self.refresh_op)

    def refresh_op(self):
        data_dict = server_connection()
        self.close()
        self.user_interface  = second_window(data_dict)
        self.user_interface.show()

def server_connection(msg=""):
    server_ip = "10.81.40.15"
    server_port = 5555
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((server_ip,server_port))
    if len(msg) > 0:
        client_socket.send(msg.encode('utf-8'))
    data_str = client_socket.recv(1024).decode('utf-8')
    data_dict = json.loads(data_str)
    client_socket.close()
    return data_dict

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.submit.clicked.connect(self.submit_op)
    
    def submit_op(self):
        #print(self.ui.username.text())
        #send username to server (hardcode server ip) and receive a dictionary
        msg =self.ui.username.text()
        data_dict = server_connection(msg)
        #dictionary is opened in new ui in form of table
        self.close()
        self.user_interface  = second_window(data_dict)
        self.user_interface.show()
        '''self.users_interface = active_users(data_dict)
        self.users_interface.show()'''
        #click on the username, new ui of file selection opens, select file and transfer by clicking "transfer"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())