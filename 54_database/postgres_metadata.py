import psycopg2

try:
    connect_str = "dbname='dvdrental' user='dvduser' host='localhost' " + \
                  "password='dvdpassword'"
    query_string="""select table_name from information_schema.tables  
                    WHERE table_schema='public' 
                    AND table_type='BASETABLE'
                 """
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    cursor.execute(query_string)
    rows = cursor.fetchall()
    print(rows)
    print(type(rows))
    print(len(rows))
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)
