# Assesment_Creator Python Package.

Steps: Install the Python package via pip
```
pip install assesment-creator
```
1. Import the package and call assesment_creator API method.

```python
''' 
url_link = "https://docs.google.com/forms/d/1WLfwaz1fuiueMGE8iEigwjZSP2HEUPGlyIWE9QNYhpg/edit"

filename = abc.docx
'''
from assesment_creator import create_assesment
create_assesment(url_link,filename)
```