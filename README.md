# 📌 POM_LoginTestProject

一個基於 Python + Pytest + Selenium 的自動化測試專案，採用 Page Object Model（POM）架構設計，主要用於模擬 MOMO 登入流程的功能測試。

---

## 📁 專案架構說明

```
POM_LoginTestProject/
├── pages/                  # Page Object 元件定義
│   └── login_page.py
├── tests/                  # 測試案例區
│   └── test_login.py
├── conftest.py             # pytest fixture 定義
├── pytest.ini              # Pytest 設定檔
├── req.txt                 # 套件需求清單 (pip install -r req.txt)
├── install_requirements.bat # 一鍵安裝套件腳本
├── runtest.bat             # 一鍵執行測試腳本
└── README.md               # 本文件
```

---

## 🚀 執行步驟（Windows）

1. **安裝必要套件**（打開 Git Bash 或 CMD 執行）：

```bash
./install_requirements.bat
# 或手動執行：
pip install -r req.txt
```

2. **執行測試**：

```bash
./runtest.bat
# 或直接使用：
pytest
```

---

## 🧪 技術說明

- 測試框架：Pytest
- 自動化工具：Selenium
- 架構設計：Page Object Model
- 測試瀏覽器：Chrome（需安裝 ChromeDriver 並設好環境變數）

---

## 📖 常見指令

| 指令 | 說明 |
|------|------|
| `pytest` | 執行測試 |
| `pytest --html=report.html` | 產出 HTML 測試報告（需先安裝 `pytest-html`） |
| `git status` | 查詢 git 狀態 |
| `git commit -m "說明"` | 提交版本說明 |
