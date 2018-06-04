# Advanced

我们会尽可能地增加`Advanced`(进阶)这里面的题目的数量和难度，当然也包含很多基础知识点的详细内容。这里的知识点的区分暂时并不是特别明显，之后onion来整理这块儿内容。

## Browser

- [打开一个网页经历了那些过程？](http://web.jobbole.com/94150/)
- [浏览器加载白屏是什么原因？](/Collection/WhiteScreen.md)
- [千万访问量的项目，前端需要注意些什么？](/Collection/DozensOfVisits.md)

## JavaScript
这一章我们尽量带来较深层的JavaScript语言层次的问题，我们会拿出几个JavaScript较深入的点来讲。

- [表达式和语句有什么区别？如何把语句转换为表达式？](/Collection/ExpressionAndStatement.md)
- 什么叫执行上下文栈(Execution Context Stack)? 一个函数调用会产生多少个上下文环境？如何激活一个上下文，什么叫caller(调用者)，什么叫callee(被调用者)？给你一段代码能否画出执行过程中的上下文堆栈变化？
- 执行上下文包括哪些结构(状态/属性)，如何追踪关联代码的执行进度？
- eval在调用的时候有哪些特别的地方？eval函数自身会产生上下文吗？会影响当前的调用上下文吗？
- 什么叫变量对象？什么叫活动对象？
- [词法作用域是什么？闭包是如何形成的？](/Collection/closure_moyu.md)
- `var foo = function bar () {}` 命名函数表达式中(上述的foo函数)bar变量是定义在哪一层作用域的？
- [`(0, 1, 2)` 的结果是什么？](/Collection/NumberExpression.md)
-  `var foo = { value: 2, bar: function () { return this.value; }` 中`(foo.bar, foo.bar)()`的`this`值是什么？`(foo.bar = foo.bar)()`、`(false || foo.bar)()`呢?

## Application
这里将JavaScript除去基本语言特性之外的东西整理出来，主要是JavaScript在工程上的应用场景，以及一些原理性问题。

- [继承（重点）](/Collection/Inherit.md)
- [异步（重点）](https://blog.risingstack.com/writing-a-javascript-framework-execution-timing-beyond-settimeout/ )
- [new操作符做了什么](http://blog.csdn.net/aimingoo/article/details/6105048)
- [JavaScript 内存管理](https://github.com/Troland/how-javascript-works/blob/master/memory-management.md)
- [实现一个Promise](https://github.com/Liyuk/code-repertory/blob/master/promise/promise.js)
- [js模块化现状？AMD和CMD是什么？](https://segmentfault.com/a/1190000009591055)
- 如何在前端解析二进制？流媒体、图片二进制数据怎样渲染到页面上？
- [函数记忆是什么？什么场景下使用？（动态规划）](/Collection/memorization.md)
- 实现一个Lazyman [Answer 1](http://www.cnblogs.com/walls/p/6341614.html)  [Answer 2](http://web.jobbole.com/89626/)
- [实现throttle和debounce (必会)](https://jinlong.github.io/2016/04/24/Debouncing-and-Throttling-Explained-Through-Examples/)
- require.js的实现原理，[webpack的实现原理与loader的实现](http://taobaofed.org/blog/2016/09/09/webpack-flow/)
- [Babel是如何实现的](https://github.com/jamiebuilds/babel-handbook/blob/master/translations/zh-Hans/plugin-handbook.md)
- [前端工程师可以用编译做什么？](https://www.zhihu.com/question/274357154)
- [如何用正则表达式实现模板引擎？（正则表达式相关知识点）](http://louiszhai.github.io/2016/06/13/regexp/)

## HTML
- 讲一下whatwg标准上的event loop规范。(别说你没看过
- microTask的有哪些，Task的有哪些？（最好答出来所有的
- 构思一下利用Task和microTask来完成框架层面的时间调度( 比如vue是如何利用microTask来实现batch update的
- 讲一下你对web components的理解
- web worker适合哪些场景

## Function Program
- [闭包（重点）](/Collection/Clojure.md)
- [柯里化（Currying）](/Collection/Currying.md)

## HTTP
- http1.0和http1.1的区别
- http请求码有哪些？206、302、303、304、307
- 能说下304具体怎样实现吗？
- http缓存逻辑是怎样的？协商缓存与强缓存？Last-Modified / Etag / Expires / Cache-Control ？
- osi七层协议和tcp/ip四层协议
- 三次握手和四次握手
- 跨域是什么？http协议中如何判断跨域？如何解决跨域问题？
- http2具体内容？SDPY了解么？
- HTTPS如何实现？tsl/ssl是什么？对称加密、非对称加密在什么时候、对什么数据加密？
- DNS劫持是什么？
- [浏览器在一次 HTTP 请求中，需要传输一个 4097 字节的文本数据给服务端，可以采用那些方式?](/Collection/SendData.md)

## Optimization
- 首屏优化
- 预加载资源、预解析DNS
- 懒加载图片怎么做
- [iframe一般怎么使用？](/Collection/iframeUse.md)
- window.onload、document.ready顺序？iframe会阻塞吗？
- cdn是什么？如何查找最近的cdn？
- gzip、chucked
- 前端安全：xss攻击和防范、CSRF、CORS
- 硬件加速怎样开启
- 优化中会提到缓存的问题，问：静态资源或者接口等如何做缓存优化
- 页面DOM节点太多，会出现什么问题？如何优化？

## Products
这里主要是一些生产中真实存在的问题。

- 一个feed流，有哪些展现方式？如果当前页面可视区有5个格子，而你有20条信息需要展示，请问有哪些自动展示的算法？
- [移动端的缓存机制有哪几种？](https://segmentfault.com/a/1190000004132566)
- 小程序如何与native通信？react-native实现原理？jsbridge如何实现？
- 过万条数据如何加载和渲染？
- 如何在前端解析二进制，流媒体、图片二进制数据怎样渲染到页面上？
- 如何解析二进制音频、视频？
- 文件如何显示上传百分比？
- 如何制作一个富文本，需要考虑哪些结构？
- html5的播放器怎么做？视频直播如何在浏览器里面实现？HLS、RTMP
- 如何在浏览器里面裁剪图片？如何裁剪视频，对视频做逐帧分析？
- 如何实现一个具有引导功能的组件库？
- 如何封装一个Form和FormItem，使其能够跟input、select、checkbox、radio等组件进行 数据存储、数据校验（自定义逻辑）、校验反馈？
- echart这类图像库的实现原理？
- i18n的国际化方案应该是怎样的？
- 数据埋点的意义是什么？应当针对哪些数据进行埋点？如何构建一个埋点系统？
- 小程序的实现原理是什么？[这【五篇】文章将带你深入了解「微信小程序」](https://github.com/phodal/articles/issues/32)
- 小游戏的实现原理是什么？[Cocos知乎文章：微信小游戏上手](https://www.zhihu.com/org/cocos-3/posts)、[深入理解使用白鹭引擎开发微信小游戏的构建机制](https://zhuanlan.zhihu.com/p/32749103)
- mpvue这样h5转小程序的工具的原理是什么？怎样去实现？[官方宣传文档](https://zhuanlan.zhihu.com/p/34450979)、[如何看待美团开源mpvue](https://www.zhihu.com/question/268421668)

## Whiteboard
前端所需要的白板面试题算法难度不高，主要针对JavaScript基础类型的遍历与扩展。   
但是如果有喜欢考算法题的，可能会考的很难。所以还是推荐如果有时间的话，可以去把leetcode的easy和medium刷一下，hard可以跳过不看。  
国内的面试难度其实很小，有兴趣的朋友看看国外的面试题就知道自己有多么菜了。

- parseQuery
- flatten
- [乱序算法（Fisher–Yates）](https://github.com/Liyuk/Interview-Questions-Answers/issues/1)
- [模版引擎](/Collection/Template.md)
- 反转二叉树
- 将两个有序数组合并成为一个有序数组
- 全选和单行选中的联动
- 数组去重，考虑object、NaN、数字1，弱类型转换
- 汉诺塔的实现
- bind
- currying
- 一个无重复元素的数组，求所有两数之和为k的组合
- 变体题：一个无重复元素的数组，求元素和（元素个数小于n）为k的组合
- [实现events(发布订阅/观察者模式)](/Collection/Events.md)
- 找出数组中最大的两数之差
- 棋盘最短路：动态规划、搜索+剪枝、时间优化、空间优化
- 二叉树遍历：前序、后序、中序，时间复杂度，空间复杂度O(1)，递归非递归
- 双向链表寻找中间的元素，单向链表寻找中间的元素
- 查找数组中第k大的数 



## System Design
这类题目非常繁琐以及复杂，主要出现在高级工程师的最终面试里。对于不同层级的开发人员的回答要求各不相同，但有必要全局地了解整个系统的设计结构和基本概念。  

- 请设计一个前端的组件库，包括组件的分类、具体的内容、API的规范、协作开发的规范。
- [System Design Primer 中文](https://github.com/donnemartin/system-design-primer/blob/master/README-zh-Hans.md)
- [System Design Interview](https://github.com/checkcheckzz/system-design-interview)

- [面试常问问题及问答思路](/Collection/OftenAsked.md)

