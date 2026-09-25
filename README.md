🧪 TestForge — Web & API Test Automation Framework

<p align="center">
  <b>Python-based SDET automation framework for UI, REST API, and database testing</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Selenium-WebDriver-43B02A?logo=selenium&logoColor=white" alt="Selenium">
  <img src="https://img.shields.io/badge/PyTest-Test%20Automation-0A9EDC" alt="PyTest">
  <img src="https://img.shields.io/badge/Requests-REST%20API-2E8B57" alt="Requests">
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?logo=githubactions&logoColor=white" alt="GitHub Actions">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Tests-27%20Passing-success" alt="27 tests passing">
  <img src="https://img.shields.io/badge/UI-7%20tests-blue" alt="7 UI tests">
  <img src="https://img.shields.io/badge/API-12%20tests-blue" alt="12 API tests">
  <img src="https://img.shields.io/badge/DB-8%20tests-blue" alt="8 DB tests">
</p>

📌 Overview

TestForge is an SDET-focused test automation framework built with Python and PyTest. It tests a small Flask-based e-commerce application at three levels:

🖥️ UI testing with Selenium WebDriver

🔌 REST API testing with Requests

🗄️ Database testing with SQLite and SQL

The framework follows the Page Object Model (POM) and uses reusable fixtures, parameterized test data, explicit waits, automatic failure screenshots, HTML reporting, and GitHub Actions for CI execution.

The goal of the project is to demonstrate how an SDET can build a maintainable automation framework rather than only writing individual test scripts.

🎯 Project Objectives

Automate critical web application scenarios

Validate REST API behavior and response data

Verify database records using SQL

Demonstrate reusable test architecture

Implement positive, negative, and data-driven testing

Capture screenshots automatically when UI tests fail

Generate test execution reports

Run the test suite through CI/CD

🧰 Tech Stack

Technology

Purpose

Python

Automation framework language

PyTest

Test execution, fixtures, parameterization

Selenium WebDriver

Browser/UI automation

Requests

REST API automation

Flask

Demo application / System Under Test

SQLite

Database validation

SQL

Database queries and assertions

Page Object Model

Maintainable UI automation architecture

Git & GitHub

Version control and source management

GitHub Actions

Continuous Integration

PyTest HTML

Test reporting

🏗️ Architecture

                         ┌──────────────────────┐
                         │   TestForge Runner   │
                         │       PyTest         │
                         └──────────┬───────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 │                  │                  │
                 ▼                  ▼                  ▼
        ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
        │   UI Tests     │ │   API Tests    │ │   DB Tests     │
        │   Selenium     │ │   Requests     │ │   SQL/SQLite   │
        └───────┬────────┘ └───────┬────────┘ └───────┬────────┘
                │                  │                  │
                ▼                  ▼                  ▼
        ┌─────────────────────────────────────────────────────┐
        │              Flask Demo Application                 │
        │                  System Under Test                   │
        └─────────────────────────────────────────────────────┘
                                    │
                                    ▼
                              ┌───────────┐
                              │  SQLite   │
                              │ Database  │
                              └───────────┘

📂 Project Structure

testforge-sdet/
│
├── app/
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── pages/
│   ├── __init__.py
│   └── login_page.py
│
├── tests/
│   ├── api/
│   │   ├── __init__.py
│   │   └── test_api.py
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   └── test_database.py
│   │
│   └── ui/
│       ├── __init__.py
│       └── test_login_ui.py
│
├── utils/
│   ├── __init__.py
│   ├── api_client.py
│   └── db_utils.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── requirements-dev.txt
├── .gitignore
├── README.md
└── .github/
    └── workflows/
        └── tests.yml

🧪 Test Coverage

The current framework contains 27 automated tests.

Layer

Tests

Coverage

🖥️ UI

7

Login positive/negative and validation scenarios

🔌 API

12

Health, login, negative login, products, data types, response time

🗄️ Database

8

User and product data integrity

Total

27

27/27 passing

UI Testing — 7 Tests

The UI suite uses Selenium WebDriver and the Page Object Model.

Covered scenarios include:

Valid login

Wrong password

Wrong email

Wrong email and password

Empty email

Empty password

Empty credentials

The UI suite uses:

Explicit waits

Reusable page methods

Parameterized test data

Headless Chrome execution

Automatic screenshots on failed UI tests

API Testing — 12 Tests

The API suite validates:

Health endpoint

Successful login

Invalid password

Invalid email

Invalid email + password

Empty email

Empty password

Empty request body

Product endpoint

Required response fields

Response data types

Response-time threshold

Database Testing — 8 Tests

The database suite validates:

Test user existence

User email format

User password field presence

Product existence

Product count

Unique product IDs

Non-empty product names

Positive product prices

Note: The demo application is intentionally simple and uses SQLite. In a production application, passwords should be securely hashed rather than stored as plaintext.

🧱 Framework Design

Page Object Model

UI locators and browser interactions are separated from test logic.

tests/ui/test_login_ui.py
            │
            ▼
pages/login_page.py
            │
            ▼
      Selenium WebDriver

This makes the UI tests easier to maintain when the application's HTML structure changes.

Reusable Fixtures

conftest.py provides reusable fixtures for:

Selenium WebDriver

Base application URL

API client

Database path

Data-Driven Testing

PyTest parameterization is used to execute multiple login scenarios without duplicating test code.

Example:

@pytest.mark.parametrize(
    "email, password, expected_message",
    [...]
)
def test_login_scenarios(...):
    ...

Automatic Failure Screenshots

When a Selenium UI test fails, the framework automatically captures a screenshot and stores it under:

reports/screenshots/

The reports/ directory is ignored by Git because generated test artifacts should not be committed to source control.

▶️ Getting Started

Prerequisites

Python 3.11+

Google Chrome

Git

Selenium Manager handles the browser driver setup in the normal local execution flow.

1. Clone the repository

git clone https://github.com/raimaagg05/testforge-sdet.git
cd testforge-sdet

2. Create a virtual environment

Windows

python -m venv venv
venv\Scripts\activate

macOS/Linux

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Start the demo application

python app/app.py

The application runs locally at:

http://127.0.0.1:5000

Keep the application terminal running.

5. Run the complete test suite

Open another terminal:

pytest -v

Expected result:

27 passed

🧪 Running Specific Test Layers

UI Tests

pytest -v tests/ui

API Tests

pytest -v tests/api

Database Tests

pytest -v tests/db

Run by PyTest marker

pytest -v -m ui
pytest -v -m api
pytest -v -m db

📊 HTML Test Report

Generate a self-contained HTML report:

pytest --html=reports/report.html --self-contained-html

The generated report is stored locally under:

reports/report.html

🔐 Demo Test Credentials

The Flask demo application contains a test account:

Email:    test@example.com
Password: Test@123

These credentials are for the local demo application only.

⚙️ Configuration

The application and test framework support environment-based configuration.

Example:

BASE_URL=http://127.0.0.1:5000
DB_PATH=testforge.db

This allows the same test framework to be pointed at a different test environment without changing the test logic.

🔄 CI/CD

GitHub Actions is configured to run the automated test suite in CI.

Developer Push / Pull Request
            │
            ▼
     GitHub Actions
            │
            ▼
    Setup Python Environment
            │
            ▼
     Install Dependencies
            │
            ▼
     Start Demo Application
            │
            ▼
       Run PyTest
            │
            ▼
     Test Result / Report

This demonstrates a basic Continuous Integration workflow for an SDET automation framework.

🧠 SDET Skills Demonstrated

This project demonstrates practical understanding of:

Test automation architecture

UI automation

REST API testing

Database testing

Selenium WebDriver

PyTest fixtures

PyTest parameterization

Positive and negative testing

Page Object Model

Explicit waits

Reusable utilities

Test isolation

Assertions

Failure diagnostics

Screenshot capture

HTML reporting

Environment configuration

Git/GitHub

CI/CD

Automated regression testing

🚀 Future Enhancements

Possible next improvements:

Add API schema validation

Add authentication/token management

Add more UI page objects

Add cross-browser execution

Add parallel test execution

Add Selenium Grid

Add Allure reporting

Add Docker support

Add environment-specific test configuration

Add Jenkins pipeline

Add security-focused API tests

Add broader end-to-end shopping workflows

📌 Why TestForge?

TestForge was built to demonstrate an end-to-end SDET mindset:

Don't just test the UI — validate the application across UI, API, and database layers and automate the complete regression workflow.

The framework combines reusable automation design, multiple testing layers, failure diagnostics, reporting, version control, and CI execution in one project.

👩‍💻 Author

Raima Aggarwal

B.Tech — Electronics & Communication Engineering

GitHub:
https://github.com/raimaagg05

Project Repository:
https://github.com/raimaagg05/testforge-sdet

📄 License

This project is intended for educational, portfolio, and SDET practice purposes.
