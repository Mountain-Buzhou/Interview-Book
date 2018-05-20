#! /bin/zsh
cd dist
git init
git add -A
git commit -m 'deploy'
git push -f git@github.com:Liyuk/Interview-Book.git master:master