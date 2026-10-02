#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Git SE Repository Inspector & Health Checker
功能：檢查專案目錄結構、分析 .gitignore 配置，並輸出驗證報告。
"""

import os
import sys
from pathlib import Path


def find_repo_root(start_path: Path) -> Path:
    """自動向上尋找包含 .git 或 .gitignore 的專案根目錄"""
    current = start_path.resolve()
    for parent in [current] + list(current.parents):
        if (parent / ".git").exists() or (parent / ".gitignore").exists():
            return parent
    return start_path.resolve()


def inspect_gitignore(root_path: Path) -> list:
    """讀取並解析 .gitignore 檔案中的規則清單"""
    gitignore_file = root_path / ".gitignore"
    if not gitignore_file.exists():
        return []

    rules = []
    with open(gitignore_file, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            # 忽略空行與註解
            if line and not line.startswith("#"):
                rules.append(line)
    return rules


def generate_report(root_path: Path, gitignore_rules: list) -> str:
    """生成專案結構與版控健康度分析報告"""
    report = []
    report.append("==========================================")
    report.append("  Git SE Repository Inspection Report")
    report.append("==========================================")
    report.append(f"Root Directory : {root_path}")
    report.append(f"Active Rules   : {len(gitignore_rules)} patterns found in .gitignore")
    report.append("------------------------------------------")

    # 檢查常見忽略目標
    key_targets = [".venv", "venv", "__pycache__", ".vscode", "requirements.txt"]
    report.append("Key Target Check:")
    for target in key_targets:
        target_path = root_path / target
        status = "Present" if target_path.exists() else "Not Found"
        report.append(f"  - {target:<18}: {status}")

    report.append("------------------------------------------")
    report.append("Inspection Completed Successfully.")
    return "\n".join(report)


def main():
    """主程式進入點"""
    # 取得當前腳本所在目錄的上層做為檢測點
    current_dir = Path(__file__).parent
    repo_root = find_repo_root(current_dir)

    rules = inspect_gitignore(repo_root)
    report_text = generate_report(repo_root, rules)

    print(report_text)


if __name__ == "__main__":
    main()
  
