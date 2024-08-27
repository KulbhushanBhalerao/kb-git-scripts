# kb-git-scripts
Some util scripts to make life easy while working with git

## fetch-pull-multiple-git-repos.py
```
Fetches and pulls changes for all the git repos in a parent folder. 

Solves problem: Solves problem of keeping all the git branches up to date when you are using some git branches from various open source projects or utils or have your own. 
Assumption: You have all your git repos in a parent folder, e.g. ~/git or C:/git 
Known issue: It fetches and pulls only for the current branches.
```
Running
```bash
python3 fetch-pull-multiple-git-repos.py
```
