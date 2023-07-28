import streamlit as st
import easyocr
import mysql.connector
import pandas as pd


st.set_page_config(
    page_title="Bizcard app",
    page_icon="📇",
)

st.title("Bizcard View Your Business card")

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
uploaded_file2 = st.file_uploader("View a business card images", type=["jpg", "jpeg", "png"])

# Display the stored business card information
mycursor.execute("SELECT * FROM bus")
result = mycursor.fetchall()
df = pd.DataFrame(result, columns=['id','name', 'job_title', 'address', 'postcode', 'phone', 'email', 'website', 'company_name'])
st.write(df)


