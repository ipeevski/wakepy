# Development

This document serves as documentation for the package developers.

## Branches and tags


- `main` branch: for development. All PRs should be against it. 
- `latest-release` branch: The latest wakepy release. This is used to select the where [wakepy.readthedocs.io](https://wakepy.readthedocs.io/) redirects to (the "latest" version). 
- Use a local short-lived feature branch for development.
- Release versions use [Semantic Versioning](https://semver.org/) and are marked with git tags (on the main branch) with format `v[major].[minor].[patch]`; e.g. v1.2.0 or v2.2.0.


## Installing for development

Install in editable state with the `doc` and `dev` options:
```
python -m pip install -e .[doc,dev]
```

where `.` means the current directory (assuming cwd is at root of the repository).

## Documentation

- The documentation is done with Sphinx and the source code lives at 
 `./docs/source`.
- **Building locally** (for debugging / testing docs), with autobuild:

```
sphinx-autobuild docs/source/ docs/build/ -a
```

The `-a` flag ensures that *all* files (not only edited files) will get rebuild. It is also possible to build just one time:
```
sphinx-build -b html docs/source/ docs/build
```
- **Deploying**: Just push to github, and it will be automatically built by readthedocs. The settings can be adjusted [here](https://readthedocs.org/dashboard).
- Versions selected for documentation are selected in the readthedocs UI. Select one version per `major.minor` version (latest of them) from the git tags. 
- The `latest` version (default versio) in readthedocs follows the `latest-release` branch automatically.
  



# Testing 

- wakepy uses pytest for tests and tox for testing the library with multiple python versions.

## Running tests with single environment

- Use pytest to run tests within a single environment:

```
python -m pytest
```

- To run tests with coverage, use

```
coverage run -m pytest <test-target> && coverage html && python -m webbrowser -t htmlcov/index.html 
```

## Running tests with multiple environments

- To run the tests with multiple python versions, use tox:

```
python -m tox 
```

- To start a debugger on error with a specific python version, select the tox environment with "-e <envname>" and add "-- --pdb" to start the python debugger on error. For example:

```
python -m tox -e py310 -- --pdb
```


# Deployment

- Create a wheel with

```
python -m pip wheel --no-deps .
```
- Push to PyPI  (assuming the one-time setup below done)
```
python -m twine  upload wakepy-<version>-py3-none-any.whl --repository wakepy
```
- If made a new version, remember to update the `latest-release` branch so ReadTheDocs may update the documentation. 
- Also, check that readthedocs has included all the correct versions (git tags)


## Setting up twine/pip for uploading to PyPI
- This should be done once per system
- (1) Get a PyPI token for the *project* from [pypi.org/manage/account/token/](https://pypi.org/manage/account/token/) 
- (2) Create a `$HOME/.pypirc` file with following contents:

```
[distutils]
  index-servers =
    pypi
    wakepy

[pypi]
  username = __token__
  password = # either a user-scoped token or a project-scoped token you want to set as the default

[wakepy]
  repository = https://upload.pypi.org/legacy/
  username = __token__
  password = # the wakepy project scoped token here.
```