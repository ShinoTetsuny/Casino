import pymysql

def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="",
        db='casino',
    )

    cur = conn.cursor()
    cur.execute("select @@version")
    output = cur.fetchall()
    print(output)

    # Create the user table
    user_table_query = """
    CREATE TABLE IF NOT EXISTS user (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name_user VARCHAR(255),
        date DATE,
        average_try FLOAT,
        average_putting FLOAT,
        last_level INT
    )
    """
    cur.execute(user_table_query)

    # Create the stats table
    stats_table_query = """
    CREATE TABLE IF NOT EXISTS stats (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        best_level INT,
        nb_try INT,
        highest_gain FLOAT,
        sold FLOAT,
        highest_putting FLOAT,
        FOREIGN KEY (user_id) REFERENCES user(id)
    )
    """
    cur.execute(stats_table_query)

    # To close the connection
    conn.close()

# Driver Code
if __name__ == "__main__":
    mysqlconnect()