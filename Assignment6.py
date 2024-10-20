import mysql.connector
from pymongo import MongoClient
#MySQL connection configuration mysql_config = {
}
'user': 'root',
'password': 'root',
'host': 'localhost',
'database': 'ecommerce'
# MongoDB connection configuration
mongo_config
}
{
'host': 'localhost',
'port': 27017,
'database': ecommerce_m'
# Connect to MySQL
mysql_conn
=
mysql.connector.connect(**mysql_config)
mysql_cursor = mysql_conn.cursor(dictionary=True)
# Connect to MongoDB
mongo_client
mongo_db
=
=
MongoClient (mongo_config['host'], mongo_config['port']) mongo_client [mongo_config['database']]
=
%s", (cat_id,))
# Fetch all categories
mysql_cursor.execute("SELECT * FROM category")
categories mysql_cursor.fetchall()
# Iterate through each category and fetch associated products
for category in categories:
cat_id = category['cat_id']
# Fetch associated products for the current category mysql_cursor.execute("SELECT * FROM product WHERE c_id
products
=
mysql_cursor.fetchall()
# Add the products array to the category document category['product'] = products
# Insert the categories with their products into MongoDB
mongo_db.category. insert_many (categories)
# Close connections
mysql_cursor.close()
mysql_conn.close()
mongo_client.close()
print("Data transfer complete!")