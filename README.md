# Interview-Questions-Answers

`Author: @liyuk @onion`

## Abstract
网络上的资源其实已经足够多了，所以在进行搜索的时候需要极大的筛选成本。为了减少这种低效的筛选，我将一些零散的知识整理在一起。  

`Entry`这个部分是几个前端知识库的链接，里面的内容比较浅显易懂。先看看整个结构性的题目，找到自己的知识的盲区，再去针对性学习。

`Collection`来自日常的面试、闲聊和偶尔的突发奇想，主要是觉得比较有趣，所以有做一些记录和分类。我和onion讨论了下，决定把这个模块分为三个大的内容，基础、进阶、框架，以及一些我之前整理的问题（与`Entry`有所部分重复）。

`Teamwork`这个部分则是关于团队管理、以及个人非技术上的一些发展相关的杂谈，也有介绍如何学习前端的文章（滑稽）。

`Foundation`这个部分是计算机基础的概念，包括计算机组成原理、操作系统、编译原理、计算机网络、数据结构与算法。这个部分就是所谓的补基础，构建完整的计算机体系结构，是向上成长的过程中必不可少的。    

**欢迎阅读者在issue里留下自己的奇思妙想，或者直接pr。**   

希望能够有助大家学习前端基础知识，以及提高姿势水平，跟大佬谈笑风生。
> 这篇文章并不能帮你提升到大佬的程度，但是可以作为查漏补缺的一个蓝图。

## Entry

我将**最基础**的前端的知识点分为三个部分：
- html+css+js（闭包、作用域、异步、继承）
- 网络、性能、测试、编码
- 自动化、工程化的开发  

这三个划分出来的只是最为基础的内容，学习这部分内容一方面需要对于书面知识的阅读，也需要在项目中加以实践。

基础的面试问题题库已经有很多了，个人觉得这个里面的题大概是入门级别的，刚学的时候看看就可以了。
>[中文前端面试大全：qiu-deqing/FE-interview](https://github.com/qiu-deqing/FE-interview)  

这个题库是英文的，相对来说体系更为分明一些，但内容较少，可以简单看看。
>[h5bp/Front-end-Developer-Interview-Questions](https://github.com/h5bp/Front-end-Developer-Interview-Questions)

白皮书里关于非技术的问题值得一读。
>[yangshun/tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook)

这本书里面梳理的非常全面，可以作为知识体系的梳理来进行学习。
>[front-end-developer-handbook-2018](https://frontendmasters.gitbooks.io/front-end-developer-handbook-2018/)  


---
## Collection

这个模块分为三个部分，即基础`Basic`，进阶`Advanced`，框架`Framework`，这是相当科学的划分。这里的内容主要是我们一起整理，以及日常讨论的一些题目，会有一些重复的内容，也可以独立作为一个基础知识体系。

---
### Basic

- html5新标签有哪些
- canvas、svg
- webGL
- 语义化
- SEO
- cookies、storage（sessionStorage、localStorage）
- IndexedDB、Web SQL
- manifest、worker、socket
- Doctype
- 合模型
- 怪异模式和标准模式
- DNS劫持是什么？
- input和textarea的区别
- 用一个div模拟textarea的实现
- css3有什么新特性，浏览器支持怎么样
- 伪类是什么？有哪些？会有哪些兼容性问题？如何处理？
- css预处理器知道吗？用过哪些？有什么优劣？后处理器知道吗？
- less、sass、postcss、prefix
- 圣杯、双飞燕布局
- float清除浮动
- 层叠优先级
- flex布局、 grid布局、table布局
- 绘制三角形、矩形、菱形、梯形（奇巧淫技，可以不问）
- spirte图（雪碧图）知道吗？使用姿势是怎样的？ svg雪碧图了解吗？
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
- typeof以及类型转换
- 函数是第一公民如何理解？
- dom的节点操作？能够背api还是知道api？
- ajax是什么？知道底层实现原理吗？知道fetch吗？自己封装过吗？
- GET、POST意义？restful架构下还有别的什么请求？
- OPTION请求做了什么？
- 事件冒泡和事件捕获是怎样的？对应的默认方法有什么？一般在什么情况使用？
- call、apply、bind
- 如何判断数据类型
- hoisting是什么？具体表现是怎样的？
- 匿名函数是什么？
- 函数表达式和函数声明的区别
- let、const暂时性锁区知道吗？表现是怎样的？
- 严格模式是什么？有什么好处？'use strict'
- arguments是什么类型？callee和caller有什么区别？
- 正则表达式
- 内存泄漏
- 垃圾回收机制
- Date.format实现过吗？思路是怎样的？
- 动画：setTimeout何时执行，requestAnimationFrame的优点
- parseQuery
- flatten
- require.js的实现原理

---
### Advanced

我们会尽可能地增加`Advanced`(进阶)这里面的题目的数量和难度，当然也包含很多基础知识点的详细内容。这里的知识点的区分暂时并不是特别明显，之后onion来整理这块儿内容。

#### Browser

- [打开一个网页经历了那些过程？](https://github.com/qiu-deqing/FE-interview#从浏览器地址栏输入url到显示页面的步骤以http为例)
- [浏览器加载白屏是什么原因？](/WhiteScreen.md)
- [千万访问量的项目，前端需要注意些什么？](/DozensOfVisits.md)

#### General

- [写一个events，backbone或者jquery，包括on、off、once、trigger](/Events.md)
- [继承（重点）](/Inherit.md)
- [模版引擎](/Template.md)
- [promise以及一些扩展](/Promise.md)
- event loop [视频](https://www.youtube.com/watch?v=8aGhZQkoFbQ&feature=youtu.be), [SPEC](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop-processing-model)
- [异步（重点）](https://blog.risingstack.com/writing-a-javascript-framework-execution-timing-beyond-settimeout/ )
- [作用域（重点）](http://www.cnblogs.com/TomXu/archive/2012/01/18/2312463.html)
- [new操作符做了什么](http://blog.csdn.net/aimingoo/article/details/6105048)
- [js模块化现状？AMD和CMD是什么？](https://segmentfault.com/a/1190000009591055)

#### Function Program
- [闭包（重点）](/Clojure.md)
- [柯里化（Currying）](/Currying.md)

#### HTTP
- http1.0和http1.1的区别
- http请求码有哪些？301、302、303、304、307
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
- gzip、chunck
- 前端安全：xss攻击和防范、CSRF、CORS
- 硬件加速怎样开启
- 优化中会提到缓存的问题，问：静态资源或者接口等如何做缓存优化
- 页面DOM节点太多，会出现什么问题？如何优化？

#### Product
- 一个feed流，有哪些展现方式？如果当前页面可视区有5个格子，而你有20条信息需要展示，请问有哪些自动展示的算法？
- [移动端的缓存机制有哪几种？](https://segmentfault.com/a/1190000004132566)
- 小程序如何与native通信？react-native实现原理？jsbridge如何实现？
- 过万条数据如何加载和渲染？

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
- Vue双向数据绑定的实现

#### Angular
- Angular双向绑定原理
- Angular的一些基础概念描述下
- Angular的factory和service有什么联系
- Angular的指令怎么写？compile和link有什么区别
- 脏值检查是什么？
- 隐式注入
- 作用域冲突  
- angularjs(1.x)和angular(2.x)的区别

---
## Team Management
- [给你一个二十人的新团队，你作为前端负责人你怎样去做？](/Team.md)
- [工程师的阶段是怎样的？不同阶段应该具备怎样的技能？](/Stages.md)
- [我们为什么热爱学习](/Learning.md)

---
## Foundation
补课大讲堂
#### Operating System
- 进程与线程
- 虚拟地址，物理地址
- 进程间通信：临界区、忙等待互斥、睡眠与唤醒、信号量、互斥量、管程、消息传递、屏障、避免锁
- 进程调度策略：批处理、交互式、实时；
- 批处理调度：FCFS、SJF、SRTN
- 交互式调度：轮转、优先级、多几队列、最短进程优先、保证调度、彩票调度、公平分享调度
- 实时调度：硬实时、软实时、周期性
- [IPC问题：读者-写者、生产者-消费者、哲学家进餐、银行家算法](https://www.zybuluo.com/zhengbuqian/note/243560)
- 页面置换算法：最优页面置换算法、最近未使用页面置换算法（NRU）、先进先出页面置换算法（FIFO）、第二次机会页面置换算法、时钟页面置换算法（clock）、最近最少使用页面置换算法（LRU）、软件模拟LRU、工作集页面置换算法、工作集时钟页面置换算法

#### Computer Organization
- 缺页中断——FIFO、LRU、OPT这三种置换算法
- 流水线、指令集

#### Network
- [帧、报文、报文段、分组、包、数据报的概念](http://www.cnblogs.com/sddai/p/5649939.html)
- DNS原理
- udp和tcp
- 可靠性数据传输原理、拥塞控制原理
- 路由选择：rip和ospf
- 计算机网络安全

#### Algorithm
- hash table
- 图：dijstra、dfs、bfs
- 树：二叉树、三叉树、平衡树、红黑树，B＋树
- kmp
- 堆、栈、队列的相互实现
- 排序算法（8种）
- 递归、非递归、动态规划

#### Compliers
- 词法分析、自动机、DFA
- 语法分析、语法制导
- 中间代码、AST树、类型检查
- 堆、栈管理，垃圾回收机制
- 目标代码生成、代码优化
- 指令集并行性
- 并行性与局部性优化
- 过程间分析
