
## Q: 写一个events，backbone或者jquery，包括on、off、once、trigger

## A: 

`Author: @backbone @yeelan0319 @liyuk @bailnl`

### struct
```js
this._events = {
    change: [callback_on_change1, callback_on_change2, ...],
    ...
}
```

### on
```js
Events.on = function(name, callback, context) {
    if (callback) {
      var handlers = events[name] || (events[name] = []);
      handlers.push({callback: callback, context: context, ctx: context || this});
      }
      return this;
};
```

#### off
```js
Events.off = function(name, callback, context) {
    // 无参数清空所有
    if (!name && !callback && !context) {
        this._events = void 0;
        return this;
    }
    // 有name时，清空name对应
    if (!callback && !context) {
        delete this._events[name];
        continue;
    }
    // 有callback时检查
    var remaining = [];
    if(
        callback && callback !== handler.callback &&
        callback !== handler.callback._callback ||
        context && context !== handler.context
    ){
        //保留回调函数在数组中
    }
}
```

### trigger
```js
//当绑定3个以下回调函数的时候Backbone会做如下优化处理，据说这样是可以提高执行效率的。    
var triggerEvents = function(events, args) {
    var ev, i = -1, l = events.length, a1 = args[0], a2 = args[1], a3 = args[2];
    switch (args.length) {
      case 0: while (++i < l) (ev = events[i]).callback.call(ev.ctx); return;
      case 1: while (++i < l) (ev = events[i]).callback.call(ev.ctx, a1); return;
      case 2: while (++i < l) (ev = events[i]).callback.call(ev.ctx, a1, a2); return;
      case 3: while (++i < l) (ev = events[i]).callback.call(ev.ctx, a1, a2, a3); return;
      default: while (++i < l) (ev = events[i]).callback.apply(ev.ctx, args); return;
    }
};
```

### once
```js
var once = _.once(function(){
    self.off(name, once);
    callback.apply(this, arguments);
});
return this.on(name, once, context);
```

## Roast:
- Events的引入减少了callback的层级调用。
- 解耦，一对多的关系。
这个问题是一个基本概念，但不要因为简单而忽视了这个基本概念。
