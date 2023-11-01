import streamlit as st
from streamlit_option_menu import option_menu
import time
import backend
import base64
from datetime import datetime

# ----Package to load imageFile---#
from PIL import Image

# ---Package to read Docx file---#
import docx2txt

# ----------Function to load images-----------------#
def load_image(image_file):
    image = Image.open(image_file)
    return image

def text_downloader(raw_text):
    timestr = datetime.now().strftime("%Y%m%d-%H%M%S")
    b64 = base64.b64encode(raw_text.encode()).decode()
    new_filename = "testcases_{}_.txt".format(timestr)
    st.markdown("#### Download File ###")
    href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Download</a>'
    st.markdown(href, unsafe_allow_html=True)

def main():
    st.title("Test Cases Generator")
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["Document Files", "Text"],
        )

    # Create a session state dictionary
    session_state = st.session_state
    if not hasattr(session_state, 'testcases'):
        session_state.testcases = ""
    additional_testcases = ""

    # Initialize the elaborated test case
    elaborated_testcase = ""

    # -------------------------------------------DocumentFiles Menu----------------------------------------------------#
    if selected == "Document Files":
        # st.subheader(selected)
        file = st.file_uploader("Upload PRD", type=["pdf", "docx", "txt"])
        if st.button("Process"):
            if file is not None:
                # --------------Process TextFile-------------------#
                if file.type == 'text/plain':
                    try:
                        raw_text = str(file.read(), "utf-8")
                        st.write("Possible TestCases")
                        session_state.testcases = backend.get_test_cases_for_text_prd(raw_text)
                        # text_downloader(session_state.testcases)
                        # st.write(session_state.testcases)
                    except:
                        st.write("None")
                # --------------Process PdfFile-------------------#
                elif file.type == "application/pdf":
                    try:
                        st.write("Possible TestCases")
                        session_state.testcases = backend.get_test_cases_for_pdf_prd(file)
                        # text_downloader(session_state.testcases)
                        # st.write(session_state.testcases)
                    except:
                        st.write("None")
                # --------------Process DocFile-------------------#
                else:
                    try:
                        raw_text = docx2txt.process(file)
                        st.write("Possible TestCases")
                        session_state.testcases = backend.get_test_cases_for_doc_prd(raw_text)
                        # text_downloader(session_state.testcases)
                        # st.write(session_state.testcases)
                    except:
                        st.write("None")

    # -------------------------------------------Text Menu---------------------------------------------------------#
    elif selected == "Text":
        # st.subheader(selected)
        txt = st.text_area(
            label="Provide PRD as a text here",
            height=200,
            max_chars=10000,
            placeholder="Write here...."
        )
        if st.button("Process"):
            try:
                st.write("Possible TestCases")
                session_state.testcases = backend.get_test_cases_for_text_prd(txt)
                    # text_downloader(additional_testcases)
                    # st.write(additional_testcases)
            except:
                st.write("None")

    with st.form("testcases_form"):
        if session_state.testcases:
            st.markdown("#### Generated Test Cases ###")
            text_downloader(session_state.testcases)
            st.write(session_state.testcases)

            st.title("Additional Prompt")
            user_input = st.text_input("Enter your query...", "")
            
            if st.form_submit_button("Elaborate on Test Case"):
                elaborated_testcase = backend.get_custom_test_cases(session_state.testcases, user_input)

    if elaborated_testcase:
        st.markdown("#### Elaborated Test Case ###")
        st.write(elaborated_testcase)

if __name__ == '__main__':
    main()
