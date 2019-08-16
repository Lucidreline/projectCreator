import config
import os
import sys
from selenium import webdriver
from time import sleep


#Takes in argument from the terminal and setsit as the project name
projectName = str(sys.argv[1])

#makes sure that the project does not already exsist
filesInDir = os.listdir("C:/Users/ma52c/Storage/Coding/Projects/")
for file in filesInDir:
    if(file == projectName):
        print("ERROR: Project name already exists. Pick a different name!")
        quit()

#Opens up a chrome browser
browser = webdriver.Chrome()

#changes to the projects dir
os.chdir(config.PROJECTS_FOLDER_PATH)

#creates folder
os.system("mkdir " + projectName)

#go into the new project folder
os.chdir(config.PROJECTS_FOLDER_PATH + projectName + "/")

#creates the files
filesToCreate = config.FILES_TO_CREATE
for file in filesToCreate:
    os.system("type nul > " + file)


def gitSetup(_projectName):
    
    browser.get("https://github.com/login")

    #put in email
    browser.find_elements_by_xpath("//*[@id='login_field']")[0].send_keys(config.GITHUB_USERNAME)

    #put in password
    browser.find_elements_by_xpath("//*[@id='password']")[0].send_keys(config.GITHUB_PASSWORD)

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

    #basic commands to init the local repo and connect it to the remote one
    gitCommands = ["git init", "git add .", """git commit -m "Initial commit." """, "git remote add origin " + repoLink, "git push -u origin master"]
    
    for command in gitCommands:
        os.system(command)
    
    #close browser
    browser.close()

gitSetup(projectName)

#opens project in VS Code
os.system("code .")