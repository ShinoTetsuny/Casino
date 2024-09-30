import pymysql 
from dotenv import load_dotenv
import os

load_dotenv()

def mysqlconnect(): 
	host = os.getenv('db_host')
	user = os.getenv('db_user')
	password = os.getenv("db_password")
	db = os.getenv('db_db')

	# To connect MySQL database 
	conn = pymysql.connect( 
		host = host,
		user = user,
		password = password,
		db = db,
		cursorclass=pymysql.cursors.DictCursor
	)

	return conn