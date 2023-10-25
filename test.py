import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class DictionaryViewer(QMainWindow):
    def __init__(self, dictionary):
        super().__init()

        self.dictionary = dictionary
        self.initUI()

        # Create a QTimer to update the table every 10 seconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTable)
        self.timer.start(10000)  # 10,000 milliseconds = 10 seconds

    def initUI(self):
        self.setWindowTitle('Dynamic Dictionary Viewer')
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        self.tableWidget = QTableWidget()
        layout.addWidget(self.tableWidget)

        # Set the number of rows and columns in the table
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderLabels(['Key'])

        # Update the table with dictionary data
        self.updateTable()

    def updateTable(self):
        # Clear the table
        self.tableWidget.setRowCount(0)

        # Populate the table with the latest dictionary keys
        row = 0
        for key in self.dictionary.keys():
            item = QTableWidgetItem(key)
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, item)
            row += 1

def main(dictionary):
    app = QApplication(sys.argv)
    viewer = DictionaryViewer(dictionary)
    viewer.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    # Example dynamic dictionary (you can replace this with your own dictionary)
    dynamic_dict = {
        'Key1': 'Value1',
        'Key2': 'Value2',
        'Key3': 'Value3',
        'Key4': 'Value4'
    }

    main(dynamic_dict)
