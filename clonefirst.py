import sqlite3

class Database:
	def __init__(self,database_Name):
		self._name = database_Name
		self.__dis_state = disconnectedState(self)
		self.__con_state=connectedState(self)
		self.current_state=self.dis_state
		self._connection=None
		#self.connectDatabase()
		self.cursor =None
		
		
		
		
		
	def connect_Database(self):
		self.current_state.connect()
		
	def disconnect_Database(self):
		self.current_state.disconnect()
		
	@property	
	def con_state(self):
		return self.__con_state
		
	@property
	def dis_state(self):
		return self.__dis_state
	
	@property
	def name(self):
		return self._name
		
	@property
	def connection(self):
		return self._connection
		
		
	def set_current_state(self,state):
		self.current_state=state
		
	def set_connection(self,value=None):
		self._connection=value
		
	def set_cursor(self,value=None):
		self.cursor=value
			
		
		
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
		
	
	
test = Database("test2")
#test.disconnect_Database()
test.connect_Database()
#test.connect_Database()
test.disconnect_Database()
test.connect_Database()		
				
#conn = sqlite3.connect("info.db")
#cursor = conn.cursor()
#	