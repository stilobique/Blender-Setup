@echo off

git pull
git submodule update --init --recursive
git submodule foreach git checkout master