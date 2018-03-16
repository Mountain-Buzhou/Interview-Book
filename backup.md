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

### commit message
```
init：项目初始化（用于项目初始化或其他某种行为的开始描述，不影响代码）
feat：新功能（feature）
fix：修补bug
docs：文档（documentation）
opt：优化和改善，比如弹窗进行确认提示等相关的，不会改动逻辑和具体功能等
style： 格式（不影响代码运行的变动）
refactor：重构（即不是新增功能，也不是修改bug的代码变动）
test：增加测试
other：用于难以分类的类别（不建议使用，但一些如删除不必要的文件，更新.ignore之类的可以使用）
```
