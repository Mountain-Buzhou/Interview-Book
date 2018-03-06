## Q: 继承

## A: 

`Author: @liyuk @高程（三）`

这部分内容其实在2015年就有过详细的编写，但是最近发现当年的代码似乎并没有很明白的阐述原理，重新翻了高程整理一下。  
特别强调一下，基本概念！基本概念！基本概念！（怨念）  

## ES5

### 1-原型链
```js
function Super() {}

function Sub() {}

// 继承
Sub.prototype = new Super();

// 生成实例
var sub = new Sub();

```

- 所有的类型默认原型为Object
- 确定原型和实例的关系
```js
// instanceof
console.log(sub instanceof Sub);
console.log(sub instanceof Super);
console.log(sub instanceof Object);

// isPrototypeOf
console.log(Object.prototype.isPrototypeOf(sub));
```
- 定义方法时，要注意区分子类和超类的方法定义，使用字面量创建原型方法会重写原型链
```js
Sub.prototype = {
    name: 'liyuk'
}
```

#### 注意
- 如果原型包含引用类型，所有实例会共享该类型
- 创建子类型时，无法在不影响其他实例的情况下，给超类的构造函数传递参数  


**实际使用时会较少单独使用原型链**

### 2-构造函数

```js
function Super() {};

function Sub() {
    // 继承
    Super.call(this); // apply 也可以
}

// 生成实例
var sub = new Sub();
```
- 子类型构造函数可以向超类型构造函数传递参数
```js
function Super(name) {
    this.name = name;
}

function Sub() {
    Super.call(this, 'liyuk');
}
```
#### 注意
- 函数无法复用

### 3-组合继承
即将原型链和构造函数组合在一起。  
通过原型链实现对原型属性和方法的继承，通过构造函数来实现对实例属性的继承。
```js
function Super() {};

function Sub(name) {
    // 构造函数继承
    Super.call(this, name);
};

// 原型链继承
Sub.prototype = new Super();
// 增强对象
Sub.prototype.constructor = Sub;

// 生成实例
var sub = new Sub();
```
**最常用的的继承方法**
#### 注意
- 会调用两次超类型的构造函数：一次是在创建子类型原型，一次是在子类型构造函数内部

### 4-原型式继承
借助原型可以基于已有的对象创建新对象，同时还不必因此创建自定义类型。
```js
function _object(o) {
    // 临时构造函数
    function F() {};
    F.prototype = o;
    return new F();
}

var Super = {};

// 继承
var sub = _object(Super);
```
es5中的`Object.create`与`_object`实现类似，都是用来创建新对象，即副本。   
#### 注意
- 可以理解为浅拷贝，引用类型依旧会指向同一个地址，与原型链继承一样存在共享值的问题。

### 5-寄生式继承
创建一个仅用于封装继承过程的函数，该函数内部以某种方式增强对象，最后（像）做完所有工作后返回对象。
```js
function _create(o) {
    var clone = _object(o);
    // method
    return clone;
}
```
寄生本质上就是进行浅拷贝后生成了新的对象，然后在新的对象上去添加方法，最后返回该新对象。从而实现不对原对象进行修改，并获得了原对象所有方法。

### 6-寄生组合式继承
组合式继承会有两次调用超类型构造函数的问题。

```js
function Super() {};

function Sub(name) {
    // 构造函数继承
    Super.call(this, name);  // 第二次调用Super
};

// 原型链继承
Sub.prototype = new Super();  // 第一次调用Super
// 增强对象
Sub.prototype.constructor = Sub;

// 生成实例
var sub = new Sub();
```
第二次在Sub构造函数内部调用Super时，生成了新的属性，从而屏蔽了原型中（超类型）的同名属性。  

寄生组合式继承，**即通过构造函数来继承属性，通过原型链的混成形式来集成方法。**  
基本思路是**不必为了指定子类型的原型而调用超类型的构造函数**  
```js
// 寄生
function inherit(sub, super) {
    // 高程三中的写法是 var prototype = Object(super.prototype);
    // 这样写可能有些问题，会污染超类型的原型，保持疑惑
    // 所以有可能是用Object.create，或者上文提到的原型式继承_obejct，或者寄生式继承的_create
    // Comment: @bramble
    var prototype = Object(super.prototype);         // 创建对象，创建超类型原型副本
    prototype.constructor = sub;                     // 增强对象，弥补因重写原型而失去的默认constructor
    sub.prototype = prototype;                       // 指定对象
}
```
修改后的寄生组合模式为
```js
function Super() {};

function Sub() {
    // 使用构造函数来继承属性
    Super.call(this);
};

// 使用寄生来混入原型链
_inherit(Sub, Super);

// 生成实例
var sub = new Sub();

```
**寄生组合式继承是最`引用`类型最理想的继承范式**

### 7-Object.create `@MDN` `兼容性：IE9+`
```js
// Super - 父类(superclass)
function Super() {
  this.x = 0;
  this.y = 0;
}

// 父类的方法
Super.prototype.move = function(x, y) {
  this.x += x;
  this.y += y;
  console.info('Super moved.');
};

// Sub - 子类(subclass)
function Sub() {
  Super.call(this); // call super constructor.
}

// 子类续承父类
Sub.prototype = Object.create(Super.prototype);
Sub.prototype.constructor = Sub;

// 因为使用“.prototype =...”后,constructor会改变为“=...”的那个
// constructor，所以要重新指定.constructor 为自身。
```

#### polyfill
尽管在 ES5 中 Object.create支持设置为[[Prototype]]为null，但因为那些ECMAScript5以前版本限制，此 polyfill 无法支持该特性。

```js
if (typeof Object.create !== "function") {
    Object.create = function (proto, propertiesObject) {
        if (typeof proto !== 'object' && typeof proto !== 'function') {
            throw new TypeError('Object prototype may only be an Object: ' + proto);
        } else if (proto === null) {
            throw new Error("This browser's implementation of Object.create is a shim and doesn't support 'null' as the first argument.");
        }

        if (typeof propertiesObject != 'undefined') throw new Error("This browser's implementation of Object.create is a shim and doesn't support a second argument.");

        function F() {}
        F.prototype = proto;

        return new F();
    };
}
```

## ES6 
### Class extends `@ruanyifeng`
es6的class其实就是个语法糖，babel转出来的依旧是寄生组合式继承。
具体的使用没有太多的可以说的，需要注意super即可以当函数，也可以实例。这部分不做细说，因为很复杂，有兴趣参考[es6 Class的继承](http://es6.ruanyifeng.com/#docs/class-extends#super-关键字)。  
需要注意的是，**ES5的继承，实质是先创造子类的实例对象this，然后再将父类的方法添加到this上面（Parent.apply(this)）。ES6 的继承机制完全不同，实质是先创造父类的实例对象this（所以必须先调用super方法），然后再用子类的构造函数修改this。**

### Object.setPrototypeOf
将一个指定的对象的原型设置为另一个对象或者null  

```js
// 语法
Object.setPrototypeOf(obj, prototype)

// 实现原理
Object.setPrototypeOf = Object.setPrototypeOf || function(obj, proto) {
    obj.__proto__ = proto;
    return obj; 
}
```

## 其他

### 继承在js当中的使用
- 高阶函数+工厂模式，可以实现继承的效果，原理偏向于构造函数实现继承
- react、vue等基础库对于各种基础类型的继承
- 复杂数据结构，诸如树、图等结构的复用和扩展
- canvas，基本图像类 派生出 线 圆 等各个需要的东西`@vamcc`

### 多继承
多继承是个伪命题，会导致菱形继承。
```js
B extends A
C extends A

D extends B, C

// 原型链合并
var sub = new Sub();

Sub.prototype = Object.assign({}, Sub.prototype, new Super2());

// 构造函数
function Sub() {
    Super1.call(this);
    Super2.call(this);
}
```
有兴趣去看看C++的菱形继承和虚继承，没兴趣不用在意。


## Roast
基本概念！基本概念！基本概念！  
一脸懵逼，生无可恋。
