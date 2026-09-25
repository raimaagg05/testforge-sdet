# TestForge — Web & API Test Automation Framework

TestForge is a self-contained SDET portfolio project that demonstrates end-to-end software testing skills across UI automation, REST API testing, database validation, reusable test architecture, reporting, and CI execution.

## Tech Stack

- Python 3.11+
- Selenium WebDriver
- PyTest
- Requests
- Flask (small demo application under test)
- SQLite
- Page Object Model (POM)
- GitHub Actions
- PyTest HTML report

## Project Architecture

```text
TestForge
├── app/
│   ├── app.py
│   └── templates/
│       └── index.html
├── config/
│   └── settings.py
├── pages/
│   └── login_page.py
├── tests/
│   ├── api/
│   │   └── test_api.py
│   ├── db/
│   │   └── test_database.py
│   └── ui/
│       └── test_login_ui.py
├── utils/
│   ├── api_client.py
│   └── db_utils.py
├── conftest.py
├── requirements.txt
├── pytest.ini
└── .github/
    └── workflows/
        └── tests.yml
```

## Features

### UI Automation
- Valid login
- Invalid login
- Required-field validation
- Page Object Model
- Explicit waits

### API Automation
- Health check
- Login API
- Product API
- Negative login scenario
- Response/status-code assertions

### Database Validation
- User record validation after successful API login
- Product data validation

### Reporting
Run:

```bash
pytest --html=reports/report.html --self-contained-html
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/testforge-sdet.git
cd testforge-sdet
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
python app/app.py
```

The application will run at:

```text
http://127.0.0.1:5000
```

Keep this terminal running.

### 5. Run tests

In another terminal:

```bash
pytest
```

Run only UI tests:

```bash
pytest tests/ui
```

Run only API tests:

```bash
pytest tests/api
```

Run database tests:

```bash
pytest tests/db
```

Generate an HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

## Test Credentials

```text
Email: test@example.com
Password: Test@123
```

## Test Cases

| ID | Type | Scenario | Expected Result |
|---|---|---|---|
| TC-UI-01 | UI | Login with valid credentials | User sees welcome message |
| TC-UI-02 | UI | Login with invalid password | Error message is displayed |
| TC-UI-03 | UI | Submit empty login form | Validation message is displayed |
| TC-API-01 | API | GET health endpoint | HTTP 200 and status=ok |
| TC-API-02 | API | Login with valid credentials | HTTP 200 and token returned |
| TC-API-03 | API | Login with invalid credentials | HTTP 401 |
| TC-API-04 | API | Get products | HTTP 200 and product list returned |
| TC-DB-01 | DB | Validate test user exists | Correct user is present |
| TC-DB-02 | DB | Validate product records | Product data is present |

## SDET Concepts Demonstrated

- Test automation
- Page Object Model
- Fixtures
- Explicit waits
- API assertions
- Negative testing
- Database validation
- Test isolation
- Reusable utilities
- HTML reporting
- CI/CD with GitHub Actions

## CI/CD

GitHub Actions runs the automated test suite on every push and pull request.

Workflow:

```text
Git Push / Pull Request
        ↓
Install Python
        ↓
Install dependencies
        ↓
Start Flask application
        ↓
Run PyTest
        ↓
Generate HTML report
```

## Future Enhancements

- Add API schema validation
- Add parameterized test data
- Add Selenium Grid / parallel execution
- Add Allure reporting
- Add Docker
- Add environment-specific configuration
- Add Jenkins pipeline
