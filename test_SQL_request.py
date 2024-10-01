from SQL_request import *
from db_connect import mysqlconnect

def TestSQL():
    # Init des variables user
    name = "tom"
    average_try = 10
    average_putting = 100
    last_level = 5
    total_gain = 100
    highest_gain = 1000
    highest_putting = 100
    best_lvl = 3

    print('test')

    # Init des variables stats
    level = 3
    nb_try = 20
    #put = 2000.0
    #gain = 300.0

    # Connect to database
    conn = mysqlconnect()
    cur = conn.cursor()

    try:
        insertNewUser(name)

        # Get user
        user_id = getUser(name)
        print(user_id['id'])

        # Insert stats
        insertNewStats(user_id['id'], level, nb_try)

        # user, level, nb_try, put, gain

    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        # Close bdd
        cur.close()
        conn.close()

TestSQL()