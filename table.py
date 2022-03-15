
import Database

class Table:
	def __init__(self,database:Database,name):
		self.__database = database
		self.__name =name
		self.__column_name_and_datatype_list={}
		self.column_name_list=[]
		
		
					
	def delete_table(self):
			try:
				self.call_delete_table_command()
			except:
				self.print_message("Table not exist")
				
	def create_table(self):
		try:
			self.call_create_table_commad()
		except:
			self.print_message("Table already exists")
						
				
	
			
	def insert(self):
		pass
	
	def add_column(self,data):
		
		self.add_column_name_and_datatype_to_column_list(data)
		
		
	
		
		
	
		
	def delete_column(self,column_name):
		try:
			del self.__column_name_and_datatype_list[column_name]
		except:
			print("Column name does not exist")
			
			
		
	def print_column_list(self):
		print(self.__column_name_and_datatype_list)
		
		
		
		
		
		
	def produce_sub_create_command(self):
		temp=""
		length_of_column_name_list =len(self.column_name_list) 
		for  index in range(length_of_column_name_list):
			if index < length_of_column_name_list-1:
				temp+=self.column_name_list+","
			else:
				temp+=self.column_name_list
		return temp
			
			

			
	def call_create_table_commad(self):
			self.__database.cursor.execute(""" CREATE TABLE """+self.__name+" "+f"({self.produce_sub_create_command()})")		
			self.__database.connection.commit()
			self.print_message("Table created successfully")
		
	def print_message(self,message):
		print(message)
		
	
			
	
	
					
	def call_delete_table_command(self):
		self.__database.cursor.execute(f"DROP TABLE {self.__name}")		
		self.__database.connection.commit()
		self.print_message(f"Table({self.__name}) is deleted!")
			
			
	def set_name(self,name):
		self.__name = name
		
	def add_column_name_and_datatype_to_column_list(self,data):
		data = data.split(" ")
		self.__column_name_and_datatype_list[data[0]]=data[1]
		
	def set_column_name_list(self,new_column_name_list):
		self.column_name_list=new_column_name_list

							
						
#tab = Table(1,2)
#tab.add_column("age int primary key")
#tab.add_column("name text")
#tab.print_column_list()	
#print(tab.create_command())							
	
