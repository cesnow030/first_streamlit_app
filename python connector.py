import snowflake.connector

# Create a connection to Snowflake
conn = snowflake.connector.connect(
    user='<your_user>',
    password='<your_password>',
    account='<your_account>',
    warehouse='<your_warehouse>',
    database='<your_database>',
    schema='<your_schema>'
)

# Create a cursor to execute SQL queries
cur = conn.cursor()

# Define your SQL query
query = "SELECT * FROM my_table"

# Execute the query
cur.execute(query)

# Fetch the results
results = cur.fetchall()

# Close the cursor and connection
cur.close()
conn.close()

# Do something with the results
for row in results:
    print(row)
