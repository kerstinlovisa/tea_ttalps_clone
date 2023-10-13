#!/bin/bash

# save current gitignore & README
cp .gitignore .gitignore_user
cp .github/README.md .github/README_user.md

# temporarily use tea gitignore & README
cp .gitignore_tea .gitignore
cp .github/README_tea.md .github/README.md

# update tea
git stash
# git pull --merge -X theirs upstream main
git merge -X theirs upstream/main
git stash pop -q

# restore user's gitignore & README
cp .gitignore_user .gitignore
cp .github/README_user.md .github/README.md

# push tea update to user's repo
git push -f origin main
