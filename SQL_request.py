from db_connect import mysqlconnect

# Connect to the database
conn = mysqlconnect()


## INSERT SQL REQUESTS
    # Insert a new user

def insertNewUser(name_user):
    # print(name_user)
    with conn.cursor() as cursor:
        sql = "INSERT INTO `user` (name_user) VALUES (%s)"
        cursor.execute(sql, (name_user,))
        conn.commit()


    # Insert stats
def insertNewStats(user_id, level, nb_try, put, gain):
    with conn.cursor() as cursor:
        sql = "INSERT INTO `stats` (user_id, level, nb_try, put, gain) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (user_id, level, nb_try, put, gain))
        conn.commit()


## UPDATE SQL REQUESTS
    # Update a user
def updateUser(name_user, average_try, average_putting, last_level, total_gain, highest_gain, highest_putting, best_lvl):
    with conn.cursor() as cursor:
        sql = "UPDATE user SET average_try = %s, average_putting = %s, last_level = %s, total_gain = %s, highest_gain = %s, highest_putting = %s, best_lvl = %s WHERE name_user = %s"
        cursor.execute(sql, (average_try, average_putting, last_level, total_gain, highest_gain, highest_putting, best_lvl, name_user))
        conn.commit()

## GET USER SQL REQUESTS
    # Get a user by name
def getUser(name):
    with conn.cursor() as cursor:
        sql = "SELECT * FROM user WHERE name_user = %s"
        cursor.execute(sql, (name,))
        user = cursor.fetchone()
        return user

    # Get all users
def getAllUsers():
    with conn.cursor() as cursor:
        sql = "SELECT * FROM user"
        cursor.execute(sql)
        users = cursor.fetchall()
        return users


## GET STATS SQL REQUESTS
    # Get stats by user id
def getStatsByUserId(user_id):
    with conn.cursor() as cursor:
        sql = "SELECT * FROM stats WHERE user_id = %s"
        cursor.execute(sql, (user_id,))
        stats = cursor.fetchall()
        return stats


    # Get all stats by user name
def getAllStatsByUserName(name_user):
    with conn.cursor() as cursor:
        sql = "SELECT * FROM stats WHERE user_id = (SELECT id FROM user WHERE name_user = %s)"
        cursor.execute(sql, (name_user,))
        stats = cursor.fetchall()
        return stats
