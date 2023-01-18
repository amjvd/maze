from PyQt5 import QtWidgets, QtGui, QtCore											#Importing libraries to be used		
import pyodbc																		
from login import *
from home import Ui_MainWindow
from register import Ui_registerPage
from forgotPasswordUser import Ui_forgotPasswordUserPage
from forgotPassword import Ui_forgotPasswordPage
from maze import *


conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=.\Database\data.accdb;')    		#location of database

GLOBNAME = "not set"								#Global variables that will be used throughout all the classes
GLOBUSER = "not set"
GlOBSECUIRTY = "not set"



	


class loginPage(QtWidgets.QMainWindow):                                 #Sets up login class passing in necessary widgets
	def __init__(self, *args, **kwargs):								#Instructor function. Any variable declared here can be accessed throughout the class.
		super().__init__(*args, **kwargs)								#Allows access to parent class using the args and the kwargs included
		self.ui = Ui_loginPage()										#Sets the gui to the gui of the login page
		self.ui.setupUi(self)											#Sets up the gui
		self.ui.btnclear.clicked.connect(self.clear)					#When clear button is clicked, connects to clear function
		self.ui.btnsubmit.clicked.connect(self.loginAuth)				
		self.ui.btnregister.clicked.connect(self.register)				
		self.ui.btnforgotPassword.clicked.connect(self.forgotPassword)	

	def clear(self):                                             #clear function, sets username and password empty
		self.ui.txtusername.setText("")
		self.ui.txtpassword.setText("")

	def register(self):
		registerPage.show()         							  #register function when register button is clicked, shows the register page and hides login
		loginPage.hide()

	def forgotPassword(self):									#forgot password function when button is clicked, shows forgot Password page
		forgotPasswordUserPage.show()
		loginPage.hide()

	def loginAuth(self):                                      #login Authentication function, compares info to database
		username = self.ui.txtusername.text()
		password = self.ui.txtpassword.text()

		if username != "" or password != "":                   #checks if information is entered
			conn = pyodbc.connect(conn_str)
			cursor = conn.cursor()                                   #opens database
			cursor.execute('SELECT * From userDetails WHERE Username = ?', (username))

			record = cursor.fetchall()
			conn.close()                                            #closes database

			uname = ""												#creates new variables to be used to save database info 
			pword = ""
			name = ""

			for row in record:                                        #sets name variable to first field which is name field, uname variable to the second field in the database which is the username field, and sets pword to the third field which is password field
				name = row[1]
				uname = row[2]
				pword = row[3]

			if username == uname and password == pword:         #checks if username and password are correct

				GLOBNAME = name 								#sets the name of the user to a global variable, and then sets welcome title to globuser (personalised)
				homePage.ui.lbltitle.setText(f"welcome {GLOBNAME}")

				loginPage.hide()
				homePage.show()                             #Homepage is shown if info is right

			else:
				QtWidgets.QMessageBox.critical(self,'Unsuccessful',"<FONT COLOR='#FFEFD5'>" 'Invalid information')   #Output if the username or password are wrong

		else:
			QtWidgets.QMessageBox.critical(self,'Unsuccessful',"<FONT COLOR='#FFEFD5'>" 'You have not entered any information')       #Output if no information is entered



class registerPage(QtWidgets.QMainWindow):					#Sets up register class, passing in the necessary widgets
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ui = Ui_registerPage()
		self.ui.setupUi(self)
		self.ui.btnlogin.clicked.connect(self.login)                  
		self.ui.btnclear.clicked.connect(self.clear)
		self.ui.btnsubmit.clicked.connect(self.submit)


	def login(self):
		registerPage.hide()
		loginPage.show()

	def clear(self):                                             
		self.ui.txtusername.setText("")
		self.ui.txtpassword.setText("")
		self.ui.txtname.setText("")

	def submit(self):
		name = self.ui.txtname.text()											#Sets variables to what the user has inputed into the required boxes
		username = self.ui.txtusername.text()
		password = self.ui.txtpassword.text()
		securityQuestion = self.ui.cmbsecurityAnswer.currentText()
		securityAnswer = self.ui.txtsecurityAnswer.text()

		if username != "" and password != "" and name != "" and securityAnswer != "" and securityQuestion != "Security Question:":			#Makes sure that the variables arent empty (That the user has inputed something)
			if len(username)>2 and len(username)<12:
				if len(password)>2 and len(password)<12:																					#Makes sure that the what the user has inputed fits within the preset char limits
					if len(name)<10:
						if len (securityAnswer)<20:                  
							conn = pyodbc.connect(conn_str)
							cursor = conn.cursor()
							cursor.execute('SELECT * From userDetails WHERE Username = ?', (username))
							record = cursor.fetchall()
							error = False

							for element in record:
								if username in element:
									error = True 																	#Sets error to true if username is already in database, so usernames are unique
							if error == True:
								QtWidgets.QMessageBox.critical(self,'Unsuccessful', "<FONT COLOR='#FFEFD5'>"'Username already exists'"<FONT COLOR='#FFEFD5'>") 

							else:
								print(securityAnswer)
								insertQuery = ("INSERT INTO userDetails (Name, Username, Password, Security_Question, Security_Answer) VALUES(?,?,?,?,?)") 	#If no errors, inserts users details into the database
								dataInsert = (name,username,password,securityQuestion,securityAnswer)
								cursor.execute(insertQuery,dataInsert)
								conn.commit()
								QtWidgets.QMessageBox.information(self,'Successful',"<FONT COLOR='#FFEFD5'>" 'Account created') 
								conn.close()
								registerPage.hide()
								loginPage.show()

						else:
							QtWidgets.QMessageBox.critical(self,'Unsuccessful',"<FONT COLOR='#FFEFD5'>" 'Make sure security answer is less than 20 characters')
					else:
						QtWidgets.QMessageBox.critical(self,'Unsuccessful',"<FONT COLOR='#FFEFD5'>" 'Make sure name is less than 10 characters')
				else:
					QtWidgets.QMessageBox.critical(self,'Unsuccessful',"<FONT COLOR='#FFEFD5'>" 'Make sure password is more than 2 characters and less than 12')
			else:
				QtWidgets.QMessageBox.critical(self,'Unsuccessful',"<FONT COLOR='#FFEFD5'>" 'Make sure username is more than 2 characters and less than 12')

		else:
			QtWidgets.QMessageBox.critical(self,'Unsuccessful',"<FONT COLOR='#FFEFD5'>" 'Do not leave any boxes blank') 


				

		

class forgotPasswordUserPage(QtWidgets.QMainWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ui = Ui_forgotPasswordUserPage()
		self.ui.setupUi(self)
		self.ui.btnclear.clicked.connect(self.clear)
		self.ui.btnlogin.clicked.connect(self.login)                  
		self.ui.btnregister.clicked.connect(self.register)
		self.ui.btnsubmit.clicked.connect(self.submit)
	
	def clear(self):                                             
		self.ui.txtusername.setText("")


	def login(self):
		forgotPasswordUserPage.hide()
		loginPage.show()

	def register(self):
		forgotPasswordUserPage.hide()
		registerPage.show()

	
	def submit(self):
		GLOBUSER = self.ui.txtusername.text()
		
		if GLOBUSER == "":
			QtWidgets.QMessageBox.critical(self,'Unsuccessful',"<FONT COLOR='#FFEFD5'>" 'You have not entered a username') 
		else:
			conn = pyodbc.connect(conn_str)
			cursor = conn.cursor()                                   #opens database
			cursor.execute('SELECT * From userDetails WHERE Username = ?', (GLOBUSER))
			record = cursor.fetchone()
			conn.close()
			
			if record:
				GlOBSECUIRTY = record[4]
				forgotPasswordUserPage.hide()
				forgotPasswordPage.show()
				forgotPasswordPage.ui.lblusername.setText(GLOBUSER)
				forgotPasswordPage.ui.lblsecurityQuestion.setText(GlOBSECUIRTY)
			
			else: 
				QtWidgets.QMessageBox.critical(self,'Unsuccessful',"<FONT COLOR='#FFEFD5'>" 'Username doesnt exist') 




class forgotPasswordPage(QtWidgets.QMainWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ui = Ui_forgotPasswordPage()
		self.ui.setupUi(self)
		self.ui.btnclear.clicked.connect(self.clear)
		self.ui.btnback.clicked.connect(self.back)                  
		self.ui.btnsubmit.clicked.connect(self.submit)

	def clear(self):                                             
		self.ui.txtsecurityAnswer.setText("")


	def back(self):
		forgotPasswordPage.hide()
		forgotPasswordUserPage.show()

	def submit(self):
		GLOBUSER = self.ui.lblusername.text()
		securityAnswer = self.ui.txtsecurityAnswer.text()
		if securityAnswer != "":
			conn = pyodbc.connect(conn_str)
			cursor = conn.cursor()                                  
			cursor.execute('SELECT * From userDetails WHERE Username = ?', (GLOBUSER))
			record = cursor.fetchone()
			conn.close()

			if securityAnswer == record[5]:
				password = record[3]
				QtWidgets.QMessageBox.information(self,'Alert',"<FONT COLOR='#FFEFD5'>" f'"{password}" is your password')
				forgotPasswordPage.hide()
				loginPage.show()
				


			else: 
				QtWidgets.QMessageBox.critical(self,'Unsuccessful',"<FONT COLOR='#FFEFD5'>" 'Incorrect Security Answer') 
		else: 
			QtWidgets.QMessageBox.critical(self,'Unsuccessful',"<FONT COLOR='#FFEFD5'>" 'Please type a Security Answer in') 



	



		

class homeWindow(QtWidgets.QMainWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.btnlogout.clicked.connect(self.logout)
		self.ui.btnmaze.clicked.connect(self.mazePage)
		

	def logout(self):
		homePage.hide()
		loginPage.show()


	def mazePage(self):
		homePage.hide()
		maze = MazeGame()
		maze.mainMenu()
		homePage.show( )
		
				



	

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    loginPage = loginPage()
    loginPage.show()
    registerPage = registerPage()
    forgotPasswordUserPage = forgotPasswordUserPage()
    forgotPasswordPage = forgotPasswordPage()
    homePage = homeWindow()
    app.exec_()
    
    
  