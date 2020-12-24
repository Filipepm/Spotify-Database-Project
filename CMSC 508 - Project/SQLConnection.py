import mysql.connector

mydb = mysql.connector.connect(
  host="cmsc508-project-12.cp9ngw4gzmqa.us-east-1.rds.amazonaws.com",
  user="admin",
  password="1234abcd"
)

print(mydb)
