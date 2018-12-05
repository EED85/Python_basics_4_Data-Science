# VS Studio Tips

## cool plugins

- git lens
- Anaconda Extension
- Markdown Preview


## Shortcuts
- Strg + # - mulitline Comment
- strg + c - quit infinite loop
- strg + shift +  P
- strg + k  s save all (Press ctrl + k, release and thren press s)

## Git workflow

### basic workflow - One Person / One PC


1. "" -> git commit all
2. -> git push

### Using several PCs

run git pull first, before appliying the basic worklfow

### several users

1. git checkout to new branch (name it develop_YourName)
2. apply basic workflow to branch
3. create Pull request on Githib
4. merge it via github pull requests plugin
5. delete develop branch on github
6. checkout master
7. git pull

## using pip command libs

open an Terminal (Python)
PS C:\DEV\git\Python_test> & python -m pip install -U autopep8