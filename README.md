# OrangeHRM Selenium Pytest Automation Framework

This project is a Selenium Automation Framework developed using Python, Pytest, and Page Object Model (POM) architecture for automating the OrangeHRM application.

---

# 🚀 Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Explicit Waits
- Undetected ChromeDriver
- Git & GitHub

---

# 📁 Project Structure

```bash
self_python_automation_project/
│
├── configuration/
│   ├── __init__.py
│   ├── config.ini
│
├── page_objects/
│   ├── dashboard_page.py
│   ├── login.py
│   ├── pim_page.py
│
├── test_cases/
│   ├── conftest.py
│   ├── test_dashboard.py
│   ├── test_login.py
│   ├── test_pim.py
│
├── utilities/
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

# ✅ Automated Test Scenarios

## Login Module
- Login Page Title Validation
- Valid Login Validation

## Dashboard Module
- Left Menu Validation
- Dashboard Validation

## PIM Module
- Navigate to PIM
- Add Employee
- Validate Personal Details Page

---

# ⚙️ Framework Features

- Page Object Model Design Pattern
- Reusable Fixtures using Pytest
- Explicit Wait Implementation
- Cross Browser Support
- Dynamic Test Data Handling
- Screenshot Capture on Failure
- Scalable Framework Design

---

# 🛠️ Installation

## Clone Repository

```bash
git clone https://github.com/Rishi5225/self_python_automation_project.git
```

## Navigate to Project

```bash
cd self_python_automation_project
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Execute Tests

## Run on Chrome

```bash
pytest -v -s --browser chrome
```

## Run on Firefox

```bash
pytest -v -s --browser firefox
```

---

# 📌 Future Enhancements

- Allure Reporting
- Jenkins CI/CD Integration
- Parallel Execution
- Logging Utility
- BasePage Utility Layer
- Data Driven Framework
- API Automation Integration

---

# 👨‍💻 Author

Rishi Thorve

QA Automation Engineer

GitHub:
https://github.com/Rishi5225
