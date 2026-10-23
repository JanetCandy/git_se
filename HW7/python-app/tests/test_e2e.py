import threading
import time
import pytest
from app import app
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module", autouse=True)
def run_server():
  """在測試啟動時背景執行 Flask 伺服器"""
  server_thread = threading.Thread(
      target=lambda: app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)
  )
  server_thread.daemon = True
  server_thread.start()
  time.sleep(1)  # 等待伺服器啟動


def test_e2e_user_workflow():
  """E2E 測試：無頭瀏覽器模擬點擊與輸入"""
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # 1. 連線到本地伺服器
    page.goto("http://127.0.0.1:5000")

    # 2. 檢查標題
    assert "Docker 微服務系統儀表板" in page.title()

    # 3. 填入資料並點擊送出
    page.fill("#msgInput", "Playwright E2E Automated Test")
    page.click("button:has-text('送出')")

    # 4. 驗證頁面是否成功渲染該筆資料
    page.wait_for_selector("text=Playwright E2E Automated Test")
    assert "Playwright E2E Automated Test" in page.content()

    browser.close()