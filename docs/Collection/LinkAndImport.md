## Q: link和@import的区别？

## A:

1. link是HTML方式， @import是CSS方式
2. link最大限度支持并行下载，@import过多嵌套导致串行下载，出现FOUC
3. link可以通过rel="alternate stylesheet"指定候选样式
4. 浏览器对link支持早于@import，可以使用@import对老浏览器隐藏样式
5. @import必须在样式规则之前，可以在css文件中引用其他文件
6. 总体来说：link优于@import
