from cgitb import reset
from unittest import result
import pyodbc

class Task:
	# Parametros de ligação à base de Dados
	def connection(self):
		servername='LAPTOP-CE766B02'
		portnumber='1433'
		databasename='Tarefas'
		username='EmanuelRod'
		password='xela'

		server="DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={};PORT={};DATABASE={};UID={};PWD={};Trusted_Connection=yes;"
		server=server.format(servername,portnumber,databasename,username,password)
		return server

	def allTasks(self):
		# objecto de coneção base de dados e apontador
		conn=pyodbc.connect(self.connection())
		cursor=conn.cursor()
		# objeto com a query à BD
		sqlquery="SELECT * FROM dbo.tasks ORDER BY state "
		cursor.execute(sqlquery)
		result=cursor.fetchall()
		#Terminar todas as ligações
		cursor.close()
		conn.close()
		# Objeto vazio que vai guardar os resultados
		tasks=[]
		for task in result:
			taskList={"id":task[0],"task":task[1],"date_created":task[2],"state":task[3]}
			tasks.append(taskList)

		return tasks

	def getTask(self,id):
		conn=pyodbc.connect(self.connection())
		cursor=conn.cursor()
		sqlquery="SELECT * FROM dbo.tasks WHERE id = ?"
		values=(id)
		cursor.execute(sqlquery,values)
		result=cursor.fetchall()
		cursor.close()
		conn.close()
		return result

	def addTask(self,task):
		conn=pyodbc.connect(self.connection())
		cursor=conn.cursor()
		sqlquery="INSERT dbo.tasks(task,date_created) VALUES (?,CAST(GETDATE() AS DATE))"
		values=(task)
		cursor.execute(sqlquery,values)
		conn.commit()
		cursor.close()
  
	def updateTask(self,taskUpdated,id):
		conn=pyodbc.connect(self.connection())
		cursor=conn.cursor()
		sqlquery="UPDATE dbo.tasks SET task = ?, date_created = CAST(GETDATE() AS DATE) WHERE id = ?"
		values=(taskUpdated,id)
		cursor.execute(sqlquery,values)
		conn.commit()
		cursor.close()
	
	def alterTask(self,state,id):
		conn=pyodbc.connect(self.connection())
		cursor=conn.cursor()
		sqlquery="UPDATE dbo.tasks SET state = ? WHERE id = ?"
		values=(state,id)
		cursor.execute(sqlquery,values)
		conn.commit()
		cursor.close()
  
	def deleteTask(self,id):
		conn=pyodbc.connect(self.connection())
		cursor=conn.cursor()
		sqlquery="DELETE FROM dbo.tasks WHERE id = ?"
		values=(id)
		cursor.execute(sqlquery,values)
		conn.commit()
		cursor.close()
