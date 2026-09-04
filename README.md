# Playwright Python QA Automation Framework

A structured **Playwright** and **Python test** (pytest) automation project demonstrating UI and **REST API** testing against a locally hosted Flask application.

This project demonstrates best practices in UI test automation, including the Page Object Model (POM), data-driven testing, automatic screenshot capture, video recording, trace recording, logging, and GitHub Actions CI/CD.

The framework was developed as part of my continuous learning to strengthen my Playwright skills while leveraging my professional experience in Selenium, Python, and enterprise QA automation.

---

## Features

- Playwright with Python
- PyTest test framework
- UI test automation
- REST API test automation
- Page Object Model (POM)
- Data-driven testing using JSON
- Automatic screenshots on test failure
- Video recording
- Playwright Trace Viewer support
- HTML test reporting
- Flask-based System Under Test (SUT)
- Logging
- GitHub Actions CI/CD
- Easy to extend and maintain

---

## Project Structure

```text
Playwright_Python3_QA1/
│
├── .github/
│   └── workflows/
│       └── playwright.yml
│ 
├── app/
│   ├── app.py
│   ├── database.py
│   ├── models.py
│   ├── templates/
│   │   ├── login.html
│   │   └── users.html
│   └── static/
│       └── style.css
│
├── data/
│   └── users.json
├── models/
│   └── user.py
│
├── pages/
│   ├── login_page.py
│   └── home_page.py
│
├── api/
│   ├── users_api.py
│   └── auth_api.py
│
├── tests/
│   ├── ui/
│   │   ├── test_login.py
│   │   ├── test_invalid_login.py
│   │   └── test_search.py
│   │
│   └── api/
│       ├── test_users_api.py
│       ├── test_login_api.py
│       └── test_posts_api.py
│
├── utils/
│   ├── config.py
│   ├── json_reader.py
│   └── logger.py
│
├── screenshots/
├── videos/
├── traces/
│
├── report/
│
├── conftest.py
├── requirements.txt
├── pytest.ini
├── README.md
└── .gitignore
```

---

## Technologies

- Python 3.x
- Playwright
- PyTest
- Git
- GitHub Actions
- JSON
- HTML Report

---

## Framework Design

The framework follows a modular design that separates responsibilities:

- **Pages** – Page Object Model classes
- **Tests** – Test scenarios
- **Utils** – Helper classes, configuration, logging and JSON reader
- **Data** – Test data stored in JSON format
- **Conftest** – Browser fixtures and PyTest hooks

This design improves maintainability, readability and scalability.

---

## Test Features

### Manual Features

- Functional Testing
- Regression Testing
- Smoke Testing
- UI Validation

### Automation Features

- Page Object Model
- Data-driven testing
- Reusable fixtures
- Automatic browser management

---

## Failure Handling

When a test fails, the framework automatically:

- Captures a screenshot
- Records browser video
- Saves a Playwright trace
- Generates an HTML report

These artefacts make debugging much easier.

---

## Running the Project

### Clone the repository

```bash
git clone https://github.com/cromox1/Playwright_Python3_QA1.git
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Install Playwright browsers

```bash
playwright install
```

---

### Run all tests

```bash
pytest
```

---

### Generate HTML Report

```bash
pytest --html=report.html
```

---

## View Playwright Trace

```bash
playwright show-trace traces/<trace-file>.zip
```

The Trace Viewer allows you to replay the complete test execution, inspect each action, review network requests, console logs and DOM snapshots.

---

## Continuous Integration

This project uses **GitHub Actions** to automatically:

- Install dependencies
- Install Playwright browsers
- Execute all tests
- Verify that the framework runs successfully

Every push to the repository automatically triggers the workflow.

---

## Future Enhancements

Planned improvements include:

- API Testing
- Parallel execution
- Cross-browser execution
- Allure reporting
- Docker support
- Environment configuration
- Jenkins integration
- Azure DevOps pipeline
- Playwright fixtures optimisation
- Test tagging (Smoke, Regression, Sanity)

---

## About Me

I am a Senior QA Automation Engineer with over 15 years of experience in software quality assurance.

My expertise includes:

- Selenium
- Python
- Playwright
- REST API Testing
- Postman
- SQL
- PyTest
- Appium
- Git
- CI/CD
- Jira
- Agile

This repository demonstrates my approach to designing clean, maintainable, and scalable automation frameworks.

---

## License

This project is provided for learning and demonstration purposes.
