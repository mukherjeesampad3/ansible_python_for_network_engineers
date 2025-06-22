## `DAY-1` 

## 1. Using `virtualenv` (Works on Python 2 & 3)

If you need finer control or are working with Python 2, use `virtualenv`.

### Install `virtualenv`

```bash
pip install virtualenv
```

### Create a Virtual Environment

```bash
virtualenv myenv
```

### Use a Specific Python Version

```bash
virtualenv -p /usr/bin/python3.8 myenv
```

### Activate / Install / Deactivate

Use the same activation commands as for `venv`, just replace `.venv` with `myenv`.

- **Linux/macOS**:

  ```bash
  source myenv/bin/activate
  ```

- **Windows (cmd)**:

  ```cmd
  myenv\Scripts\activate.bat
  ```

- **Windows (PowerShell)**:

  ```powershell
  .\myenv\Scripts\Activate.ps1
  ```

To deactivate:

```bash
deactivate
```

---

## 3. Tips & Best Practices

### Add venv to `.gitignore`

Prevent committing your virtual environment:

```gitignore
.venv/
myenv/
```

### Requirements File

Save all installed packages:

```bash
pip freeze > requirements.txt
```

Reinstall them later:

```bash
pip install -r requirements.txt
```

### 🐍 Multiple Python Versions

If you have multiple Python versions (e.g., 3.8, 3.9), you can create version-specific environments:

```bash
python3.9 -m venv .venv39
```

You now have a self-contained environment for each project.

---

## What is `requirements.txt` in Python?

`requirements.txt` is a text file used to list all the Python packages your project depends on. It ensures others (or future you) can install **exactly the same versions** of all required packages.

### Why It's Important

- Makes your project **reproducible**
- Helps with **deployment**, **testing**, and **CI/CD**
- Common with **virtual environments**

### Example `requirements.txt`

```txt
flask==2.3.3
requests>=2.31.0
numpy
pandas<2.0
```

- `flask==2.3.3` → Install exactly version 2.3.3
- `requests>=2.31.0` → Any version ≥ 2.31.0
- `numpy` → Latest available version
- `pandas<2.0` → Any version < 2.0

### How to Use It

**Create it** from your current environment:

```bash
pip freeze > requirements.txt
```

**Install everything** from it:

```bash
pip install -r requirements.txt
```
##  Using `python-dotenv`

Use `.env` files to manage environment variables securely and conveniently.

### Install `python-dotenv`

```bash
pip install python-dotenv
```

### Create a `.env` File

Place this file at the root of your project:

```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://user:pass@localhost:5432/mydb
```

### Load Variables in Python

```python
from dotenv import load_dotenv
import os

load_dotenv()  # loads variables from .env

debug = os.getenv("DEBUG")
secret_key = os.getenv("SECRET_KEY")
database_url = os.getenv("DATABASE_URL")
```

### Add `.env` to `.gitignore`

Never commit secrets to version control:

```gitignore
.env
```

### Best Practices

- Use `.env.example` to share required environment variables:

  ```env
  DEBUG=
  SECRET_KEY=
  DATABASE_URL=
  ```

- Keep `.env` for development secrets only.
- Use environment variables for production securely (e.g., Docker, CI/CD tools).

---

## How to Use Environment Variables in Python

Environment variables allow you to configure your applications without hardcoding sensitive or environment-specific data.

### Setting Environment Variables

#### Temporary (CLI-only)

```bash
export SECRET_KEY="your-secret-key"
```

#### Permanently (Linux/macOS)
Add to `~/.bashrc`, `~/.zshrc`, or `~/.bash_profile`:

```bash
export DEBUG=True
export DATABASE_URL=postgres://user:pass@localhost:5432/mydb
```

Then source the file:

```bash
source ~/.bashrc
```

#### Permanently (Windows)
Use PowerShell:

```powershell
[System.Environment]::SetEnvironmentVariable("DEBUG", "True", "User")
```

Or through the system GUI: System Properties → Environment Variables.

### Access in Python

```python
import os

secret_key = os.getenv("SECRET_KEY")
debug = os.environ.get("DEBUG")
```

### Good Practices

- Never hardcode secrets into your code.
- Prefer `.env` for local development.
- Use deployment systems (like Docker, Heroku, or GitHub Actions) to set environment variables securely.


