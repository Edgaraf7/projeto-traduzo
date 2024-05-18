from src.models.history_model import HistoryModel


def test_request_history():
    data = HistoryModel.list_as_json()

    assert "Hello, I like videogame" in data
    assert "Do you love music?" in data
