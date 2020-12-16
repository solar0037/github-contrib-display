Github-Contrib-Display
======================

.. contents::

A display for viewing your github contributions in the terminal.

Prerequisites
-------------

- Linux/Windows (no macOS support for the script yet)
- Python3, virtualenv (or use poetry instead)

Setup
-----

This generates a virtual environment and installs necessary packages.

Linux

.. code-block:: bash

    git clone https://github.com/solar0037/github-contrib-display.git
    cd github-contrib-display

    # poetry install  # if poetry is installed
    ./scripts/setup.sh  # instead use the script
    # pip install -r requirements.txt  # or even manual setup

Windows

.. code-block:: bat

    git clone https://github.com/solar0037/github-contrib-display.git
    cd github-contrib-display

    # poetry install  # if poetry is installed
    .\scripts\setup.bat  # instead use the batch file
    # pip install -r requirements.txt  # or even manual setup

Run
---

This runs the code.

Linux

.. code-block:: bash

    ./scripts/run.sh
    # python3 -m github_contrib_display  # manually run the code

Windows

.. code-block:: bat

    .\scripts\run.bat
    # python -m github_contrib_display  # manually run the code
