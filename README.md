# Phase 3 CLI+ORM Project

## Overview

This project is a CLI application that allows users to add and view locations using a SQLite database.

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install dependencies:

    ```bash
    pipenv install
    pipenv shell
    ```

## Usage

Run the CLI application:

```bash
python lib/cli.py

## Follow the prompts to add and view locations.

Project Structure
lib/cli.py: The main entry point for the CLI application.
lib/helpers.py: Contains helper functions for adding and viewing locations.
lib/models/location.py: Defines the Location model using SQLAlchemy.
lib/models/__init__.py: Sets up the database connection and session.
