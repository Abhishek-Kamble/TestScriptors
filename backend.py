from dotenv import load_dotenv
from pypdf import PdfReader
import os
import time
import openai

load_dotenv()

# ------------------Generation of TestCase via uploading pdf file----------------------------------- #
def get_test_cases_for_pdf_prd(pdfFileObject):
    openai.api_key  = os.getenv("OPENAI_API_KEY")
    pdf_reader = PdfReader(pdfFileObject)
    text = []
    testcases = ''

    for i in range(0, len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[i].extract_text()
        page_obj = page_obj.replace('\t\r', '')
        page_obj = page_obj.replace('\xa0', '')
        text.append(page_obj)
        
    def join_multiple_pages(lst, pages):
        new_text = []
        for i in range(0, len(lst), pages):
            new_text.append(''.join(lst[i:i+pages]))
        return new_text

    new_text = join_multiple_pages(text, 3)

    def get_answer(prompt, model="gpt-3.5-turbo"):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]

    for i in range(0, len(new_text)):
        prompt = f"""Provide me the test cases which should be tagged based on the product feature,priority,severity and to be collected in respective test suites for given Product Requirement Document.
        I will give you content of the same from each pages, beginning to end.
        Don't be conversational. Content is shared below, delimited with triple backticks:
        ```{new_text[i]}```
        """
        try:
            response = get_answer(prompt)
        except:
            response = get_answer(prompt)
        print(response)
        testcases = testcases + ' ' + response + '\n\n'
        time.sleep(19)
    return testcases




# ------------------Generation of TestCase via uploading using text file----------------------------------- #
def get_test_cases_for_text_prd(txtfile):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    def get_answer(prompt, model="gpt-3.5-turbo"):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,  # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]

    prompt = f"""Provide me the test cases which should be tagged based on the product feature,priority,severity and to be collected in respective test suites for given Product Requirement Document.
    I will give you content of the same from each pages, beginning to end.
    Don't be conversational. Content is shared below, delimited with triple backticks:
    ```{txtfile}```
    """
    try:
        response = get_answer(prompt)
    except:
        response = get_answer(prompt)
    testcases=""
    print(response)
    testcases = testcases + ' ' + response + '\n\n'
    time.sleep(19)
    return testcases


# ------------------Generation of TestCase via uploading Doc file----------------------------------- #
def get_test_cases_for_doc_prd(txtfile):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    def get_answer(prompt, model="gpt-3.5-turbo"):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,  # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]

    prompt = f"""Provide me the test cases which should be tagged based on the product feature,priority,severity and to be collected in respective test suites for given Product Requirement Document.
    I will give you content of the same from each pages, beginning to end.
    Don't be conversational. Content is shared below, delimited with triple backticks:
    ```{txtfile}```
    """
    try:
        response = get_answer(prompt)
    except:
        response = get_answer(prompt)
    testcases=""
    print(response)
    testcases = testcases + ' ' + response + '\n\n'
    time.sleep(19)
    return testcases


