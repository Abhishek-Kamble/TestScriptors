import streamlit as st
from streamlit_option_menu import option_menu
import time

# ----Package to load imageFile---#
from PIL import Image

# ---Package to read Docx file---#
import docx2txt

import backend

# ----------Function to load images-----------------#
def load_image(image_file):
    image = Image.open(image_file)
    return image


def main():
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["DocumentFiles", "Text"],
        )
    testCases = ""
    # -------------------------------------------DocumentFiles Menu----------------------------------------------------#
    if selected == "DocumentFiles":
        st.subheader(selected)
        file = st.file_uploader("Upload Document", type=["pdf", "docx", "txt"])
        if st.button("Process"):
            if file is not None:

                # --------------Process TextFile-------------------#
                if file.type == 'text/plain':
                    raw_text = file.read()
                    raw_text = str(file.read(), "utf-8")
                    st.write("Possible TestCases")
                    # with st.spinner('Wait for it...'):
                    #     time.sleep(100)
                    st.write(raw_text)
                # --------------Process PdfFile-------------------#
                elif file.type == "application/pdf":
                    try:
                        st.write("Possible TestCases")
                        # with st.spinner('Wait for it...'):
                        #     time.sleep(100)
                        testCases = backend.getTestCasesForPdfPrd(file)
                        st.write(testCases)
                    except:
                        st.write("None")
                # --------------Process DocFile-------------------#
                else:
                    raw_text = docx2txt.process(file)
                    st.write("Possible TestCases")
                    # with st.spinner('Wait for it...'):
                    #     time.sleep(100)
                    st.write(raw_text)


    # -------------------------------------------Text Menu---------------------------------------------------------#
    elif selected == "Text":
        st.subheader(selected)
        txt = st.text_area(
            label="Provide PRD as a text here",
            height=200,
            max_chars=10000,
            placeholder="Write here...."
        )
        if st.button("Process"):
            st.write("Possible TestCases")
            # with st.spinner('Wait for it...'):
            #     time.sleep(100)
            testCases = backend.getTestCasesForTextPrd(txt)
            st.write(testCases)




    # ------------------------------------------ImageFiles Menu-----------------------------------------------------#
    # elif selected == "ImageFiles":
    #     st.subheader(selected)
    #     image_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
    #     if st.button("Process"):
    #         st.write("Preview")
    #         if image_file:
    #             st.image(load_image(image_file))


if __name__ == '__main__':
    main()
