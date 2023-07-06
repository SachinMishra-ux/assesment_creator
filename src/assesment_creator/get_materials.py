from assesment_creator.logger import logger
from assesment_creator.cutom_exception import InvalidURLException
from assesment_creator.helper import *
from ensure import ensure_annotations

import requests
from bs4 import BeautifulSoup
from time import sleep

#url= "https://docs.google.com/forms/d/1WLfwaz1fuiueMGE8iEigwjZSP2HEUPGlyIWE9QNYhpg/edit"


@ensure_annotations
def get_data(link: str) -> list:
    page= requests.get(link)
    sleep(3)
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find_all(class_='geS5n')
    content= [pair.text for pair in content]
    return content

@ensure_annotations
def create_assesment(form_link:str, file_name:str) -> None:
    global output_file = ""
    try:
        if form_link and file_name is None:
            raise InvalidURLException("Url or file_name cannot be empty")
        else:
            splitted_file_name = file_name.split(".")

            if "." in file_name and splitted_file_name[-1] != "docx" : 
                output_file = splitted_file_name[0] + ".docx"

            elif "." not in file_name:
                output_file = file_name + ".docx"

            content= get_data(form_link)
            if content:
                questions, options= filter_qno(content)
                create_docx(questions, options, file_name)
                print(f"Scraping done successfully! Check {file_name}\nThank you! \\m/")
            else:
                print("No data found! Please check the link provided")   
                
    except Exception as e:
        print(e)

