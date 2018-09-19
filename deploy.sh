#! /bin/zsh
cd dist
git init
git add -A
git commit -m 'deploy'
git push -f git@github.com:Mountain-Buzhou/Interview-Book.git master:gh-pages