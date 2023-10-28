# Test cases generator

Test cases generator application is developed using python.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required libraries.

```bash
pip install streamlit
pip install streamlit_option_menu
pip install docx2txt
pip install pypdf
pip install openai
pip install python-dotenv
```

## Usage
[ Generate openai API key and copy it](https://platform.openai.com/account/api-keys)

Create a .env file in the root directory.

Add this environment variable - OPENAI_API_KEY and assign copied API key to this variable.

Run following command in terminal.

```bash
streamlit run UI.py
```

Application will be opened in the browser, if not opened, copy the URL provided in the terminal and paste in the browser's new tab.