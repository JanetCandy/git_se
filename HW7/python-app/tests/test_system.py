import pytest
from app import app, messages_db


@pytest.fixture
def client():
  app.config["TESTING"] = True
  messages_db.clear()
  with app.test_client() as client:
    yield client


def test_api_workflow(client):
  """系統測試：測試 Web API 的 POST 與 GET 互動"""
  # 測試 POST
  res_post = client.post("/api/messages", json={"content": "System Test Msg"})
  assert res_post.status_code == 201
  data = res_post.get_json()
  assert data["status"] == "success"
  assert data["content"] == "System Test Msg"

  # 測試 GET
  res_get = client.get("/api/messages")
  assert res_get.status_code == 200
  all_msgs = res_get.get_json()
  assert "System Test Msg" in all_msgs