import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel
from PyQt5.uic import loadUi


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("main.ui", self)
        self.setWindowTitle("Coffee App")
        self.initialize_database()
        self.load_coffee_data()

    def initialize_database(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("coffee.sqlite")
        if not db.open():
            print("Failed to open database")
            sys.exit(1)

    def load_coffee_data(self):
        query = QSqlQueryModel()
        query.setQuery("SELECT * FROM coffee")
        self.tableView.setModel(query)
        self.tableView.resizeColumnsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec_())
