import pytest
from assesment_creator.get_assesment import get_data
from assesment_creator.cutom_exception import InvalidURLException


outcome= [('[True or False] Regularization is a technique which makes slight modifications to the learning algorithm such that the model generalizes better.',
  ''),
 ('', 'True'),
 ('', 'False'),
 ('[True or False] The dense layer connects all the inputs and outputs of all the neurons in each layer.',
  ''),
 ('', 'True'),
 ('', 'False')]
good_URL_data = [
    ("https://docs.google.com/forms/d/1WLfwaz1fuiueMGE8iEigwjZSP2HEUPGlyIWE9QNYhpg/edit", outcome)
]

bad_URL_data = [
    ("https://www.youtube.com/watch?v=roO5VGxOw2sahesbf"),  # exception
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t"),  # exception
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t==22s"),  # exception
    ("https://www.youtube.com/watch?v=tku5zP1VzXA")
]

@pytest.mark.parametrize("URL, response", good_URL_data)
def test_get_data(URL, response):
    assert get_data(URL) == response

@pytest.mark.parametrize("URL", bad_URL_data)
def test_get_data_failed(URL):
    with pytest.raises(InvalidURLException):
        get_data(URL)