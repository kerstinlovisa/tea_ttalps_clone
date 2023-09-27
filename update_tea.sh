#!/bin/bash

# save current gitignore 
cp .gitignore .gitignore_user

# temporarily use tea gitignore
cp .gitignore_tea .gitignore

# update tea
git pull --rebase upstream main

# restore user's gitignore
cp .gitignore_user .gitignore

# push tea update to user's repo
git push -f origin main
