from src.app.core.tokenizer import Tokenizer

def test_add():
    words = Tokenizer("Amit Kumar Giri")
    assert words.get_words()[0] == "Amit"
    assert words.get_words()[1] == "Kumar"
    assert words.get_words()[2] == "Giri"