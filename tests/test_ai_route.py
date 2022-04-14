# Built-ins
from pathlib import Path

# Internals
from app.server import app

# 3rd party
import pytest
from fastapi.testclient import TestClient

APP_ROOT_PATH = Path('app').resolve()
TEST_PHOTOS_PATH = Path(APP_ROOT_PATH, 'cerebrum', 'fotos', 'testes')

client = TestClient(app)

@pytest.fixture
def filename():
    _filename = 'Caule10LL.jpg'
    image = Path(TEST_PHOTOS_PATH, _filename)
    client.post(
        '/files',
        files={ 'file': open(image, 'rb') }
    )

    return _filename

def test_ai(filename):
    response = client.post(
        '/ai',
        json={'filename': filename}
    )
    data = response.json()

    assert response.status_code == 200, 'Invalid request'
    assert data.get('plant') is not None, 'Plant field not present'
    assert data.get('accuracy') is not None, 'Accuracy field not present'
    assert type(data['plant']) == str
    assert type(data['accuracy']) == float

def test_ai_without_uploading_image():
    response = client.post(
        '/ai',
        json={'filename': 'ImageNotUploaded.jpg'}
    )
    
    assert response.status_code == 404, 'Invalid request'
    assert response.json() == {'detail': 'File not found'}