import os
import subprocess
import sys
from selenium import webdriver
from time import sleep

#github creds
github_Username = "Lucidreline"
github_Password = os.environ.get("GITHUB_PW") #Put your password here

projectsFolderPath = "C:/Users/ma52c/Storage/Coding/Projects/"

browser = webdriver.Chrome()


#Takes in argument from the terminal and setsit as the project name
projectName = str(sys.argv[1])

#makes sure that the project does not already exsist
filesInDir = os.listdir("C:/Users/ma52c/Storage/Coding/Projects/")
for file in filesInDir:
    if(file == projectName):
        print("ERROR: Project name already exsists. Pick a different name!")
        quit()

#changes to the projects dir
os.chdir(projectsFolderPath)

#creates folder
os.system("mkdir " + projectName)

#go into the new project folder
os.chdir(projectsFolderPath + projectName + "/")

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

    #basic commands to init the local repo and connect it to the remote one
    gitCommands = ["git init", "git add .", """git commit -m "first commit" """, "git remote add origin " + repoLink, "git push -u origin master"]
    
    for command in gitCommands:
        os.system(command)
    
        
    #make github repo private 
    browser.get("https://github.com/" + github_Username + "/" + projectName + "/settings")
    browser.find_elements_by_xpath("//*[@id='options_bucket']/div[8]/ul/li[1]/details/summary")[0].click()
    browser.find_elements_by_xpath("//*[@id='options_bucket']/div[8]/ul/li[1]/details/details-dialog/div[4]/form/p/input")[0].send_keys(projectName)
    browser.find_elements_by_xpath("//*[@id='options_bucket']/div[8]/ul/li[1]/details/details-dialog/div[4]/form/div/button")[0].click()

    #close browser
    browser.close()

gitSetup(projectName)

#opens project in VS Code
os.system("code .")