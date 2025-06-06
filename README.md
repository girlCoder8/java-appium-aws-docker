# Java Appium AWS Docker Automation Framework

This project provides a comprehensive, containerized automation framework for web, mobile, API, and AI-driven test prioritization. It leverages Java + Appium for mobile testing, Playwright for web testing, Postman/Newman for API testing, and Python for AI-based test prioritization, all orchestrated via Docker Compose.

---

## Features

- **Mobile Automation:** Java, Appium, Selenium, and TestNG for iOS mobile app testing.
- **Web Automation:** Playwright (TypeScript) for cross-browser web UI testing.
- **API Automation:** Postman collections executed with Newman.
- **AI Test Prioritization:** Python-based ML model to prioritize test execution.
- **Dockerized:** Each component runs in its own container for consistency and scalability.
- **CI Integration:** Ready for GitHub Actions CI/CD.

---

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Java JDK 11+](https://adoptopenjdk.net/)
- [Maven](https://maven.apache.)
- [Xcode](https://developer.apple.com>xcode)
- [Node.js](https://nodejs.org/) (for local Playwright runs)
- AWS account and credentials (if using AWS features)

---

## Project Structure

```
.
├── ai/                # AI test prioritization (Python)
│   ├── Dockerfile
│   ├── model.pkl
│   └── prioritizer.py
├── api/               # API automation (Postman/Newman)
│   ├── Dockerfile
│   └── collections/
│       └── sample.postman_collection.json
├── mobile/            # Mobile automation (Java, Appium, TestNG)
│   ├── Dockerfile
│   ├── pom.xml
│   ├── testng.xml
│   ├── config.properties
│   ├── .gitignore
│   ├── README.md
│   ├── drivers/
│   ├── logs/
│   ├── reports/
│   ├── hooks/
│   ├── listeners/
│   ├── src/
│   │   ├── main/java/
│   │   │   └── com/example/framework/   # Core framework code, page objects, utilities
│   │   └── test/java/com/example/tests/ # Test classes
│   └── src/test/resources/              # Test data, screenshots, etc.
├── web/               # Web automation (Playwright)
│   ├── Dockerfile
│   ├── package.json
│   ├── playwright.config.ts
│   └── tests/
│       └── login.spec.ts
├── metadata.csv       # Test metadata for AI prioritization
├── docker-compose.yml # Orchestration for all services
├── .env               # Environment variables (not committed)
├── .gitignore         # Git ignore rules
├── README.md
└── LICENSE.txt
```

---

## Recommended Files and Folders for Mobile Automation

- **`.gitignore`**: Exclude build artifacts, IDE files, logs, and sensitive data.
- **`README.md`**: Documentation for setup, usage, and troubleshooting.
- **`testng.xml`**: TestNG suite configuration for organizing and running tests.
- **`config.properties`**: Environment-specific settings (URLs, device names, credentials, etc.).
- **`drivers/`**: Store Appium/Selenium driver binaries if needed.
- **`src/main/java/`**: Reusable utilities, core framework code, and page objects.
- **`src/test/java/`**: Test classes.
- **`src/test/resources/`**: Test data files (CSV, JSON, Excel), screenshots, and logs.
- **`logs/`**: Store execution logs (can be gitignored).
- **`pom.xml`**: Maven configuration.
- **`Dockerfile`**: Containerize the mobile test runner.
- **`hooks/` or `listeners/`**: Custom TestNG listeners or hooks (e.g., for reporting, screenshots on failure).
- **`reports/`**: Generated test reports (can be gitignored).

---

## Getting Started

### 1. Clone the repository

```sh
git clone https://github.com/girlCoder8/java-appium-aws-docker.git
cd java-appium-aws-docker
```

### 2. Set up environment variables

Create a `.env` file in the project root for sensitive credentials (e.g., AWS keys).  
**Do not commit this file to version control.**

Example `.env`:
```
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
DEVICE_NAME=iPhone_13
```

Reference this file in your `docker-compose.yml`:
```yaml
env_file:
  - .env
```

### 3. Build and Run All Services

```sh
docker-compose up --build
```

This will build and start the following containers:
- **mobile:** Runs Java Appium tests.
- **web:** Runs Playwright web tests.
- **api:** Runs API tests using Newman.
- **ai:** Runs AI-based test prioritization.

---

## Component Details

### Mobile Automation (`mobile/`)

- **Tech:** Java, Appium, Selenium, TestNG, Maven
- **Entry Point:** `src/test/java/com/example/tests/`
- **Build & Run:**
  ```sh
  cd mobile
  mvn clean test
  ```
  Or via Docker Compose as above.

### Web Automation (`web/`)

- **Tech:** Playwright, TypeScript, Node.js
- **Entry Point:** `tests/login.spec.ts`
- **Build & Run:**
  ```sh
  cd web
  npm install
  npx playwright test
  ```
  Or via Docker Compose as above.

### API Automation (`api/`)

- **Tech:** Postman, Newman
- **Entry Point:** `collections/sample.postman_collection.json`
- **Run:**
  ```sh
  cd api
  docker run --rm -v $(pwd)/collections:/etc/newman postman/newman run /etc/newman/sample.postman_collection.json
  ```
  Or via Docker Compose as above.

### AI Test Prioritization (`ai/`)

- **Tech:** Python, pandas, joblib
- **Entry Point:** `prioritizer.py`
- **Run:**
  ```sh
  cd ai
  pip install pandas joblib
  python prioritizer.py ../metadata.csv
  ```
  Or via Docker Compose as above.

---

## Continuous Integration

- **GitHub Actions:** See [`.github/workflows/ci.yml`](.github/workflows/ci.yml) for CI configuration.
- **CI Command:** Runs `docker-compose up --abort-on-container-exit` on each push.

---

## Customization

- **Add/modify tests** in their respective folders.
- **Update dependencies** in `pom.xml`, `package.json`, or `requirements.txt` as needed.
- **Adjust Dockerfiles** for custom environments.
- **Edit `metadata.csv`** to provide up-to-date test metadata for AI prioritization.

---

## Troubleshooting

- Ensure Docker daemon is running.
- Check container logs for errors.
- Verify AWS credentials if using AWS features.
- For Playwright, ensure browsers are installed (`npx playwright install`).

---

## License

MIT License. See [LICENSE.txt](LICENSE.txt)