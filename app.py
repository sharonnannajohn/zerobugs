import sqlite3
conn = sqlite3.connect('weddingvenues.db')
curs=conn.cursor()
curs.execute(""" CREATE TABLE IF NOT EXISTS VENUES
                 (VENUE_ID integer PRIMARY KEY AUTOINCREMENT,
                  VENUE_NAME VARCHAR(200),
                  LOCATION TEXT,
                  OWNER_NAME TEXT,
                  OWNER_CONTACT integer
                  )         
             """)
conn.commit()

curs.execute("""INSERT INTO VENUES (VENUE_NAME,LOCATION,OWNER_NAME,OWNER_CONTACT) VALUES(?,?,?,?)
""",("Beachside Resort","Ernakulam","Lekshmi P",1234567890))
conn.commit()

curs.execute("""INSERT INTO VENUES (VENUE_NAME,LOCATION,OWNER_NAME,OWNER_CONTACT) VALUES(?,?,?,?)
""",("Relish","Thiruvananthapuram","Sharon",1278908839))
conn.commit()

curs.execute("""INSERT INTO VENUES (VENUE_NAME,LOCATION,OWNER_NAME,OWNER_CONTACT) VALUES(?,?,?,?)
""",("Doshadow Beach Resort","Alappuzha","Prasad",1271123409))
conn.commit()

curs.execute("""INSERT INTO VENUES (VENUE_NAME,LOCATION,OWNER_NAME,OWNER_CONTACT) VALUES(?,?,?,?)
""",("Golden Horizon Retreat","Ernakulam","Catherine",8482914477))
conn.commit()

curs.execute("""INSERT INTO VENUES (VENUE_NAME,LOCATION,OWNER_NAME,OWNER_CONTACT) VALUES(?,?,?,?)
""",("Whispering Oaks","Idukki","Dcunia",8899004477))
conn.commit()

curs.execute(""" CREATE TABLE IF NOT EXISTS BOOKINGS 
                 (BOOKING_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 VENUE_NAME TEXT,
                 VENUE_ID INTEGER,
                 CUSTOMER_NAME TEXT,
                 CUSTOMER_PHONE INTEGER,
                 FROM_DATE TEXT,
                 TO_DATE TEXT,
                 FOREIGN KEY (VENUE_NAME) REFERENCES VENUES(VENUE_NAME),
                 FOREIGN KEY (VENUE_ID) REFERENCES VENUES(VENUE_ID));
         
             """)
conn.commit()
conn.close()






conn.commit()
conn.close()

