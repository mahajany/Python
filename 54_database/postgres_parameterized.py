import psycopg2

try:
    connect_str = "dbname='dvdrental' user='dvduser' host='localhost' " + \
                  "password='dvdpassword'"
    query_string="""select CITy.city, Country.country       
                      from city, country 
                     where city.country_id in (%s,%s) 
                        or country = %s 
                       and CITY.country_id = country.country_id"""
    query_tuple=(44,102,'United States')
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    ##cursor.execute('select CITy.city, Country.country from city, country where city.country_id in (%s,%s) or country = %s and CITY.country_id = country.country_id',query_tuple)
    cursor.execute(query_string, query_tuple)
    rows = cursor.fetchall()
    print(rows)
    print(type(rows))
    print(len(rows))
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)
