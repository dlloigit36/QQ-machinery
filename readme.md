# Background:
This is web application developed in Python with Flask, SQLAlchemy as db model to create and 
store data into database. 

Current code use Python build-in database SQLite, with db file saved inside "instance" folder. Db file will be created when you run this program for the first time. With minimal code changes, database can be changed to use other database like PostgreSQL as an example.

Bootstrap5 used to render html content.

# Purpose:
This application can be used as inventory system to keep track of machinery parts installed
for specific client.

# Getting Started

Follow these steps to set up your local environment and run the application using PyCharm Community Edition.

## Prerequisites

*   [PyCharm Community Edition](https://jetbrains.com) installed.
*   Python installed on your system.

## Setup and Installation

### 1. Open the Project
Download or clone all files from Github repository. Launch PyCharm and select **File > Open**. Navigate to the root directory of this project and click **OK**.

### 2. Create a Virtual Environment
1.  Go to **File > Settings** (or **PyCharm > Settings** on macOS).
2.  Navigate to **Project: [Project Name] > Python Interpreter**.
3.  Click **Add Interpreter** > **Add Local Interpreter...**.
4.  Select **Virtualenv Environment** and ensure **New environment** is selected.
5.  Click **OK**. PyCharm will create a `.venv` folder in your project directory.

### 3. Install Dependencies
PyCharm should detect the `requirements.txt` file automatically.
*   **Option A:** Click **Install requirements** in the yellow notification bar at the top of the editor.
*   **Option B (if Option A does not work):** Open the **Terminal** tab at the bottom of PyCharm and run:
    ```bash
    pip install -r requirements.txt
    ```
    On MacOS type:
    ```
    pip3 install -r requirements.txt
    ```
    On Windows type:
    ```
    python -m pip install -r requirements.txt
    ```

## Running the Program
1.  Locate your entry point file (e.g., `main.py`) in the Project tool window.
2.  Right-click the file and select **Run 'filename'**.
3.  For future runs, you can simply click the green **Play (▶)** button in the top-right toolbar or press `Shift + F10`.
