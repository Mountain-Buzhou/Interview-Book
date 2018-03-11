# Interview-Questions-Answers

`Author: @liyuk @onion`

## Abstract
网络上的资源其实已经足够多了，所以在进行搜索的时候需要极大的筛选成本。为了减少这种低效的筛选，我将一些零散的知识整理在一起。希望阅读者不要抱着急功近利的想法来学习前端，扎根基础知识，才能更好地实现业务。  

`Entry`这个部分是几个前端知识库的链接，里面的内容比较浅显易懂。先看看整个结构性的题目，找到自己的知识的盲区，再去针对性学习。

`Collection`来自日常的面试、闲聊和偶尔的突发奇想，主要是觉得比较有趣，所以有做一些记录和分类。我和onion讨论了下，决定把这个模块分为三个大的内容，基础、进阶、框架，以及一些我之前整理的问题（与`Entry`有所部分重复）。

`Teamwork`这个部分则是关于团队管理、以及个人非技术上的一些发展相关的杂谈。

`Foundation`这个部分是计算机基础的概念，包括计算机组成原理、操作系统、编译原理、计算机网络、数据结构与算法、数据库系统、软件工程。这个部分就是所谓的补基础，构建完整的计算机体系结构，是向上成长的过程中必不可少的。**对于这种资讯类的repo来说，很少有提及基础的重要性，希望能够引起阅读者的重视**。    

**欢迎大家在issue里留下自己的奇思妙想，或者直接pr。**   

希望能够有助大家学习前端基础知识，以及提高姿势水平，跟大佬谈笑风生。
> 这篇文章并不能帮你提升到大佬的程度，但是可以作为查漏补缺的一个蓝图。

## Entry

我将**最基础**的前端的知识点分为三个部分：
- html+css+js（闭包、作用域、异步、继承）
- 网络、性能、测试、编码
- 自动化、工程化的开发  

这三个划分出来的只是最为基础的内容，学习这部分内容一方面需要对于书面知识的阅读，也需要在项目中加以实践。

### Naive
基础的面试问题题库已经有很多了，个人觉得这个里面的题大概是入门级别的，刚学的时候看看就可以了。
>[中文前端面试大全：qiu-deqing/FE-interview](https://github.com/qiu-deqing/FE-interview)  

白皮书里关于非技术的问题值得一读。
>[yangshun/tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook)

这本书里面梳理的非常全面，可以作为知识体系的梳理来进行学习。
>[front-end-developer-handbook-2018](https://frontendmasters.gitbooks.io/front-end-developer-handbook-2018/)  

### Interesting
关于一些Javascript里细节的点，可以看看这位大哥的博客，写的很清晰，代码实现很完整。
>[冴羽的博客](https://github.com/mqyqingfeng/Blog)   

《前端要给力之系列》是一系列非常有趣的文章，同时讲的非常深入
>[前端要给力之系列](/Entry/Geili.md)


---
## Collection

这个模块分为三个部分，即基础`Basic`，进阶`Advanced`，框架`Framework`，这是相当科学的划分。这里的内容主要是我们一起整理，以及日常讨论的一些题目，会有一些重复的内容，也可以独立作为一个基础知识体系。

---
### Basic

- html5新标签有哪些
- canvas、svg、webGL
- 语义化、SEO
- manifest、worker、socket
- input和textarea的区别
- 用一个div模拟textarea的实现
- css3有什么新特性，浏览器支持怎么样
- 伪类是什么？有哪些？会有哪些兼容性问题？如何处理？
- css预处理器知道吗？用过哪些？有什么优劣？后处理器知道吗？
- 盒模型有哪几种？怪异模式和标准模式？
- less、sass、postcss、prefix
- 层叠优先级
- 圣杯、双飞燕布局
- float清除浮动
- flex布局、 grid布局、table布局
- 绘制三角形、矩形、菱形、梯形（奇巧淫技，可以不问）
- spirte图（雪碧图）知道吗？svg雪碧图了解吗？
- px、em、rem、vw、vh？rem的根节点样式在什么时候设置？
- position有哪些？他们的定位原点是什么？
- 媒体查询用css好还是用js好？
- link和@import的区别？
- 响应式设计的css
- css低版本浏览器兼容问题，额外需要什么后缀来声明浏览器兼容
- !important意义，是否应当规避使用？
- BFC块级上下文、IFC，实现双栏高度对齐
- BEM命名法，有什么优势，有什么劣势
- 1px边框问题
- （水平）居中有哪些实现方式、（垂直）居中有哪些实现方式
- typeof以及弱类型转换规则？NaN、undefined、null
- dom的节点操作？能够背api还是知道api？
- ajax是什么？知道底层实现原理吗？知道fetch吗？自己封装过吗？
- GET、POST意义？restful架构下还有别的什么请求？OPTION请求是什么？
- 事件冒泡和事件捕获是怎样的？对应的默认方法有什么？一般在什么情况使用？
- call、apply、bind
- 如何判断数据类型
- hoisting是什么？具体表现是怎样的？
- 匿名函数是什么？函数表达式和函数声明的区别
- let、const暂时性锁区知道吗？表现是怎样的？
- 严格模式是什么？有什么好处？'use strict'
- arguments是什么类型？callee和caller有什么区别？
- 正则表达式规则？可以实现一个正则引擎吗？
- js的内存泄漏是怎样产生的？
- js引擎的垃圾回收机制
- Date.format实现过吗？思路是怎样的？
- 动画：setTimeout何时执行，requestAnimationFrame的优点
- require.js的实现原理，webpack的实现原理与loader的实现

---
### Advanced

我们会尽可能地增加`Advanced`(进阶)这里面的题目的数量和难度，当然也包含很多基础知识点的详细内容。这里的知识点的区分暂时并不是特别明显，之后onion来整理这块儿内容。

#### Browser

- [打开一个网页经历了那些过程？](https://github.com/qiu-deqing/FE-interview#从浏览器地址栏输入url到显示页面的步骤以http为例)
- [浏览器加载白屏是什么原因？](/Collection/WhiteScreen.md)
- [千万访问量的项目，前端需要注意些什么？](/Collection/DozensOfVisits.md)

#### JavaScript语言理解
这一章我们尽量带来较深层的JavaScript语言层次的问题，我们会拿出几个JavaScript较深入的点来讲。

- 表达式和语句有什么区别？如何把语句转换为表达式？
- 什么叫执行上下文栈(Execution Context Stack)? 一个函数调用会产生多少个上下文环境？如何激活一个上下文，什么叫caller(调用者)，什么叫callee(被调用者)？给你一段代码能否画出执行过程中的上下文堆栈变化？
- 执行上下文包括哪些结构(状态/属性)，如何追踪关联代码的执行进度？
- eval在调用的时候有哪些特别的地方？eval函数自身会产生上下文吗？会影响当前的调用上下文吗？
- 什么叫变量对象？什么叫活动对象？
- 词法作用域是什么？闭包是如何形成的？
- var foo = function bar () {} 命名函数表达式中(上述的foo函数)bar变量是定义在哪一层作用域的？

#### html
- 讲一下whatwg标准上的event loop规范。(别说你没看过
- microTask的有哪些，Task的有哪些？（最好答出来所有的
- 构思一下利用Task和microTask来完成框架层面的时间调度( 比如vue是如何利用microTask来实现batch update的
- 讲一下你对web components的理解

其他的待补充，先哄老婆睡觉了
#### 其他

- [继承（重点）](/Collection/Inherit.md)
- event loop [视频](https://www.youtube.com/watch?v=8aGhZQkoFbQ&feature=youtu.be), [SPEC](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop-processing-model)
- [异步（重点）](https://blog.risingstack.com/writing-a-javascript-framework-execution-timing-beyond-settimeout/ )
- [new操作符做了什么](http://blog.csdn.net/aimingoo/article/details/6105048)
- [js模块化现状？AMD和CMD是什么？](https://segmentfault.com/a/1190000009591055)
- 如何在前端解析二进制？流媒体、图片二进制数据怎样渲染到页面上？
- 函数防抖（debounce）和函数节流（throttle）是什么？有什么区别？
- 函数记忆是什么？什么场景下使用？（动态规划）

#### Function Program
- [闭包（重点）](/Collection/Clojure.md)
- [柯里化（Currying）](/Collection/Currying.md)

#### HTTP
- http1.0和http1.1的区别
- http请求码有哪些？206、302、303、304、307
- 能说下304具体怎样实现吗？
- osi七层协议和tcp/ip四层协议
- 三次握手和四次握手
- 跨域是什么？http协议中如何判断跨域？如何解决跨域问题？
- http2具体内容？SDPY了解么？
- HTTPS如何实现？tsl/ssl是什么？对称加密、非对称加密在什么时候、对什么数据加密？
- DNS劫持是什么？

#### Optimization
- 首屏优化
- 预加载资源、预解析DNS
- 懒加载图片怎么做
- iframe一般怎么使用？
- window.onload、document.ready顺序？iframe会阻塞吗？
- cdn是什么？如何查找最近的cdn？
- gzip、chucked
- 前端安全：xss攻击和防范、CSRF、CORS
- 硬件加速怎样开启
- 优化中会提到缓存的问题，问：静态资源或者接口等如何做缓存优化
- 页面DOM节点太多，会出现什么问题？如何优化？

#### Product
- 一个feed流，有哪些展现方式？如果当前页面可视区有5个格子，而你有20条信息需要展示，请问有哪些自动展示的算法？
- [移动端的缓存机制有哪几种？](https://segmentfault.com/a/1190000004132566)
- 小程序如何与native通信？react-native实现原理？jsbridge如何实现？
- 过万条数据如何加载和渲染？

#### Whiteboard
- parseQuery
- flatten
- [乱序算法（Fisher–Yates）](https://github.com/Liyuk/Interview-Questions-Answers/issues/1)
- [模版引擎](/Collection/Template.md)
- 棋盘最短路（动态规划）
- 反转二叉树
- 二叉树遍历（前序、后序、中序）
- 将两个有序数组合并成为一个有序数组
- 双向链表寻找中间的元素，单向链表寻找中间的元素
- 全选和单行选中的联动
- 数组去重，考虑object、NaN、数字1，弱类型转换
- bind
- currying
- 查找数组中第k大的数
- 一个无重复元素的数组，求所有两数之和为k的组合
- 变体题：一个无重复元素的数组，求元素和（元素个数小于n）为k的组合
- [实现events(发布订阅/观察者模式)](/Collection/Events.md)
- 找出数组中最大的两数之差

#### Command
- shell/bash命令
- git命令

---
### Framework

#### React
- React的生命周期mount和update描述下
- [React的生命周期中的isBatchingUpdates了解吗？Transaction知道吗](https://zhuanlan.zhihu.com/p/20328570)
- React的vdom如何实现？jsx是怎样解析的？
- React的diff/patch算法原理
- React的组件逻辑（受控、非受控）？如何搭建一个组件库
- React的数据流，flux相关
- Redux、Mobx、Rxjs，发布订阅模式、观察者模式
- Redux解决了什么痛点（有什么优点），又有什么缺点
- Redux的中间件有哪些？redux-actions、redux-promise、redux-thunk、redux-saga、redux-immutable了解过哪些？说说差异   
- Redux有什么优化方案？
- SSR了解过吗？怎样做？
- React-Native了解过吗？JavascriptCore是什么？

#### Vue
- Vue是如何设计响应式系统的？
- 什么时候使用computed, methods, watch？之间有什么样区别？
- template 和 render(jsx) 有什么的联系？
- this.$nextTick是如何设计的？

#### AngularJS
尽管angularJS已经基本退出了历史舞台，但是详细有的同学还是做过相关的项目，并很有可能被面试官问起。
- angularJS的数据绑定采用什么机制？详述原理
- 如果通过angularJS的 directive/component 规划一套全组件化体系，可能遇到哪些挑战？
- 一个angularJS应用应当如何良好地分层？
- ng-click中写的表达式，能使用JS原生对象上的方法，比如Math.max之类的吗？为什么？

---
## Team Management
这部分内容更多是非技术方向上的一些杂谈，看看就好。
### Management
- [给你一个二十人的新团队，你作为前端负责人你怎样去做？](/Teamwork/Team.md)
### Growing
- [工程师的阶段是怎样的？不同阶段应该具备怎样的技能？](/Teamwork/Stages.md)

---
## Foundation
我非常希望看到这里的同学能够认认真真去系统性的学习整个计算机体系结构。因此我将各个模块中偏向应用的东西都梳理了出来。这些梳理出来的点比较偏工程，稍做迁移就可以应用在我们工作当中。学习的时候可以暂时根据这些梳理出来的关键字去过一下知识点。  

我省略了《软件工程》与《数据库系统》的内容，因为前者方法论适合实践总结，后者我还不太熟悉。我推荐一本《计算机程序的构造和解释（SICP）》，是MIT本科的第一门课，讲述如何构造和分析复杂系统（程序）。这些书我自己也定期的回顾，之前与大佬讨论，不论科班还是非科班出身，不断回顾并思考计算机基础的东西，是非常重要的。
![基础书籍](/assets/imgs/books.jpeg)

### Operating System
- 进程与线程
- 虚拟地址，物理地址
- 进程间通信：临界区、忙等待互斥、睡眠与唤醒、信号量、互斥量、管程、消息传递、屏障、避免锁
- 进程调度策略：批处理、交互式、实时；
- 批处理调度：FCFS、SJF、SRTF
- 交互式调度：轮转、优先级、多级队列、最短进程优先、保证调度、彩票调度、公平分享调度
- 实时调度：硬实时、软实时、周期性
- [IPC问题：读者-写者、生产者-消费者、哲学家进餐、银行家算法](https://www.zybuluo.com/zhengbuqian/note/243560)
- 页面置换算法：最优页面置换算法、最近未使用页面置换算法（NRU）、先进先出页面置换算法（FIFO）、第二次机会页面置换算法、时钟页面置换算法（clock）、最近最少使用页面置换算法（LRU）、软件模拟LRU、工作集页面置换算法、工作集时钟页面置换算法

### Computer Organization
- 缺页中断——FIFO、LRU、OPT三种置换算法
- 流水线、指令集

### Network
- [帧、报文、报文段、分组、包、数据报的概念](http://www.cnblogs.com/sddai/p/5649939.html)
- DNS原理
- UDP和TCP
- 可靠性数据传输原理、拥塞控制原理
- 路由选择：RIP、OSPF、BGP
- 差错检验和纠正技术
- 计算机网络安全

### Algorithm
- 递归与非递归
- 排序算法（8种）
- 栈、队列、散列表、二叉树、红黑树
- 动态规划、贪心、平摊分析
- B树、二项堆、斐波那契堆、不相交集合
- 最小生成树Kruskal和Prim，最短路Dijstra和Bellman-Ford
- 最短路Floyd-Warshall和Johnson，最大流Ford-Fulkerson
- 排序网络、矩阵运算、线性规划、多项式与快速傅立叶变换
- 有限数论，字符串匹配Rabin-Karp和KMP
- 计算几何学、NP完全性、近似算法

### Compliers
- 词法分析、自动机、DFA
- 语法分析、语法制导
- 中间代码、AST树、类型检查
- 堆、栈管理，垃圾回收机制
- 目标代码生成、代码优化
- 指令集并行性
- 并行性与局部性优化
- 过程间分析
