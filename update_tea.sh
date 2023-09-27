#!/bin/bash

cp .gitignore_tea .gitignore
git pull --rebase upstream main
cp .gitignore_user .gitignore
