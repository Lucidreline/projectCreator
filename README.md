# Project Creator
A Python automation app that gets you started with your project. For windows. Not sure how this will work on Mac.

## Installation
If you haven't already, Install python 3.

You will need to install selenium.

```bash
pip install -U selenium
```

And also install Chrome Driver: https://chromedriver.chromium.org/downloads
Then put chrome driver in a folder, copy the folder's path, and add that path as a value of the environmental system variable 'path'

## Usage
Create a file named config.py and add in your github username, password, your projects folder's path, and the files you want to be created in this project.

Here is an example. Keep the variable names the same. Add your own values.
```python
GITHUB_USERNAME      = "Lucidreline"
GITHUB_PASSWORD      = "MyTopSecretPassword123"
PROJECTS_FOLDER_PATH = "C:/Users/ma52c/Storage/Coding/Projects/"
FILES_TO_CREATE      = ["app.py", "README.md", "CheckList.txt", ".gitignore"]
```

To create a project, open your terminal and cd into this folder. Then, run the python script along with your project's name

```bash
cd C:/Users/ma52c/Storage/Coding/Projects/
python app.py myProject
```

