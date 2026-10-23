import pytest
from app import app


@pytest.fixture
def client():
  app.config["TESTING"] = True
  with app.test_client() as client:
    yield client


def test_index_route(client):
  """單元測試：驗證伺服器首頁可正常載入"""
  response = client.get("/")
  assert response.status_code == 200
  assert b"HW7" in response.data