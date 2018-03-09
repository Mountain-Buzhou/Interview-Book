# Interview-Questions-Answers

## Abstract
网络上的资源其实已经足够多了，所以在进行搜索的时候需要极大的筛选成本。为了减少这种低效的筛选，我将一些零散的知识整理在一起。  

`Base`这个部分是几个前端知识库的链接，里面的内容比较浅显易懂，但不够深入。**所以不要觉得看完面试题就ok，还需要深入理解各种概念的原理。**

`Collection`来自日常的面试、闲聊和偶尔的突发奇想，主要是觉得比较有趣，所以有做一些记录和分类。  

希望能够有助大家学习前端基础知识。

## Base

我将**最基础**的前端的知识点分为三个部分：
- html+css+js（闭包、作用域、异步、继承）
- 网络、性能、测试、编码
- 自动化、工程化的开发  

这三个划分出来的只是最为基础的内容，学习这部分内容一方面需要对于书面知识的阅读，也需要在项目中加以实践。

**多看书，多实践**，将认识和实践相结合才能深入理解这些概念。  

基础的面试问题题库已经有很多了，个人觉得这个里面的题大概是入门级别的，刚学的时候看看就可以了。
>[中文前端面试大全：qiu-deqing/FE-interview](https://github.com/qiu-deqing/FE-interview)  

这个题库是英文的，相对来说体系更为分明一些，但内容较少，可以作为梳理结构的时候看看。
>[h5bp/Front-end-Developer-Interview-Questions](https://github.com/h5bp/Front-end-Developer-Interview-Questions)

最后这个白皮书里关于非技术的问题值得一读。
>[yangshun/tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook)

---
## Collection

### Intersting

- [浏览器加载白屏是什么原因？](/WhiteScreen.md)
- [千万访问量的项目，前端需要注意些什么？](/DozensOfVisits.md)

---
### Team Management
- [给你一个二十人的新团队，你作为前端负责人你怎样去做？](/Team.md)
- [工程师的阶段是怎样的？不同阶段应该具备怎样的技能？](/Stages.md)
- [我们为什么热爱学习](/Learning.md)

---
### General

- [写一个events，backbone或者jquery，包括on、off、once、trigger](/Events.md)
- [继承（基本概念，划重点）](/Inherit.md)
- [模版引擎](/Template.md)
- [promise以及一些扩展](/Promise.md)
- event loop [视频](https://www.youtube.com/watch?v=8aGhZQkoFbQ&feature=youtu.be), [SPEC](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop-processing-model)
- [异步](https://blog.risingstack.com/writing-a-javascript-framework-execution-timing-beyond-settimeout/ )
- [作用域](http://www.cnblogs.com/TomXu/archive/2012/01/18/2312463.html)

#### Function Program
- [闭包（基本概念，划重点）](/Clojure.md)
- [柯里化（Currying）](/Currying.md)

#### HTTP
- http1.0和http1.1的区别
- http2具体内容
- https具体内容

#### CSS
- BFC，双栏高度对齐

#### Javascript
- [new操作符做了什么](http://blog.csdn.net/aimingoo/article/details/6105048)
- typeof以及类型转换

#### React
- React的生命周期
- React的vdom实现
- React的diff/patch算法原理
- React的组件逻辑和组件库思路
- React的数据流，flux相关
- Redux、Mobx、Rxjs，发布订阅模式、观察者模式
- Redux解决了什么痛点（有什么优点），又有什么缺点
- Redux的中间件有哪些？redux-actions、redux-promise、redux-thunk、redux-saga、redux-immutable了解过哪些？说说差异   

#### HOLE :)
- iframe
- batch
- ast/babel

#### Command
- shell/bash命令
- git命令

#### Product
- 一个feed流，有哪些展现方式？如果当前页面可视区有5个格子，而你有20条信息需要展示，请问有哪些自动展示的算法？
- [移动端的缓存机制有哪几种？](https://segmentfault.com/a/1190000004132566)
- 小程序如何与native通信？react-native实现原理？jsbridge如何实现？
