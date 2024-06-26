# Import the required modules
import mysql.connector
import base64
from PIL import Image
import io


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
w = '4'
query = "SELECT QR FROM penut_tokenstorage WHERE id_number=27461501745267184763129482"

# Execute the query to get the file
cursor.execute(query)

data = cursor.fetchall()

# The returned data will be a list of list
image = data[0][0]

# Decode the string
binary_data = base64.b64decode(image)

# Convert the bytes into a PIL image
image = Image.open(io.BytesIO(binary_data))

# Display the image
image.save("save.jpeg")

input()
