import sqlite3
from states import *
from table import Table

class Database:
	def __init__(self,database_name):
		self.table_of_name_and_table_object={}
		self.set_database_name(database_name)
		self.init_state_obj()
		self.init_other_attr()
		self.set_current_state(self.dis_state)
		
	###public api
		
	def connect_Database(self):
		self.current_state.connect()
		
	def disconnect_Database(self):
		self.current_state.disconnect()
		
	def pre_create_table(self,name):
		self.current_table=Table(self,name)
		self.add_table_to_database_table(name)
		
		
	def add_column(self,data):
		self.current_table.add_column(data)
		
		
	def create_table_with_args(self,name,*args):
		self.current_table=Table(self,name)
		self.add_table_to_database_table(name)
		self.current_table.set_column_name_list(list(args))
		self.current_table.call_create_table_commad()
		
		
		
	def create_table(self):
		self.current_table.create_table()
		
	def delete_table(self,name):
		self.table_of_name_and_table_object[name].delete_table()
		del self.table_of_name_and_table_object[name]
		
	#################	
	
		
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
		
	@property
	def cursor(self):
		return self._cursor
		
		
	def set_current_state(self,state):
		self.current_state=state
		
	def set_connection(self,value=None):
		self._connection=value
		
	def set_cursor(self,value=None):
		self._cursor=value
		
	def set_database_name(self,name):
			self._name=name
	def add_table_to_database_table(self,name):
		self.table_of_name_and_table_object[name]=self.current_table
	
				

				
	def init_state_obj(self):
		self.__dis_state = disconnectedState(self)
		self.__con_state=connectedState(self)

	def  init_other_attr(self):
		self._connection=None
		self._cursor =None
		
				
	
	
			
	
					
			
	
			
		
		

