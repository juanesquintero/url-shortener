from unittest.mock import patch
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.main import app
from app.db.models.url import URL
from app.db.conn import Base, engine
from app.shared.dependencies import get_db

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

url_mock = {
    'title': 'Test Title',
    'address': 'https://example-long.com/params-with?query=1231',
    'shorted': 'http://localhost:8000/test',
    'clicks': 0
}

@patch('app.services.urls.read_urls')
def test_list_all(mock_read_urls):
    mock_read_urls.return_value = [url_mock]
    response = client.get("/urls")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json().get('data'), list)
    assert response.json().get('detail') == 'All URLs fetched'

@patch('app.services.urls.read_shorted_url')
def test_get_one_by_shorted(mock_get_one):
    mock_get_one.return_value = URL(**url_mock)

    short_url = url_mock.get('shorted')
    response = client.get(f'/urls?short_url={short_url}')

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json().get('data'), dict)

@patch('app.services.urls.read_url')
def test_get_one_by_original(mock_get_one):
    mock_get_one.return_value = URL(**url_mock)
    original_url = url_mock.get('address')
    response = client.get(f"/urls/?original_url={original_url}")

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json().get('data'), dict)


@patch('app.controllers.urls.get_top_urls')
def test_list_top(mock_get_top_urls):
    mock_get_top_urls.return_value = [url_mock]

    response = client.get("/urls/top?limit=1")
    assert response.status_code == 200
    assert response.json() == {
        'detail': 'Top 1 URLs fetched',
        'data': [url_mock]
    }

@patch('app.controllers.urls.create_shorten_url')
@patch('app.controllers.urls.get_page_title')
def test_shorten_url(mock_get_page_title, mock_create_shorten_url):
    mock_get_page_title.return_value = url_mock.get('title')
    mock_create_shorten_url.return_value = URL(**url_mock)

    response = client.post("/urls/shorten", params={'original_url': url_mock.get('address')})
    assert response.status_code == 201
    assert response.json() == {
        'detail': 'URL shorten added successfully',
        'data': url_mock
    }
