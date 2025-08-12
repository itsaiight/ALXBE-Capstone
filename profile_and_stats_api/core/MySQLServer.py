import mysql.connector

try:
   
    mydb = mysql.connector.connect(
        host= 'localhost', 
        user = 'root', 
        password = 'uDNR9Q8z5FStjEJn'
    )

    if mydb.is_connected():
        mycursor = mydb.cursor()
        mycursor.execute("""
            INSERT INTO f1_driver_and_stats.core_result(result_id, position, points, driver_id, race_id)
            VALUES 
            (1,1, 25, 10, 1),
            (2,2, 18, 5, 1),
            (3,3, 15, 11, 1),
            (4,4, 12, 18, 1),
            (5,5, 10, 8, 1),
            (6,6, 8, 18, 1),
            (7,7, 6, 4, 1),
            (8,8, 4, 9, 1),
            (9,9, 2, 14, 1),
            (10,10, 1, 1, 1),
            (11,11, 0, 3, 1),
            (12,12, 0, 13, 1),
            (13,13, 0, 7, 1),
            (14,14, 0, 16, 1),
            (15,15, 0, 15, 1),
            (16,16, 0, 19, 1),
            (17,17, 0, 2, 1),
            (18,18, 0, 6, 1),
            (19,19, 0, 21, 1),
            (20,20, 0, 17, 1),
            (21,1, 25, 14, 2),
            (22,2, 18, 10, 2),
            (23,3, 15, 11, 2),
            (24,4, 12, 5, 2),
            (25,5, 0, 9, 2),
            (26,6, 0, 1, 2),
            (27,7, 10, 7, 2),
            (28,8, 8, 18, 2),
            (29,9, 6, 12, 2),
            (30,10, 4, 16, 2),
            (31,11, 0, 3, 2),
            (32,12, 2, 8, 2),
            (33,13, 1, 6, 2),
            (34,14, 0, 17, 2),
            (35,15, 0, 21, 2),
            (36,16, 0, 15, 2),
            (37,17, 0, 19, 2),
            (38,18, 0, 4, 2),
            (39,19, 0, 13, 2),
            (40,20, 0, 2, 2);
        """)
        mydb.commit()
        print("entries created successfully!")

except mysql.connector.Error as e:
    print("Error while connecting to MySQL or creating the database:", e)


finally:
    if mydb.is_connected:
        mycursor.close()
        mydb.close()

"""This is used to enter the results into my results table in the database,
I have done the rest in MYSQL. This is just to show how to do it in python."""