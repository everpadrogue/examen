# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\practica.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.Qt import QSqlDatabase
import sqlite3
from pprint import pprint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(230, 30, 421, 321))
        self.tableView.setObjectName("tableView")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 70, 151, 211))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_viewdata = QtWidgets.QPushButton(self.widget)
        self.pushButton_viewdata.setObjectName("pushButton_viewdata")
        self.verticalLayout.addWidget(self.pushButton_viewdata)
        self.pushButton_addRow = QtWidgets.QPushButton(self.widget)
        self.pushButton_addRow.setObjectName("pushButton_addRow")
        self.verticalLayout.addWidget(self.pushButton_addRow)
        self.pushButton_deleteRow = QtWidgets.QPushButton(self.widget)
        self.pushButton_deleteRow.setObjectName("pushButton_deleteRow")
        self.verticalLayout.addWidget(self.pushButton_deleteRow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    


        self.create_DB()
        self.pushButton_viewdata.clicked.connect(self.print_data)
        self.model = None
        self.pushButton_viewdata.clicked.connect(self.sql_table_view_model)
        self.pushButton_addRow.clicked.connect(self.sql_add_row)
        self.pushButton_deleteRow.clicked.connect(self.sql_delete_row)
        
    def sql_delete_row(self):
        try:
            if self.model:
                self.model.removeRow(self.tableView.currentIndex().row())
            else:
                self.sql_tableview_model
        except Exception as e:
            print(e)
            
    def sql_add_row(self):
        try:
            if self.model:
                self.model.insertRows(self.model.rowCount(),1)
            else:
                self.sql_tableview_model()
        except Exception as e:
            print(e)
                 
    def sql_table_view_model(self):
        try:
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('Miempleado.db')
            
            tableview=self.tableView
            self.model= QtSql.QSqlTableModel()
            tableview.setModel(self.model)
            
            self.model.setTable('empleado')
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            self.model.select()
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, "id_empleado")
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, "apellido")
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, "nombre")
            self.model.setHeaderData(3, QtCore.Qt.Horizontal, "telefono")
            self.model.setHeaderData(4, QtCore.Qt.Horizontal, "direccion")
            self.model.setHeaderData(5, QtCore.Qt.Horizontal, "fecha_nacimiento")
            self.model.setHeaderData(6, QtCore.Qt.Horizontal, "observaciones")
            self.model.setHeaderData(7, QtCore.Qt.Horizontal, "sueldo")
            self.model.setHeaderData(8, QtCore.Qt.Horizontal, "id_departamento")
            
        except Exception as e:
            print(e)
            
    def print_data(self):
        try:
            sqlite_file='Miempleado.db'
            conn=sqlite3.connect(sqlite_file)
            cursor= conn.cursor()
            
            cursor.execute("SELECT * FROM 'empleado' ORDER BY id_empleado")
            all_rows = cursor.fetchall()
            pprint(all_rows)
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(e)
            
        
        
    def create_DB(self):
        try:
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('Miempleado.db')
            db.open() 
            
            query = QtSql.QSqlQuery() 
            
            query.exec_("create table empleado(id_empleado int primary key,"
                            "apellido VARCHAR(45), nombre VARCHAR(45), telefono int, direccion VARCHAR(45), fecha_nacimiento VARCHAR(20), observaciones VARCHAR(45), sueldo int, id_departamento int)")
            query.exec_("insert into empleado values(1001,'Padron Guerrero', 'Everardo', '4181006161', 'Dolores Hidalgo', '1-07-1999','buen empleado','1000','100')")
            query.exec_("insert into empleado values(1001,'Padron Guerrero', 'Brenda', '4280000000', 'Dolores Hidalgo', '2-04-2002', 'buen empleada','2000','101')")
            query.exec_("insert into empleado values(1002,'Armijo Hernandez', 'Jared', '2616444646', 'Dolores Hidalgo', '14-06-1999', 'buen empleado','8000','102')")
            query.exec_("insert into empleado values(1003,'Briones Gomez', 'Abigail', '5119151166', 'Dolores Hidalgo', '12-11-2000', 'buen empleada','55000','103' )")
        except Exception as e:
            print(e)
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_viewdata.setText(_translate("MainWindow", "View Data"))
        self.pushButton_addRow.setText(_translate("MainWindow", "Add Row"))
        self.pushButton_deleteRow.setText(_translate("MainWindow", "Delete Row"))          




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
