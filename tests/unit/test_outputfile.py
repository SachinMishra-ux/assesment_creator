import pytest
from assesment_creator.helper import output_file

test_data = [
    ("abc", 'abc.docx'),
    ("test1.docx", 'test1.docx'),
    ("abc1", 'abc1.docx'),
    ("abc.doc", 'abc.docx'),
    ("something", 'something.docx')
]

@pytest.mark.parametrize("file_name, response", test_data)
def test_output_file(file_name, response):
    assert output_file(file_name) == response