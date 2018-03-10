## Q: Currying

## A: 

`Author: @liyuk`
`Proofreader: @沉禹`

### 简单介绍
柯里化又叫部分求值，是把接受多个参数的函数变换成接受一个单一参数（最初函数的第一个参数）的函数，并且返回接受余下的参数而且返回结果的新函数的技术。    

---
### 基础阅读

如果需要了解学习柯里化的概念，何幻大神的《柯里化的前生今世》系列十三篇文章讲的非常全，并且很深入浅出、浅显易懂（数学不好就难懂了）  

[知乎专栏：业余程序员的个人修养](https://zhuanlan.zhihu.com/self-discipline?group_id=954635149120458752)  


对于使用Javascript来学习函数式编程，槽点很多，具体可以看看这两个链接：  

[Functional Programming in Javascript === Garbage](https://awardwinningfjords.com/2014/04/21/functional-programming-in-javascript-equals-garbage.html)   

[贺老关于《Functional Programming in Javascript === Garbage》的吐槽](https://github.com/hax/hax.github.com/issues/14)   

[Jim的吐槽: JavaScript可以作为函数式语言学习吗？ - Jim Liu的回答 - 知乎](
https://www.zhihu.com/question/36525679/answer/67924020)

---
### 面试题库

柯里化(Currying)具有：延迟计算、参数复用、动态生成函数的作用。相关的出题都是围绕着三个点来的，同时需要明确理解Clojure与Currying之间的联系（[简单了解Clojure与Lisp](https://www.jianshu.com/p/a41a9a46e0a1?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation))。但网上的资料都过于浅显，所以还是需要自己去做一些深入的了解。  
接下来说面试题，主要引用了[柯里化在工程中有什么好处? - 赵雨森的回答 - 知乎](
https://www.zhihu.com/question/37774367/answer/192978122)，以及我之前积累的几段代码。

#### 延迟计算

```js
// curring 函数
function currying(func) {
    const args = [];
    return function result(...rest) {
        if (rest.length === 0)
            return func(...args);
        args.push(...rest);
        return result;
    }
}

const add = (...args) => args.reduce((a, b) => a + b);

const sum = currying(add);

sum(1,2)(3);
sum(4);
sum(); // 10

```

这个题目稍微简化一下，当我们不使用currying函数、不存在拆分arguments，而是只是实现一个简单功能的时候，比如
`sum(1)(2)(3)() = 6`这样的问题时，可以使用递归进行实现，这里就不进行代码实现了。   
同时我们也许可以选择一个更难一点的问题，比如`sum(1)(2)(3) = 6`这个问题的实现，则需要考虑取值的结果，实际上考点一个是`递归`，一个是`求值`，也就是`valueOf`和`toString`。
```js
// add(1)(2)(3)(4)

// method 1
function add(num) {
    var sum = 0;
    sum += num;
    var tempFun = function(nnum) {
        if (arguments.length === 0) {
            return sum;
        } else {
            sum += nnum;
            return tempFun;
        }
    }
    tempFun.valueOf = function() {
        return sum;
    }
    tempFun.toString = function() {
        return sum + '';
    }
    return tempFun;
}

// method 2
function add(num) {
    var args = [];

    function addNum() {
        if (arguments.length === 0) {
            return calulate;
        } else {
            Array.prototype.push.apply(args, Array.prototype.splice.call(arguments, 0));
            return addNum;
        }
    }

    function calulate() {
        var result = args.reduce((previousValue, currentValue) => {
            return previousValue + currentValue;
        }, 0);
        args = [];
        return result;
    }

    addNum.valueOf = function() {
        return calulate();
    }
    addNum.toString = function() {
        return calulate() + '';
    }
    return addNum;
}


// add(args) = sum(1, 2, 3, 4)
function add(args) {
    return sum.apply(this, args);
}
```

#### 参数复用  

例如兼容现代浏览器和IE浏览器的添加事件方法，我们通常会这样写：
```js
const addEvent = function (elem, type, fn, cature) {
    if (window.addEventListener) {
        elem.addEventListener(type, (e) => fn.call(elem, e), capture);
    } else if (window.attachEvent) {
        elem.attachEvent('on' + type, (e) => fn.call(elem, e);
    }
}
```
这种方法显然有个问题，就是每次添加事件处理都要执行一遍`if {...} else if {...}`。其实用下面的方法只需判断一次即可：
```js
const addEvent = (function () {
    if (window.addEventListener) {
        return (elem, type, fn, capture) => {
            elem.addEventListener(type, (e) => fn.call(elem, e), capture);
        };
    } else {
        return (elem, type, fn, capture) => {
            elem.attachEvent('on' + type, (e) => fn.call(elem, e);
        };
    }
})();
```
这个例子，第一次`if {...} else if {...}`判断之后，完成了部分计算，动态创建新的函数来处理后面传入的参数，以后就不必重新进行计算了。这是一个典型的柯里化的应用。

#### 动态生成函数

当多次调用同一个函数，并且传递的参数绝大多数是相同的时候，那么该函数就是一个很好的柯里化候选。例如我们经常会用`Function.prototype.bind`方法来解决上述问题。
```js
const obj = { name: 'test' };
const foo = function (prefix, suffix) {
    console.log(prefix + this.name + suffix);
}.bind(obj, 'currying-');

foo('-function'); // currying-test-function
```
与`call`/`apply`方法直接执行不同，`bind`方法将第一个参数设置为函数执行的上下文，其他参数依次传递给调用方法（函数的主体本身不执行，可以看成是延迟执行），并动态创建返回一个新的函数。这很符合柯里化的特征。下面来手动实现一下`bind`方法：
```js
// es6
Function.prototype.bind = function (context, ...args) {
    return (...rest) => this.call(context, ...args, ...rest);
};

// es5
Function.prototype.bind = function(oThis) {
    var args = Array.prototype.slice.call(arguments, 1);
    var fToBind = this;
    var F = function() {};
    var fBound = function() {
        return ftoBind.apply(this instanceof F ? this : oThis || this,
            args.concat(Array.prototype.slice.call(arguments)));
    }
    F.prototype = fToBind.prototype;
    fBound.prototype = new F();
    return fBound;
}

```
---
### uncurrying
```js
Function.prototype.uncurry = function() {
    var _this = this;
    return function() {
        return Function.prototype.call.apply(_this, arguments);
    }   
}
```
- 为Function原型添加unCurrying方法，这样所有的function都可以被借用；
- 返回一个借用其它方法的函数，这是目的；
- 借用call方法实现，但call方法参数传入呢？借用apply，至此完毕。

---
### 推荐库
#### Ramda.js
函数式编程优势主要体现在**数据不变性**和**函数无副作用**两方面。虽然 Ramda 没有对此特别加强，但它在这两方面支持的非常好。  
Ramda 的目标更为专注：专门为函数式编程风格而设计，更容易创建函数式 pipeline、且从不改变用户已有数据。
Ramda 主要特性如下：
- Ramda 强调更加纯粹的函数式风格。数据不变性和函数无副作用是其核心设计理念。这可以帮助你使用简洁、优雅的代码来完成工作。
- Ramda 函数本身都是自动柯里化的。这可以让你在只提供部分参数的情况下，轻松地在已有函数的基础上创建新函数。
- Ramda 函数参数的排列顺序更便于柯里化。通常最后提供要操作的数据。
最后两点一起，使得将多个函数构建为简单的函数序列变得非常容易，每个函数对数据进行变换并将结果传递给下一个函数。Ramda 的设计能很好地支持这种风格的编程。
[Document](http://ramdajs.com/0.19.0/index.html)
[Github](https://github.com/ramda/ramda)

#### Lodash.js / Underscore.js

Lodash
是一个一致性、模块化、高性能的 JavaScript 实用工具库。  

[Lodash document](https://www.lodashjs.com)  

Underscore一个JavaScript实用库，提供了一整套函数式编程的实用功能，但是没有扩展任何JavaScript内置对象。它是这个问题的答案：“如果我在一个空白的HTML页面前坐下， 并希望立即开始工作， 我需要什么？“...它弥补了部分jQuery没有实现的功能,同时又是Backbone.js必不可少的部分。

[Underscore document](http://underscorejs.org)

---
## Roast: 
在自己并没有彻底吃透的区域，搬运其实也有风险的，可能会有知识误区，不仅误导自己也误导他人。  
因此我也只能说是在Javascript这门语言的fp（函数式编程）上，稍微能够理解`一点点`这种并不太能广泛应用却可以用来吹逼的知识点，因而觉得整理的资料也许还是有些用处。  
事实上，Javascript并不太适合用于学习fp，因为业界对于fp这个东西，除去对于表层概念的瞎吹，核心的问题并没有得到解决。而对于Lodash这类库的使用，也更多表现为基础操作库，而并非是应用fp的一些核心概念，`活生生用得像个语法糖一样`。  
如果需要再进一步的学习了解，可以看看ClojureScript相关资料，解决了一些Javascript在fp上的不彻底的一些问题（具体问题我也无法举例，因为学习不彻底）。再一个可以看看youtube上这个视频[ClojureScript for Skeptics - Derek Slager](https://www.youtube.com/watch?v=gsffg5xxFQI)。  

---
## 扩展阅读
**《泛函分析》**