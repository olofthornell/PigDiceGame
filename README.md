Pig dice game project
==========================

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Info about the development of Pig dice game.

### Rules of the game

A game were you play against a computer player. First player to reach 100 point are the winner. If you hit 1 your score of the turn is set to zero and the turn ends. If you want to save your turn score to a total - enter "hold" in the terminal.

### Main menu commands

You play the game from the GitBash terminal using commands. https://gitforwindows.org/

In the main menu you use the following commands.

```
# Start the gameplay
start

# Read the game rules
rules

# Look at the high score list
high_score

# Empty the high score list
clear_high_score

# Exit the program
exit

```

### In game commands

When you start the game you get another set of commands.

```
# Roll the dice
roll

# Save your turn score to a total
hold

# Get six points to your turn score
cheat

# Set personality of cpu to coward
difficulty coward

# Set personality of cpu to moderate
difficulty moderate

# Set personality of cpu to bold
difficulty bold

# Exit the gameplay
exit

```

[[_TOC_]]



Instructions
--------------------------

Important things about the project


### Check version of Python

Check what version of Python you have. The Makefile uses `PYTHON=python` as default.

```
# Check you Python installation
make version
```

If you have another naming of the Python executable then you can solve that using an environment variable. This is common on Mac and Linux.

```
# Set the environment variable to be your python executable
export PYTHON=python3
make version
```

Read more on [GNU make](https://www.gnu.org/software/make/manual/make.html).



### Python virtual environment

Install a Python virtual environment and activate it.

```
# Create the virtual environment
make venv

# Activate on Windows
. .venv/Scripts/activate

# Activate on Linx/Mac
. .venv/bin/activate
```

When you are done you can leave the venv using the command `deactivate`.

Read more on [Python venv](https://docs.python.org/3/library/venv.html).



### Install the dependencies

Install the PIP packages that are dependencies to the project and/or the development environment. The dependencies are documented in the `requirements.txt`.

Do not forget to check that you have an active venv.

```
# Do install them
make install

# Check what is installed
make installed
```

Read more on [Python PIP](https://pypi.org/project/pip/).



### Run the code

To run the program write the following. It is important to Use the GitBash terminal.

```
# Execute the main program
python pig/main.py

If the game cant find the modules do the following.

# Go to the root of the project
# In gitbash write like this:
export PYTHONPATH=.

 then run the program again

```

All code is stored in the directory `pig/`.


### Run the validators

You can run the static code validators like this. They check the sourcecode and exclude the testcode.

```
# Run each at a time
make flake8
make pylint

# Run all on the same time
make lint

```

### Run the unittests

You can run the unittests like this. The testfiles are also stored in the `pig/` directory.

```
# Run unttests without coverage
make unittest

# Run unittests with coverage
make coverage

# Run the linters and the unittests with coverage
make test
```

You can open a web browser to inspect the code coverage as a generated HTML report.

```
<browser> htmlcov/index.html
```

Read more on:

* [unittest](https://docs.python.org/3/library/unittest.html)
* [coverage](https://coverage.readthedocs.io/)



### Run parts of the testsuite

You can also run parts of the testsuite, for examples files or methods in files.

You can run all tests from a testfile.

```
# Run a testfile
python -m unittest test.test_game
```

You can also run a single testcase from a file.

```
# Run a test method, in a class, in a testfile
python -m unittest test.test_game.TestGameClass.test_init_default_object
```



### Remove generated files

You can remove all generated files by this.

```
# Remove files generated for tests or caching
make clean

# Do also remove all you have installed
make clean-all
```

### Generate UML and documentation

You can automaticly generate UML diagrams and documentation from the code.

```
# Generate diagrams with pyreverse
make pyreverse

# Generate documentation
make pdoc

```


Optional targets
--------------------------

These targets might be helpful when running your project.



### Codestyle with black

You can unify the codestyle using black. Running black will change your source code to have a codestyle according to black codestyle.

```
# Same same, different names
make black
make codestyle
```

Read more on [black](https://pypi.org/project/black/).

