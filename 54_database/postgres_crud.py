import psycopg2

try:
    connect_str = "dbname='dvdrental' user='dvduser' host='localhost' " + \
                  "password='dvdpassword'"
    drop_query="""if exists drop table fans"""
    create_query="""CREATE TABLE fans (
     id          SERIAL PRIMARY KEY,
    name        char(40),
    location    char(40)
);"""
    insert_query="""insert into fans(name,     location) values
                                   ('Yogesh', 'FDB'),
                                   ('Bradley', 'CAL'),
                                   ('Cooper', 'HWD'),
                                   ('Harrison', 'NYC')"""
    select_one_query="""select * from fans where name='Cooper'""" 
    select_all_query="""select * from fans""" 

    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
    # create a new table with a single column called "name"
    cursor.execute(create_query)
    cursor.execute(insert_query)
    cursor.execute(select_one_query)
    rows = cursor.fetchall()
    id_to_be_deleted=rows[0][0]
    delete_query="delete from fans where id = "+str(id_to_be_deleted)
    cursor.execute(delete_query)
    cursor.execute(select_all_query)
    rows = cursor.fetchall()
    print(rows)
    print(type(rows))
    print(len(rows))
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print("...or may be some SQL Error!!!")
    print(e)
