from dotenv import load_dotenv
from pypdf import PdfReader
import os
import time
import openai

load_dotenv()
def getTestCases(pdfFileObject):
    openai.api_key  = os.getenv("OPENAI_API_KEY")
    pdfReader = PdfReader(pdfFileObject)
    text = []
    testCases = ''

    for i in range(0, len(pdfReader.pages)):
        pageObj = pdfReader.pages[i].extract_text()
        pageObj = pageObj.replace('\t\r', '')
        pageObj = pageObj.replace('\xa0', '')
        text.append(pageObj)
        
    def joinMultiplePages(lst, pages):
        newText = []
        for i in range(0, len(lst), pages):
            newText.append(''.join(lst[i:i+pages]))
        return newText

    newText = joinMultiplePages(text, 3)

    def getAnswer(prompt, model="gpt-3.5-turbo"):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]

    for i in range(0, len(newText)):
        prompt = f"""Provide me the test cases collected in respective test suites for given Product Requirement Document.
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