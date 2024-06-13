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

## Running the CLI Application
To run the CLI application, use the following command:

```bash
python lib/cli.py
```

Follow the prompts in the CLI to add and view locations.

## Interacting with the Database
You can interact with the SQLite database directly using the SQLite command-line tool. Here are the basic commands:

Access the SQLite command-line interface:

```bash
sqlite3 locations.db
```
## Example commands:

View all locations:

```sql
SELECT * FROM locations;
```

This will display all entries in the locations table.

### Insert a new location:

```sql
INSERT INTO locations (name, latitude, longitude) VALUES ('Location Name', latitude_value, longitude_value);
```

Replace 'Location Name', latitude_value, and longitude_value with your actual data.

## Project Structure

lib/cli.py: Main entry point for the CLI application.
lib/helpers.py: Helper functions for adding and viewing locations.
lib/models/location.py: Defines the Location model using SQLAlchemy.
lib/models/init.py: Sets up the database connection and session.
