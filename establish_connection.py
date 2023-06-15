def establish_connection():

    import psycopg2
    conn = psycopg2.connect(
        database="tkinter",
        user="postgres",
        password="9841639491",
        host="127.0.0.1",
        port=5432
    )
    conn.autocommit = True
    print("Connection established successfully!!")
    cursor = conn.cursor()
    return cursor