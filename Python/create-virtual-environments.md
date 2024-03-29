# Create virtual environments

Virtual environments are used for isolating development and working with a fresh, dedicated instance of Python. Virtual environments allow used packages to be frozen in place, controlling versions so that another user can install required packages in order to run the programme.

```bash
// when using POSIX systems like Linux/Ubuntu/Debian
// create an environment
python3 -m venv <path/to/env>

// activate an environment
source <venvname>/bin/activate
```

```bash
// when using a Windows system
// create an environment
C:\> python -m venv <path/to/venv>

// activate an environment
C:\> <venv>\Scripts\activate.bat
```

## Freezing `pip requirements`

When deploying a `python` script, including the required packages and their versions can be done by freezing them in place. Another user can then create a virtual environment on their machine and install then `pip install`.

```bash
pip freeze > requirements.txt
```