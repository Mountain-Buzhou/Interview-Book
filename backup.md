### tips

因为项目过于简单，所以没有使用gitbook。   
上传后如果需要gh-pages生效，请记得跑一遍python脚本生成html文件

### python
将markdown生成html脚本

```
pip install markdown

python md_conv.py README.md
```

### toc生成
```
wget https://raw.githubusercontent.com/ekalinin/github-markdown-toc/master/gh-md-toc

chmod a+x gh-md-toc

./gh-md-toc README.md
```