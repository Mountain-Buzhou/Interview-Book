# 闭包之魔芋理解

`Author: @魔芋`

### 【魔芋】概念解释：

01，在一个函数内声明一个函数，形成了嵌套函数。此时，外边的函数称为外部函数。内部的称为内部函数。或称为父函数和子函数。



02，闭包wiki:<https://en.wikipedia.org/wiki/Closure_%28computer_programming>

 

03，JS采用词法作用域（lexical scoping），函数的执行依赖于函数作用域，这个作用域是在函数定义时决定的，而不是函数调用时决定的。

- 词法作用域：词法作用域也叫静态作用域，是指作用域在词法解析阶段就已经确定了，不会改变。
- 动态作用域：是指作用域在运行时才能确定。



参看下面的例子，引自[杨志的回答](https://www.zhihu.com/question/20032419/answer/13742892)

```
var foo=1;

function static(){
    alert(foo);
}

!function(){
    var foo=2;
    static();

}();
```

在js中，会弹出1而非2，因为static的scope在创建时，记录的foo是1。
如果js是动态作用域，那么他应该弹出2





04，魔芋：识别闭包，在词法分析阶段已经确定了。

当外部函数运行的时候，一个闭包就形成了，他由内部函数的代码以及任何内部函数中指向外部函数局部变量的引用组成。





------





### 【Q】函数第一次被调用时，会发生什么？

当函数第一次被调用时，会创建一个执行环境（execution context）及相应的作用域链，并把作用域链赋值给一个特殊的内部属性（即`[[Scope]]`）。

然后，使用`this`、`arguments`和其他参数来初始化函数的活动对象（activation object）。

在作用域链中，内部函数的活动对象出于第一位，外部函数的活动对象始终处于第二位，外部函数的外部函数的活动对象处于第三位，……直至作为作用域链终点的全局执行环境。

每次调用JS函数时，会为之创建一个新的对象来保存所有的局部变量（函数定义的变量，函数参数。），把这个对象添加到作用域链中。函数体内部的变量都保存在函数作用域内。

我们将作用域链看做一个对象列表，而不是一个栈。（魔芋：栈是一种线性表，仅允许在表的一端进行插入和删除运算。）

当函数返回的时候，就从作用域链中将这个绑定变量的对象删除。

如果这个函数不存在嵌套的函数，也没有其他引用指向这个绑定变量的对象，它就会被当做垃圾回收掉（魔芋：这个操作由浏览器自动完成）。



### 【Q】闭包是什么？

闭包（closure）是可以访问外部函数作用域中的变量的函数。（外部函数的参数也可以访问）





### 【Q】为什么闭包函数可以访问外部函数的变量？

因为闭包函数的作用域链包含了外部函数的作用域。

 

### 【Q】如何创建闭包？

在一个函数类内创建另外一个函数。内部函数使用了外部函数的变量，就形成了闭包。



### 【Q】普通函数的内部函数是闭包函数么？

魔芋：不是。



### 【Q】闭包函数必须返回（return）么，return这个闭包函数？

魔芋：不必要返回，只要使用外部函数的变量即可。

代码：

```
function fn1() {
    var a = 1;
    


function fn2() {
    console.log(a);
}

fn2();


}

fn1();
```



### 【Q】 如果用不同的变量引用函数中的闭包函数。 它们是相同的么？

是不同的。

简单的例子：

```
function outter(){
    var x = 0;
    return function(){
        return x++;
    }
}
var a = outter();
console.log(a());
console.log(a());
var b = outter();
console.log(b());
console.log(b());
```

运行结果为：
0
1
0
1



### 【Q】闭包的用途？

- 可以创建私有变量。

因为只有闭包函数可以访问外部函数的变量。





### 【Q】请写出一个闭包实例？

```
function moyu(){
    var name = "魔芋";
    return function(){
        console.log(name+" 你好~");
}
}
var res = moyu();
res();//"魔芋 你好~"
```



![1527622788167](../../../moyu-note/JavaScript/submenu/closure_moyu.assets/1527622788167.png)







### 【Q】闭包的缺点：

- 闭包函数作用域中，使用的外部函数变量不会被立刻销毁回收，所以会占用更多的内存。过度使用闭包会导致性能下降。建议在非常有必要的时候才使用闭包。 



------

### 魔芋归纳的一些注意点：

01，同一个闭包函数，所访问的外部函数的变量是同一个变量。 

02，如果把闭包函数，赋值给不同的变量，那么不同的变量指向的是不同的闭包函数，所使用的外部函数变量是不同的。 

03，闭包函数分为定义时，和运行时。只有运行时，才会访问外部函数的变量。 

04，在for循环的闭包函数，只有在运行时，才在作用域中寻找变量。for循环会先运行完毕，此时，闭包函数并没有运行。 

例子：如果闭包中使用for的i。那么闭包中的i是for循环中的最后一个值。

05，如果在for循环中，使用闭包的自执行函数。那么闭包会使用for循环的变量i（0-*，假设i从0开始）。 

06，一个函数里，可以有多个闭包。 



### 【Q】闭包和内存泄漏？

在IE中，JS对象和DOM对象使用不同的垃圾收集机制。

事件绑定中的匿名函数也是闭包函数。

如果闭包函数中有HTML元素。那么该元素由于有引用，所以无法被回收。

```javascript
function moyu_test(){

var  _div = document.getElementById("moyu");

_div.onclick=function(){

	console.log(_div.innerHTML);

}

}

moyu_test();//这里_div元素有引用，除非浏览器关闭才会回收。


```

改进方式：主动解除引用。



```javascript
function moyu_test(){

var  _div = document.getElementById("moyu");

_div.onclick=function(){

	console.log(_div.innerHTML);

}

_div=null;//解除引用

}

moyu_test();


```



### 【Q】闭包中的this？

对于某个函数来说，如果函数在全局环境中，this指向window。

如果在对象中，就指向这个对象。 

而对象中的闭包函数，this指向window。因为闭包并不属于这个对象的属性或方法。

 

```javascript
var user = 'The Window';
var obj = {
    user : 'The Object',
    getUserFunction : function () {
        return function () { //闭包不属于obj，里面的this 指向window
            return this.user;
        };
    }
};
alert(obj.getUserFunction()()); //The window
//可以强制指向某个对象
alert(obj.getUserFunction().call(obj)); //The Object
//也可以从上一个作用域中得到对象
getUserFunction : function () {
    var that = this; //从对象的方法里得对象
    return function () {
        return that.user;
    };
}
```



### 【Q】闭包和arguments?

arguments是函数的实参对象。闭包有自己的arguments，所以无法直接访问外部函数的arguments。可以将外部函数的arguments保存到一个变量中，然后在闭包中使用。





------

### 【判断题】

###### 题1：

```javascript
function createFunctions(){
    var result = new Array();

    for (var i=0; i < 10; i++){
        result[i] = function(num){
            return function(){
                return num;
            };
        }(i);
    }

    return result;
}

var res = createFunctions();
console.log(res[5]());
```



结果为5；

魔芋解析：在for循环中，数组元素赋值调用了闭包函数，此时`num为`for循环中的`i`值。

考察点：闭包函数在调用时，从作用域查找变量值。



###### 题2：

```js
var subduction =(function(){
    
var moyu = 0;
return function(){
    return moyu -=1;
}


})();

subduction();
subduction();
subduction();

/*moyu等于几？*/
```

结果为-3。

考察点：同一个闭包变量使用同样的变量。



###### 题3：



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

![1527656311145](../../../moyu-note/JavaScript/submenu/closure_moyu.assets/1527656311145.png)



 魔芋的解释：

01，o.add();

第一个console.log('add', this);//输出o这个对象。

在对象方法中，方法中的this指向这个对象。

第一个this.num = 3;

表示：o.num =3;

02，匿名自执行函数中的this，指向全局环境变量。为window。

所以

(function() {

​            console.log('closure', this);//这里的this是指向哪里？window

​            console.log(this.num);//1

​            this.num = 4;//window.num = 4;

})();

匿名自执行函数的this.num为window.num。为1。

this.num = 4;//window.num = 4;

03，

console.log(o.num);//3，因为前面修改了o.num=3；

04，console.log(num);//4

这里，num为window.num。

05，var sub = o.sub;

sub();//4

魔芋：sub为函数。全局函数中的this指向全局环境，也就是window。

所以为window.num为4；

 



###### 题4：

```js
for(var i = 1; i < 10; i ++){
    setTimeout(function(){
        console.log(i);
    }, 1000);
}
```



结果为1秒后的9个10。

![1527656577721](../../../moyu-note/JavaScript/submenu/closure_moyu.assets/1527656577721.png)

魔芋解析：for循环结束后，`i`值为10，在任务队列中加入9个定时器。1秒后，调用闭包函数，此时闭包函数在作用域中使用`i`值。

考察点：闭包函数在调用时，使用变量的当前值。



###### 题5：

```js
// 变体一
for (var i = 1; i < 10; i++) {
    (function(i){
        setTimeout(function(){
            console.log(i);
        }, i * 1000);
    })(i);
}
```



结果，每隔1秒，依次的输出1到9。

![1527657051063](../../../moyu-note/JavaScript/submenu/closure_moyu.assets/1527657051063.png)

魔芋解析：在for循环中，每次调用匿名自执行函数。定时器中的闭包函数使用的是传递进来的for的`i`值（1-9）。

考察点：闭包函数在调用时，使用变量的当前值。



###### 题6：

```js
// 变体二
for (var i = 1; i < 10; i++) {
    (function(){
        setTimeout(function(){
            console.log(i);
        }, i * 1000);
    })();
}
```



结果：每隔1秒输出10。进行9次。

![1527657323488](../../../moyu-note/JavaScript/submenu/closure_moyu.assets/1527657323488.png)



魔芋解析：每次for循环中，给任务队列加入定时器，定时器中的闭包函数，在定义时，并没有传递i值。所以闭包函数在调用时，在自己的作用域中使用for循环结束后的i值。





###### 题7：

```js
// 变体三
for (var i = 1; i < 10; i++) {
    (function(){
        setTimeout(function(i){
            console.log(i);
        }, i * 1000);
    })();
}
```

结果：

依次输出9个undefined。

![1527657728413](../../../moyu-note/JavaScript/submenu/closure_moyu.assets/1527657728413.png)



魔芋解析：在定时器中的闭包函数，它有形参`i`，但是，并没有传递实参。所以形参i的值为undefined。i*1000 的i还是来自for循环中的i。









