import sqlite3
# make data base connection
conn = sqlite3.connect("temp.db")
cursor = conn.cursor()

# Data Cleaning and transformation

file = open(file="temp_data_pipes_01a.txt", mode='r')
data = file.read()

lines_list = data.splitlines()

tags = ",".join(lines_list[0].split("|"))
lines_list.remove(lines_list[0])
cursor.execute("create table if not exists temperature (id integer primary key,"+(str(tags))+")")

for line in lines_list:
    tpple = tuple(line.split("|"))
    cursor.execute("insert or replace into temperature (State, Month, Avg, Record)"+" values(?,?,?,?)", tpple)

conn.commit()

# # Data Cleaning Ends here




