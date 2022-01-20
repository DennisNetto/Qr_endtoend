def pri(b):
    # Import the required modules
    import mysql.connector
    import base64

    # Create a connection
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password='password',
        database="tnstorage"  # Name of the database
    )

    # Create a cursor object
    cursor = mydb.cursor()

    # Prepare the query
    b = '"' + b + '"'
    query = 'SELECT privatekey FROM penut_tokenstorage WHERE hash= '
    query = query + b

    # Execute the query to get the file
    cursor.execute(query)

    data = cursor.fetchall()

    # The returned data will be a list of list
    image = data[0][0]

    # Decode the string
    binary_data = base64.b64decode(image)
    out = b[1:-1] + ".pem"
    file_out = open(out, "wb")
    file_out.write(binary_data)
