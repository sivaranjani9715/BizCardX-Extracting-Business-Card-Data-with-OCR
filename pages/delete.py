import streamlit as st
import easyocr
import mysql.connector



st.title("Bizcard Delete Your Business card")

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
uploaded_file = st.file_uploader("Delete a business card image", type=["jpg", "jpeg", "png"])

# Create a dropdown menu to select a business card to delete
mycursor.execute("SELECT id, name FROM bus")
result = mycursor.fetchall()
business_cards = {}
for row in result:
    business_cards[row[0]] = row[1]
selected_card_id = st.selectbox("Select a business card to delete", list(business_cards.keys()), format_func=lambda x: business_cards[x])

# Get the name of the selected business card
mycursor.execute("SELECT name FROM bus WHERE id=%s", (selected_card_id,))
result = mycursor.fetchone()
selected_card_name = result[0]

# Display the current information for the selected business card
st.write("Name:", selected_card_name)
# Display the rest of the information for the selected business card

# Create a button to confirm the deletion of the selected business card
if st.button("Delete Business Card"):
    mycursor.execute("DELETE FROM bus WHERE name=%s", (selected_card_name,))
    mydb.commit()
    st.success("Business card information deleted from database.")

