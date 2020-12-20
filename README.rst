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

Clone this repository and follow the instructions.
This generates a virtual environment and installs necessary packages.

Note: virtualenv will be installed if you use the setup script.

Linux

.. code-block:: bash

    ./scripts/setup.sh  # default: use the script
    # poetry install  # if poetry is installed
    # pip install -r requirements.txt  # or even manual setup

Windows

.. code-block:: PowerShell

    .\scripts\setup.ps1  # default: use the powershell script
    # .\scripts\setup.bat  # batchfile is deprecated, use powershell instead
    # poetry install  # if poetry is installed
    # pip install -r requirements.txt  # or even manual setup

Run
---

This runs the code.

Linux

.. code-block:: bash

    ./scripts/run.sh
    # python3 -m github_contrib_display  # manually run the code

Windows

.. code-block:: PowerShell

    .\scripts\run.ps1
    # .\scripts\run.bat  # batchfile is deprecated, use powershell instead
    # python -m github_contrib_display  # manually run the code
