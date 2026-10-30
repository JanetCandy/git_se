# 🚀 Smart Task & Time Tracker (智慧型任務與工時追蹤系統)

本專案是一個遵循**軟體工程原則（Software Engineering Principles）**設計的 Python 專案，旨在協助使用者管理個人或團隊的專案任務、估算工時，並提供自動化的生產力分析報表。

---

## 🛠️ 軟體工程設計亮點

1. **高內聚與低耦合（Modular Design）**：
   - `models.py`：負責定義資料實體（Task）。
   - `storage.py`：實作**儲存庫模式（Repository Pattern）**，隔離資料儲存細節（JSON 序列化）。
   - `service.py`：封裝核心商業邏輯與統計計算。
2. **自動化單元測試（Unit Testing）**：
   - 採用 Python 內建 `unittest` 框架，涵蓋新增任務、狀態更新與生產力報表計算等核心功能的測試，確保程式碼品質與可維護性。

---

## 📂 專案結構

```text
task_tracker/
│
├── models.py          # 資料模型
├── storage.py         # 資料持久化儲存庫
├── service.py         # 商業邏輯與統計分析
├── test_tracker.py    # 單元測試檔
└── README.md          # 專案說明文件