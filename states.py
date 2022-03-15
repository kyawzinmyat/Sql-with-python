import sqlite3
import Database


class connectedState:
	
	def __init__(self,database:Database):
		self.__database = database
		
	def connect(self):
		print(f"Already connected to database({self.__database.name})!")
		
	def disconnect(self):
		self.set_database_state()
		self.print_disconnect_status()	
	
	def set_database_state(self):
		self.__database.set_current_state(self.__database.dis_state)
		
	def print_disconnect_status(self):
		print(f"disconnected to database")
		
		
		
class disconnectedState:
	def __init__(self,database:Database):
	    self.__database=database
	    
	def connect(self):
		
		self.set_database_state()
		self.call_connect_and_cursor_command()
		
	def disconnect(self):
		print("Database is already disconnected!")
		
		
	def call_connect_and_cursor_command(self):
		self.__database.set_connection(sqlite3.connect(f"{self.__database.name}.db"))
		self.__database.set_cursor(self.__database.connection.cursor())

		self.print_text_create_successfully()
		
		
		
	def set_database_state(self):
		self.__database.set_current_state(self.__database.con_state)
		
	def print_text_create_successfully(self):
		print("successfully connected to database")
		

	
		