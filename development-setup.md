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
    - [Signed Commits](#signed-commits)

### Python

- [pyenv](https://github.com/pyenv/pyenv)

Pyenv can be used to switch between different versions of python easily,
depending on the version of Python charm uses. For example:
```bash
pyenv install 3.10.7
pyenv global 3.10.7
```
Install pyenv by following the 
[installation guide](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation). Python 
[build dependencies](https://github.com/pyenv/pyenv?tab=readme-ov-file#install-python-build-dependencies)
may need to be pre-installed before installing additional Python versions.

- [pipx](https://github.com/pypa/pipx)

Pipx is recommended to install Python applications (i.e. pflake8) in an isolated environment
without modifying your system dependencies.

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
Using pyproject-flake8 is required to read from pyproject.toml.

1. Install VS Code flake8 extension
2. pipx install flake 8 and it's plugins
```bash
pipx install pyproject-flake8
pipx inject flake8-docstrings flake8-copyright flake8-builtins pep8-naming
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

### Tox

Use pipx to install tox.

```bash
pipx install tox
```

### Signed Commits

* Make sure `gpg` is installed:

   * On Linux

     ```bash
     sudo apt-get install gnupg
     ```

   * On MacOS

     ```bash
     brew install gnupg pinentry-mac
     ```

* Generate a new key following the prompts and entering your Canonical email
  address. Please add a passphrase to the key when you generate it.

  ```bash
  gpg --gen-key
  ```

* List generated keys and note the `<long_key>`

  ```bash
  gpg --list-secret-keys --keyid-format LONG
  ```

  Output:

  ```bash
  /home/username/.gnupg/secring.gpg
  -------------------------------
  sec   4096R/<long_key> <date> [expires: <date>]
  uid                          <name> <<email>>
  ssb   4096R/<value> <date>
  ```

* Get the public key

  ```bash
  gpg --armor --export <long_key>
  ```

* Go to your GitHub settings and add the gpg public key:
  https://github.com/settings/keys

* Configure git to sign commits:

  ```bash
  git config --global user.signingkey <long_key>
  git config --global commit.gpgsign true
  ```

* On MacOS some extra steps are required:

  ```bash
  echo "pinentry-program /opt/homebrew/bin/pinentry-mac" >> ~/.gnupg/gpg-agent.conf
  killall gpg-agent
  ```

  You can test if it works properly using:

  ```bash
  echo "test" | gpg --clearsign
  ```

  A prompt should ask for your password and a PGP Signature should be printed in
  your shell.

#### Alternative signing using an SSH key

* We assume that you're using `git` (version >= 2.34) and already have an SSH
key to push to our repositories.

* Configure git to sign commits

```shell
# tell git to sign using SSH
git config --global gpg.format ssh
# tell git which SSH key to use
git config --global user.signingkey path/to/your/ssh/key
# tell git to sign all commits
git config --global commit.gpgsign true
```

* Add the SSH key to [GitHub](https://github.com/settings/keys) as a new SSH
  signing key. This is required even if you already have the same key configured
  as an authentication key.

* Voilà
