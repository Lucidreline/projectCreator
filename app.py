import os
import subprocess
import sys
import selenium
from selenium import webdriver
from time import sleep





#Takes in argument from the terminal and setsit as the project name
projectName = str(sys.argv[1])

#makes sure that the project does not already exsist
filesInDir = os.listdir("C:/Users/ma52c/Storage/Coding/Projects/")
for file in filesInDir:
    if(file == projectName):
        print("ERROR: Project name already exsists. Pick a different name!")
        quit()

github_Username = "Lucidreline"
github_Password = os.environ.get("GITHUB_PW")


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(r"C:\Users\ma52c\Storage\Coding\Projects\ProjectCreater\chromedriver.exe")

#changes to the projects dir
os.chdir("C:/Users/ma52c/Storage/Coding/Projects/")

#creates folder
os.system("mkdir " + projectName)

#go into the new project folder
os.chdir("C:/Users/ma52c/Storage/Coding/Projects/" + projectName + "/")

#creates the files
filesToCreate = ["app.py", "README.md", "CheckList.txt"]
for file in filesToCreate:
    os.system("type nul > " + file)







    
def gitSetup(_projectName):
    

    browser.get("https://github.com/login")

    #put in email
    browser.find_elements_by_xpath("//*[@id='login_field']")[0].send_keys(github_Username)

    #put in password
    browser.find_elements_by_xpath("//*[@id='password']")[0].send_keys(github_Password)

    #hit signin
    browser.find_elements_by_xpath("//*[@id='login']/form/div[3]/input[7]")[0].click()

    #go to new repo page
    browser.get("https://github.com/new")

    #put in new repo name
    browser.find_elements_by_xpath("//*[@id='repository_name']")[0].send_keys(projectName)
    sleep(2)

    #click 'create repo'
    browser.find_elements_by_xpath("//*[@id='new_repository']/div[3]/button")[0].click()

    #extract repo link
    repoLink = browser.find_elements_by_xpath("//*[@id='empty-setup-push-repo-echo']/span[1]/span")[0].text
    repoLink = str(repoLink)

    #close browser
    browser.close()

    #basic commands to init the local repo and connect it to the remote one
    gitCommands = ["git init", "git add .", """git commit -m "first commit" """, "git remote add origin " + repoLink, "git push -u origin master"]
    
    for command in gitCommands:
        os.system(command)
        

gitSetup(projectName)

#opens project in VS Code
os.system("code .")