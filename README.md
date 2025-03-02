# Generic_VENV_Manger
https://github.com/StevenNaliwajka/Generic_JSON_Manger  
Builds Json Files for users on setup.
------------------
# Setup.
### 1) Install Project as a Subtree with git.

To integrate this repo into your project.  
Navigate to the location of where you want it in CMD and input a variation of this:
```angular2html
git subtree add --prefix=PATH/TO/FOLDER/Generic_JSON_Manger https://github.com/StevenNaliwajka/Generic_JSON_Manger.git main --squash
```

### 2) In the future.
To update to the latest version of this repo.
```angular2html
git subtree pull --prefix=PATH/TO/FILE/Generic_JSON_Manger https://github.com/StevenNaliwajka/Generic_JSON_Manger.git main --squash
```
------------------

## Using the tools.
### Create .JSON:
Usage for creating JSON is:  
```angular2html
    # data to be passed should be in the form.
data = {
    "name": "Alice",
    "age": 28,
    "skills": ["Python", "Machine Learning", "Data Science"]
}
```
```angular2html
JSONUtil.create_json("~/PATH/TO/NEWFILE.JSON", data)
```

Ensure to add 'NEWFILE.JSON' to ".gitignore" file.
```angular2html
echo NEWFILE.JSON >> .gitignore
```
### Read .JSON:
temp
### Update .JSON:
temp
### Delete .JSON:
temp