## Q: 实现一个基本的模版引擎

## A: 

`Author: @liyuk`

主要思路为使用正则表达式匹配出全局的变量，替换称为对应的data中的数据。

```js
// 封装
function _.template(templateId, data){
    // 获取模板字符串
    var str = document.getElementById(templateId).innerHTML;
    // 正则表达式  标记<%= name %> 这里的变量命名规则只能是字母或数字不能有特殊字符
    var reg = /<%=\s*(\w+)\s*%>/;
    // exec返回一个匹配数组
    var arrReg = '';
    while (arrReg = reg.exec(str)){
        str = str.replace(arrReg[0],data[arrReg[1]]);
    }
    return str;
}

var data = {
    "name":"haha",
    "age":22
};
// 调用模板引擎
var html = _.template('template',data);
document.body.innerHTML = html; 
```

```html
<!--html template-->
<script type="text/template" id="template">
    <div>这是一个div<%= name %></div>
    <p>这是一个p<%= age %></p>
</script>
```

简单的实现实际上就是正则匹配，加上字符串替换。  
- 如果涉及对象的key调用，要用正则做点的分隔来实现层级区分
- 如果再涉及自定义属性，那么需要加入语法解析的内容去获取保留字面量以及对应所匹配的参数，类似v-if、v-for这类
- 同时还需要涉及到模板的执行语句，预编译
- 唯一标识符用来强调模板中的字面量
- xss漏洞防范，使用转义字符
```js
function strip(html) {
    return String(html)
    .replace(/&/g, '&amp;')//&
    .replace(/</g, '&lt;')//左尖号
    .replace(/>/g, '&gt;')//右尖号
    .replace(/"/g, '&quot;')//双引号"
    .replace(/'/g, '&#039;');//IE下不支持&apos;'
}
```

## Roast
这个题很简单，基本概念。
但是如果深入的话，我们可以推出如下题目：
- 正则引擎如何实现？
- 模板引擎中设计的词法分析、语法分析、语义分析是什么？
- 能否用非正则的方式实现模板引擎？
- 如何利用递归和非递归分别实现AST树？
- 模板引擎中内容发生变化时，AST树执行了什么操作？