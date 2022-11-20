import streamlit as st
import pyqrcode
import png

st.title('QR-code generator app')
form = st.form(key='website-link')
link = form.text_area('Enter your website-link')
submit = form.form_submit_button('Submit')

if submit:
    qr_code = pyqrcode.create(link)
    qr_code.png("image.png", scale=5)
    with open("image.png", "rb") as file:
        btn = st.download_button(label="Download image",data=file,file_name="IMAGE.png",mime="image/png")