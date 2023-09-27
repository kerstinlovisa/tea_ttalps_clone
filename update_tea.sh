#!/bin/bash

# save current gitignore 
cp .gitignore .gitignore_user

# temporarily use tea gitignore
cp .gitignore_tea .gitignore

# update tea
git stash
git pull --rebase upstream main
git stash pop

# restore user's gitignore
cp .gitignore_user .gitignore
