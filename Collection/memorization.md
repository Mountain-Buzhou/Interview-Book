## Q: 函数记忆是什么？什么场景下使用？（动态规划）

## A：

01，将上次计算结果保存起来的函数，称为有记忆能力（memorization）的函数。

```
function memorize(f) {
    var cache = {}; 
    return function() {
         var key = arguments.length + Array.prototype.join.call(arguments,",");
         if (key in cache) return cache[key];
         else return cache[key] = f.apply(this, arguments);
    };
}
```

- 01，利用闭包，将结算结果保存在私有的缓存对象里。
- 02，将实参长度加实参参数作为缓存对象属性。
- 03，如果key属性不存在，就将结果保存在key属性的值。

下面的代码展示了如何使用memorize()：

```
// 返回两个整数的最大公约数
// 使用欧几里德算法:http://en.wikipedia.org/wiki/Euclidean_algorithm
function gcd(a,b) {                     // 这里省略对a和b的类型检查
    var t;                              // 临时变量用来存储交换数值
    if (a < b) t=b, b=a, a=t;           // 确保 a >= b
    while(b != 0) t=b, b = a%b, a=t;    // 这是求最大公约数的欧几里德算法
    return a;
}
var gcdmemo = memorize(gcd);
gcdmemo(85, 187) // => 17
```

代码分析By魔芋

var gcdmemo = memorize(gcd);

f=fcd(a,b);

第一次调用时，cache为空对象。 gcdmemo为返回的匿名函数。

key为285,187

第二次调用时，cache.key已存在，将直接返回计算值。

------

应用一：实现记忆功能的递归函数：

```
var factorial = memorize(function(n) {  
      return (n <= 1) ? 1 : n * factorial(n-1);
            });
factorial(5)            // => 120.对于4~1的值也有缓存
```

应用二：数组去重：

```
unction unique(arr) {
  var ret = []
  var hash = {}
  for (var i = 0; i < arr.length; i++) {
    var item = arr[i]
    var key = typeof(item) + item;
    if (hash[key] !== 1) {
      ret.push(item)
      hash[key] = 1
    }
  }
  return ret;
}
```

**