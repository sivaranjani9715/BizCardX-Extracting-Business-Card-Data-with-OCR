import streamlit as st
import easyocr
import mysql.connector

st.title("Bizcard Update Your Business card")

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
uploaded_file = st.file_uploader("Upload a business card images", type=["jpg", "jpeg", "png"])

# Create a dropdown menu to select a business card to update
mycursor.execute("SELECT id, name FROM bus")
result = mycursor.fetchall()
business_cards = {}
for row in result:
    business_cards[row[1]] = row[0]
selected_card_name = st.selectbox("Select a business card to update", list(business_cards.keys()))
    
# Get the current information for the selected business card
mycursor.execute("SELECT * FROM bus WHERE name=%s", (selected_card_name,))
result = mycursor.fetchone()

# Display the current information for the selected business card
st.write("Name:", result[1])
st.write("Job Title:", result[2])
st.write("Address:", result[3])
st.write("Postcode:", result[4])
st.write("Phone:", result[5])
st.write("Email:", result[6])
st.write("Website:", result[7])
st.write("company_name:", result[8])

# Get new information for the business card
name = st.text_input("Name", result[1])
job_title = st.text_input("Job Title", result[2])
address = st.text_input("Address", result[3])
postcode = st.text_input("Postcode", result[4])
phone = st.text_input("Phone", result[5])
email = st.text_input("Email", result[6])
website = st.text_input("Website", result[7])
company_name = st.text_input("Company Name", result[8])

# Create a button to update the business card
if st.button("Update Business Card"):
    # Update the information for the selected business card in the database
    mycursor.execute("UPDATE bus SET name=%s, job_title=%s, address=%s, postcode=%s, phone=%s, email=%s, website=%s, company_name=%s WHERE name=%s", 
                         (name, job_title, address, postcode, phone, email, website, company_name, selected_card_name))
    mydb.commit()
    st.success("Business card information updated in database.")
