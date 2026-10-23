# HW7: Software Testing & Automated CI/CD Pipeline

本專案為軟體工程作業 **HW7**，旨在實作完整的三層軟體測試架構（單元測試、系統/API 測試、E2E 無頭瀏覽器測試），並透過 GitHub Actions 實現自動化持續整合（CI）。

---

## 📂 專案目錄結構

```text
HW7/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions 自動化測試設定
└── python-app/
    ├── app.py              # Flask 微服務後端
    ├── requirements.txt    # 專案相依套件
    └── tests/
        ├── test_unit.py    # 1. 單元測試 (Server 路由與回應)
        ├── test_system.py  # 2. 系統測試 (Web API 互動)
        └── test_e2e.py     # 3. E2E 測試 (Playwright 無頭瀏覽器)