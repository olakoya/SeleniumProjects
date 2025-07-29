````markdown
# Selenium Web Automation Projects

This repository contains a collection of Selenium-based automation scripts developed as part of my ongoing upskilling, continuous learning, and real-world test automation practice.

These projects focus on automating various web applications and test scenarios using Python, Selenium WebDriver, and supporting tools.

---

## 🚀 Project Overview

- **Tech Stack:** Python + Selenium WebDriver  
- **Frameworks Used:** Pytest / Unittest / Robot Framework (based on individual project)  
- **Browsers Automated:** Chrome, Firefox (using WebDriverManager)  
- **Execution:** Locally and via command line  
- **Reporting:** HTML reports / CLI output  

---

## 📂 Project Structure

```text
SeleniumProjects/
├── tests/
│   ├── test_login_functionality.py
│   ├── test_search_feature.py
│   └── test_shopping_cart.py
├── pages/
│   ├── login_page.py
│   ├── home_page.py
│   └── cart_page.py
├── utils/
│   └── read_config.py
├── reports/
│   └── test_report.html
├── conftest.py
├── requirements.txt
└── README.md
````

---

## ✅ Features Covered

* ✅ Login page automation with positive/negative test cases
* ✅ Search field validation with dynamic waits
* ✅ Add/remove items from shopping cart
* ✅ Screenshot capture on failure
* ✅ Use of Page Object Model (POM) for code reusability
* ✅ Config-driven browser and URL setup

---

## 🧪 Tools & Libraries

* `selenium` – Web automation library
* `pytest` – Testing framework
* `webdriver-manager` – Auto-manage browser drivers
* `pytest-html` – Generate test reports
* `configparser` – Handle environment configs

---

## 🖥️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/SeleniumProjects.git
cd SeleniumProjects
```

2. Set up the environment:

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

3. Run the tests:

```bash
pytest --html=reports/report.html
```

---

## 📸 Screenshots

Screenshots from the test executions, e.g., login test passed, cart test failed with screenshots captured can be found in each day folder.

---

## 🔍 What I Learned

* Building scalable automation frameworks from scratch
* Implementing POM to keep tests maintainable
* Handling synchronization issues using explicit waits
* Generating HTML reports and debugging via logs/screenshots
* Writing reusable utility functions and configuration handling

---

