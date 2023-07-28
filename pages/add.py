import streamlit as st
import easyocr
import mysql.connector
import cv2
import numpy as np 

st.title("Bizcard Add Your Business card")


# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="ocr",
    auth_plugin="mysql_native_password")

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Create a table to store the business card information
mycursor.execute("CREATE TABLE IF NOT EXISTS businesscard (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), job_title VARCHAR(255), address VARCHAR(255), postcode VARCHAR(255), phone VARCHAR(255), email VARCHAR(255), website VARCHAR(255), company_name VARCHAR(225))")

# Create an OCR object to read text from the image
reader = easyocr.Reader(['en'])


#display 

st.markdown(
        f"""    
        <h3 style='color: #f50505; font-size: 48px;'>Extracting Business Card Data with OCR</h3>    
        """,
        unsafe_allow_html=True)

# Create a file uploader widget
uploaded_file1 = st.file_uploader("Add a business card images", type=["jpg", "jpeg", "png"])

if uploaded_file1 is not None:
        # Read the image using OpenCV
        image = cv2.imdecode(np.fromstring(uploaded_file1.read(), np.uint8), 1)
        # Display the uploaded image
        st.image(image, caption='Uploaded business card image', use_column_width=True)
        # Create a button to extract information from the image
        if st.button('Extract Information'):
            # Call the function to extract the information from the image
            bounds = reader.readtext(image, detail=0)
            # Convert the extracted information to a string
            text = "\n".join(bounds)
            # Insert the extracted information and image into the database
            sql = "INSERT INTO bus(name, job_title, address, postcode, phone, email, website, company_name) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (bounds[0], bounds[1], bounds[2], bounds[3], bounds[4], bounds[5], bounds[6], bounds[7])
            mycursor.execute(sql, val)
            mydb.commit()
            # Display a success message
            st.success("Business card information added to database.")