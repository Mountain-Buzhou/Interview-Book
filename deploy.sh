#! /bin/bash
vuepress build docs
cd docs/.vuepress/dist
git init
git add -A
git commit -m 'deploy'
git push -f git@github.com:Liyuk/Interview-Book.git master:master