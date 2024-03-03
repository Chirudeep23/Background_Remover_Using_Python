import streamlit as st
from PIL import Image
from rembg import remove
import io

st.title('Image Background Remover')
st.caption('_Developed By Chirudeep Amaraju_')

uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    removed = remove(image)
    removed = removed.convert("RGB")
    
    # Display the processed image
    st.image(removed, caption='Processed Image', use_column_width=True)

    # Save the image to a BytesIO object
    img_io = io.BytesIO()
    removed.save(img_io, format='JPEG')
    img_io.seek(0)

    # Create a link for downloading the image
    st.download_button(
        label="Download image",
        data=img_io,
        file_name='removed.jpg',
        mime='image/jpeg'
    )
    
st.subheader('Contact', divider='grey')
#Customisation of Contact icons
col1, col2, col3, col4 = st.columns(4)
with col1:
        st.link_button("GitHub", "https://github.com/Chirudeep23")
with col2:
        st.link_button("LinkedIn", "https://www.linkedin.com/in/chirudeep-amaraju-74aa6b259/")
with col3:
        st.link_button("Instagram","https://www.instagram.com/chirudeep_23/")

