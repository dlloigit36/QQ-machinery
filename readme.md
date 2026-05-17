# Background:
This is web application developed in Python with Flask, SQLAlchemy as db model to create and 
store data into database. 

Current code use Python build-in database SQLite, with db file saved inside "instance" folder. Db file will be created when you run this program for the first time. With minimal code changes, database can be changed to use other database like PostgreSQL as an example.

Bootstrap5 used to render html content.

# Purpose:
This application can be used as inventory system to keep track of machinery parts installed
for specific client.

# Python Project Setup Guide- Visual Studio Code as IDE

Follow these steps to configure Visual Studio Code, set up a virtual environment, and run the Python project.
Clone Python code from GitHub repository.
```
 git clone https://github.com/dlloigit36/QQ-machinery.git
```

## 1. Install the Python Extension
1. Open **Visual Studio Code**.
2. Click the **Extensions** icon on the left Activity Bar (`Ctrl+Shift+X` or `Cmd+Shift+X`).
3. Search for **Python**.
4. Find the extension published by **Microsoft** and click **Install**.

## 2. Set Up a Python Virtual Environment
1. Open your project folder in VS Code (`File` > `Open Folder...`).
2. Open the built-in terminal (`Terminal` > `New Terminal`).
3. Run the creation command based on your operating system:

* **Windows:**
  ```bash
  python -m venv .venv
  ```
  Sometimes Python is installed under a different command name. Try running these in your VS Code terminal.
  ```
  py -m venv .venv
  ```
  or
  ```
  python3 -m venv .venv
  ```
* **macOS/Linux:**
  ```bash
  python3 -m venv .venv
  ```

## 3. Select the Python Interpreter
1. Open the Command Palette using `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS).
2. Type **Python: Select Interpreter** and select it.
3. Choose the interpreter located inside your new virtual environment (labeled with `(.venv)`).
4. Close your current terminal and open a **New Terminal** to automatically activate the environment. You will see `(.venv)` at the start of your terminal line.

## 4. Install Dependencies
1. Ensure your terminal shows the active `(.venv)` environment.
2. Run the installation command to load the required packages:
* **macOS/Linux:**
   ```bash
   pip install -r requirements.txt
   ```
* **Windows:**
  ```bash
  python -m pip install -r requirements.txt
  ```   


## 5. Run the Program
1. Open your main Python file (e.g., `main.py`).
2. Click the **Play button** > **drop down** > **Run as Task** (Run Python File) in the top-right corner of the editor window.
3. Alternatively, run it directly from the active terminal:
   ```bash
   python main.py
   ```


# Getting Started with PyCharm as IDE

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

## Modify Flask secret key
*   **Option A:** Change secret key directly on below line in "main.py"
    ```
    app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY', "enter your own key with no space")
    ```
*   **Option B:** Create a .env file on root directory, with content below:
    ```
    FLASK_KEY='enter_your_own_key_8BYkEfBA6O6donzWlSihBXox7C0sKR6b77'
    ```
