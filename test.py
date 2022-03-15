t=[]


def test(com):
	t.append(com)
	
def g(name,*args):
	return name,list(args)
	
print(g('kyaw','zin'))	

	
def test1():
	c=""
	j=len(t)
	for i in range(len(t)):
		if i<j-1:
			c+=t[i]+","
		else:			
			c+=t[i] 
	return c
		
		
test("name text")
test("age int")
c=test1()
		
j={1:2}	
del j[1]	
print(j)	
			
k =f"CREATE TABLE info ({c})"

print(k)


a=""

l={"name":"kyaw"}
for i in l:
	a+=i
	print(a)





#import sqlite3


#conn = sqlite3.connect("test.db")
#c = conn.cursor()

#t =k
#c.execute(t)

#print(c.fetchall())

#conn.commit()
#conn.close()



def create_command(self):
		temp=""
		j=0
		k=len(self.__column_name_and_datatype_list)-1
		for name,datatype in self.__column_name_and_datatype_list.items():
			if j<k:
				temp+=name+" "+datatype+","
			else:
				temp+=name+" "+datatype
			j+=1
		return temp
			