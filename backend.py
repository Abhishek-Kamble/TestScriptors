from dotenv import load_dotenv
from pypdf import PdfReader
import os
import time
import openai

load_dotenv()

<<<<<<< HEAD

# ------------------Generation of TestCase via uploading pdf file----------------------------------- #
def getTestCasesForPdfPrd(pdfFileObject):
    openai.api_key = os.getenv("OPENAI_API_KEY")
=======
# ------------------Generation of TestCase via uploading pdf file----------------------------------- #
def getTestCasesForPdfPrd(pdfFileObject):
    openai.api_key  = os.getenv("OPENAI_API_KEY")
>>>>>>> 1a339c385779aae0e9300c1a0c4987939348a255
    pdfReader = PdfReader(pdfFileObject)
    text = []
    testCases = ''

    for i in range(0, len(pdfReader.pages)):
        pageObj = pdfReader.pages[i].extract_text()
        pageObj = pageObj.replace('\t\r', '')
        pageObj = pageObj.replace('\xa0', '')
        text.append(pageObj)
<<<<<<< HEAD

    def joinMultiplePages(lst, pages):
        newText = []
        for i in range(0, len(lst), pages):
            newText.append(''.join(lst[i:i + pages]))
=======
        
    def joinMultiplePages(lst, pages):
        newText = []
        for i in range(0, len(lst), pages):
            newText.append(''.join(lst[i:i+pages]))
>>>>>>> 1a339c385779aae0e9300c1a0c4987939348a255
        return newText

    newText = joinMultiplePages(text, 3)

    def getAnswer(prompt, model="gpt-3.5-turbo"):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
<<<<<<< HEAD
            model=model,
            messages=messages,
            temperature=0,  # this is the degree of randomness of the model's output
=======
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
>>>>>>> 1a339c385779aae0e9300c1a0c4987939348a255
        )
        return response.choices[0].message["content"]

    for i in range(0, len(newText)):
        prompt = f"""Provide me the test cases which should be tagged based on the product feature,priority,severity and to be collected in respective test suites for given Product Requirement Document.
        I will give you content of the same from each pages, beginning to end.
        Don't be conversational. Content is shared below, delimited with triple backticks:
        ```{newText[i]}```
        """
        try:
            response = getAnswer(prompt)
        except:
            response = getAnswer(prompt)
        print(response)
        testCases = testCases + ' ' + response + '\n\n'
        time.sleep(19)
    return testCases


<<<<<<< HEAD
=======


>>>>>>> 1a339c385779aae0e9300c1a0c4987939348a255
# ------------------Generation of TestCase via uploading using text file----------------------------------- #
def getTestCasesForTextPrd(txtfile):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    def getAnswer(prompt, model="gpt-3.5-turbo"):
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
        response = getAnswer(prompt)
    except:
        response = getAnswer(prompt)
<<<<<<< HEAD
    testCases = ""
    print(response)
    testCases = testCases + ' ' + response + '\n\n'
    time.sleep(19)
    return testCases
=======
    testCases=""
    print(response)
    testCases = testCases + ' ' + response + '\n\n'
    time.sleep(19)
    return testCases

>>>>>>> 1a339c385779aae0e9300c1a0c4987939348a255
