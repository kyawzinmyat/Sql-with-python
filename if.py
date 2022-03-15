from Database import Database
#from .states import *


test = Database("test")
#test.disconnect_Database()
test.connect_Database()
#test.connect_Database()
#test.disconnect_Database()
#test.add_table()
#test.connect_Database()		

				


													



test.delete_table("person10")
print(test.table_of_name_and_table_object)

#test.create_table("person3","name text")
#test.create_table("person4","age int")

#print(test.data_table)
#							
													
#conn = sqlite3.connect("info.db")
#cursor = conn.cursor()
#	