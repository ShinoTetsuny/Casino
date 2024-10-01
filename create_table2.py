from db_connect import mysqlconnect

# Connect to the database
conn = mysqlconnect()
cur = conn.cursor()

def create_tables():

    # Create the user table
    user_table_query = """
    CREATE TABLE IF NOT EXISTS user (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name_user VARCHAR(255) UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        average_try FLOAT DEFAULT 0,
        average_putting FLOAT DEFAULT 0,
        last_level INT,
        total_gain FLOAT DEFAULT 0,
        highest_gain FLOAT DEFAULT 0,
        highest_putting FLOAT DEFAULT 0,
        best_lvl INT DEFAULT 0
    )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    """
    cur.execute(user_table_query)
    conn.commit()

    # Create the stats table
    stats_table_query = """
    CREATE TABLE IF NOT EXISTS stats (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        level INT,
        nb_try INT,
        put FLOAT,
        gain FLOAT,
        FOREIGN KEY (user_id) REFERENCES user(id)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    """
    cur.execute(stats_table_query)
    conn.commit()

    # To close the connection
    cur.close()
    conn.close()

create_tables()