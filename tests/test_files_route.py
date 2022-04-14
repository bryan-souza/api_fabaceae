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
def test_image():
    image = Path(TEST_PHOTOS_PATH, 'Caule10LL.jpg')
    return image

def test_files_route(test_image):
    response = client.post(
        '/files',
        files={ 'file': open(test_image, 'rb') }
    )

    assert response.status_code == 200
    assert response.json() == {'filename': 'Caule10LL.jpg'}