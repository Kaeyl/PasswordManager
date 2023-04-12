import psycopg2

def view():
    try:
        con = psycopg2.connect(
            database="password_manager",
            user="postgres",
            password="",
            host="localhost",
            port=''
        )
        cursor_obj = con.cursor()
        cursor_obj.execute("SELECT * FROM password_table")
        result = cursor_obj.fetchall()
        return result
        con.close()
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into table", error)
    finally:
        # closing database connection.
        if con:
            cursor_obj.close()
            con.close()

def add_password(password, email, username, url, app):
    try:
        con = psycopg2.connect(
            database="password_manager",
            user="postgres",
            password="",
            host="localhost",
            port=''
        )
        cursor_obj = con.cursor()
        postgres_insert_query = """ INSERT INTO password_table (user_passwd, user_email, username, url, app_name) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (password, email, username, url, app)
        cursor_obj.execute(postgres_insert_query, record_to_insert)
        con.commit()
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into table", error)
    finally:
        # closing database connection.
        if con:
            cursor_obj.close()
            con.close()
            print("PostgreSQL connection is closed")

def edit_password(position_id, password):
    try:
        con = psycopg2.connect(
            database="password_manager",
            user="postgres",
            password="",
            host="localhost",
            port=''
        )
        cursor_obj = con.cursor()
        postgres_insert_query = """UPDATE password_table SET user_passwd = (%s) WHERE (%s) = p_id;"""
        record_to_insert = (password, position_id )
        cursor_obj.execute(postgres_insert_query, record_to_insert)
        con.commit()
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into table", error)
    finally:
        # closing database connection.
        if con:
            cursor_obj.close()
            con.close()
            print("PostgreSQL connection is closed")

def edit_row(password, email, username, url, app, position_id):
    try:
        con = psycopg2.connect(
            database="password_manager",
            user="postgres",
            password="",
            host="localhost",
            port=''
        )
        cursor_obj = con.cursor()
        postgres_insert_query = """UPDATE password_table SET user_passwd = (%s), user_email = (%s), username = (%s), url = (%s), app_name = (%s) WHERE (%s) = p_id;"""
        record_to_insert = (password ,email,username, url, app, position_id)
        cursor_obj.execute(postgres_insert_query, record_to_insert)
        con.commit()
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into table", error)
    finally:
        # closing database connection.
        if con:
            cursor_obj.close()
            con.close()
            print("PostgreSQL connection is closed")

def delete_password(user_selection, postgres_insert_query):
    try:
        con = psycopg2.connect(
            database="password_manager",
            user="postgres",
            password="",
            host="localhost",
            port=''
        )
        cursor_obj = con.cursor()
        cursor_obj.execute(postgres_insert_query, user_selection)
        con.commit()
    except (Exception, psycopg2.Error) as error:
        print("Failed to remove record into table", error)
    finally:
        # closing database connection.
        if con:
            cursor_obj.close()
            con.close()
            print("PostgreSQL connection is closed")
