## Q: 闭包 javascript

## A: 

`Author: @liyuk`

闭包这个东西，无疑是js中最为坑的一个地方。   
暂时不想写了，高程和相关资料很多。  
重点是对于函数构成作用域的理解，理解了什么是函数作用域，正推、反推都可以解决大部分的闭包问题。

这里推荐一篇翻译的很好的文章，讲清楚了闭包的原理。

[【译】看权威的wikipedia如何解释闭包 译者@ne_smalltown](https://segmentfault.com/a/1190000007386162)

再一个就是闭包的变体题目实在是非常多，如果认真准备的话，去多刷刷变体题目吧。   
这里写几个闭包相关的题目。

```js
var num = 1;
var o = {
    num: 2,
    add: function() {
        this.num = 3;
		console.log('add', this);
        (function() {
			console.log('closure', this);
            console.log(this.num);
            this.num = 4;
        })();
        console.log(this.num);
    },
    sub: function() {
        console.log(this.num);
    }
}
o.add();
console.log(o.num);
console.log(num);
var sub = o.sub;
sub();

// 请写出输出结果
```

```js
function fun(n,o) {
  console.log(o)
  return {
    fun:function(m){
      return fun(m,n);
    }
  };
}
var a = fun(0);  a.fun(1);  a.fun(2);  a.fun(3);//undefined,?,?,?
var b = fun(0).fun(1).fun(2).fun(3);//undefined,?,?,?
var c = fun(0).fun(1);  c.fun(2);  c.fun(3);//undefined,?,?,?

//问:三行a,b,c的输出分别是什么？
```

```js
// 最基础题
for(var i = 1; i < 10; i ++){
    setTimeout(function(){
        console.log(i);
    }, 1000);
}

// 变体一
for (var i = 1; i < 10; i++) {
    (function(i){
        setTimeout(function(){
            console.log(i);
        }, i * 1000);
    })(i);
}

// 变体二
for (var i = 1; i < 10; i++) {
    (function(){
        setTimeout(function(){
            console.log(i);
        }, i * 1000);
    })();
}

// 变体三
for (var i = 1; i < 10; i++) {
    (function(){
        setTimeout(function(i){
            console.log(i);
        }, i * 1000);
    })();
}
```

理解闭包形成的原因，理解**定义时**和**运行时**的区别。
