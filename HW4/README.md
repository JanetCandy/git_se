# Git 協作與開發流程指南：Fork, Branch, Merge & Pull Request

本專案採用 **VS Code + Python** 環境開發，並詳細紀錄如何對上游母專案進行貢獻。內容完整涵蓋 Fork 專案、建立開發分支、本地合併變更、VS Code 整合操作以及發送 Pull Request 的標準流程。

---

## 專案關聯連結

- **母專案（Upstream Repository）**：[se-test-examples/git-examples (main)](https://github.com/se-test-examples/git-examples/commits/main/)
- **開發分支（Feature/Develop Branch）**：[se-test-examples/git-examples (developGitBranch)](https://github.com/se-test-examples/git-examples/commits/developGitBranch)
- **子專案 / 個人 Fork 專案（Origin Repository）**：[ccckmit/git-examples (main)](https://github.com/ccckmit/git-examples/commits/main/)

---

## 本專案採用的 Git 工作流架構

本操作流程主要採用 **Forking Workflow（Fork-and-Pull 模式）**，並融合了 **GitHub Flow** 的分支管理概念（參考自 *阮一峰《Git 工作流程指南》* 與 *ByteByteGo《How Does Git Work?》*）：

1. **Forking Workflow**：適用於開源專案或權限劃分嚴格的團隊。開發者無權直接 push 到母專案（Upstream），必須先 Fork 到個人倉庫（Origin），開發完成後再透過 Pull Request（PR）由團隊審查（Code Review）後合併。
2. **Feature Branching**：所有功能開發與修改皆不在主分支（`main`）直接進行，而是開闢獨立的開發分支（如 `developGitBranch`），確保主線程式碼隨時保持穩定。

---

## 完整實作步驟與指令紀錄

---

### 1. 複製母專案（Fork & Clone）

**【GitHub Web 動作】**
1. 開啟母專案頁面：`https://github.com/se-test-examples/git-examples`
2. 點擊右上角 **「Fork」** 按鈕，建立個人的遠端專案 `ccckmit/git-examples`。

**【CLI 實際執行指令】**
```bash
# Clone 個人 Fork 的子專案至本地
1632  git clone git@github.com:ccckmit/git-examples.git
1634  cd git-examples

# 新增檔案並提交 Fork 紀錄
1635  git add .
1636  git commit -m "add ccckmitFork.md"
1637  git push