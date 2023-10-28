from dotenv import load_dotenv
from pypdf import PdfReader
import os
import time
import openai

load_dotenv()

def get_test_cases(new_text):
    openai.api_key  = os.getenv("OPENAI_API_KEY")
    testcases = ''
    def get_answer(prompt, model="gpt-3.5-turbo"):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]

    for i in range(0, len(new_text)):
        prompt = f"""Provide me the test cases which should be tagged based on the product feature, priority, severity and 
        to be collected in respective test suites for given Product Requirement Document.
        I will give you content of the same from each pages, beginning to end.
        Don't be conversational. Content is shared below, delimited with triple backticks:
        ```{new_text[i]}```
        """
        try:
            response = get_answer(prompt)
        except:
            response = get_answer(prompt)
        testcases = testcases + ' ' + response + '\n\n'
        time.sleep(19)
    return testcases

# ------------------Generation of TestCase via uploading pdf file----------------------------------- #
def get_test_cases_for_pdf_prd(pdfFileObject):
    pdf_reader = PdfReader(pdfFileObject)
    text = []

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
    return get_test_cases(new_text)


def get_tokens(input_string):
    new_text = []
    max_words_per_phrase = 3000
    words = input_string.split()
    phrase = ""
    word_count = 0
    for word in words:
        if word_count + 1 <= max_words_per_phrase:
            phrase += " " + word
            word_count += 1
        else:
            new_text.append(phrase.strip())
            phrase = word
            word_count = 1
    new_text.append(phrase.strip())
    return new_text


# ------------------Generation of TestCase via uploading using text file----------------------------------- #
def get_test_cases_for_text_prd(txtfile):
    new_text = get_tokens(txtfile)
    return get_test_cases(new_text)


# ------------------Generation of TestCase via uploading Doc file----------------------------------- #
def get_test_cases_for_doc_prd(txtfile):
    new_text = get_tokens(txtfile)
    return get_test_cases(new_text)