# Development Setup

This guide serves as a guide to setting up the IDE to be compliant with the
[*static code analysis*](CONTRIBUTING.md/#static-code-analysis) section
of the contributing guide. It is a suggestion to follow the setup but does
not cover all the static code analysis tools mentioned.

### Table of Contents
- [Development Setup](#development-setup)
    - [Table of Contents](#table-of-contents)
    - [Python](#python)
    - [VS Code](#vs-code)

### Python

- [pyenv](https://github.com/pyenv/pyenv)

Pyenv can be used to switch between different versions of python easily,
depending on the version of Python charm uses. For example:
```bash
pyenv install 3.10.7
pyenv global 3.10.7
cd PATH/TO/REPOSITORY
python -m virtualenv venv
```

### VS Code

The extensions do not use project configurations by default. The setup below
helps setup tools to follow project configurations setup in `pyproject.toml`.

- [Black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)

1. Install VS Code Black formatter extension
2. Set black as the default formatter for Python (snippet in `settings.json` 
    for reference)
```json
"[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true,
},
```

- [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort)

1. Install VS Code isort extension
2. Use black as the isort profile by pasting the code below into 
    `settings.json`(Ctrl+Shift+p, Preferences: Open User Settings (JSON)) or 
    by adding isort args `--profile`, `black`(separate item) in the 
    settings UI (Ctrl+Shift+p, Preferences: Open Settings (UI))
```diff
"[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true,
+    "editor.codeActionsOnSave": {
+        "source.organizeImports": true
+    },
},
+ "isort.args":["--profile", "black"],
```

- [flake8](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8)

Default flake8 cannot be used to read the project settings.
Using pyproject-flake8 is required.

1. Install VS Code flake8 extension
2. pip install flake 8 and it's plugins
```bash
pip install flake8 flake8-docstrings \
    flake8-copyright flake8-builtins \
    pyproject-flake8 pep8-naming
```
1. Change the flake 8 to point to pflake8 installed above by modifying the
    *Flake8: Path* entry in Settings(UI) or
    by pasting the code below into `settings.json`
```json
"python.linting.flake8Path": "PATH/TO/pflake8",
"python.linting.flake8Enabled": true,
"flake8.path": [
    "PATH/TO/pflake8"
],
```

- Ignoring .vscode folder on enabling typecheck

By enabling VS Code type checking feature, it creates a `.vscode` directory with
project `settings.json`. You can ignore this globally by adding it to global
gitignore file.
```
// .gitconfig file
...
[core]
excludesFile = ~/.gitignore_global
...

// ~/.gitignore_global file
.vscode/
```

- Adding rulers for line-length

1. Open vscode `settings.json` and add the following snippet below or modify the
    Editor: Rulers entry in Settings UI.
```json
"editor.rulers": [
    80, 99
]
```