(window.webpackJsonp=window.webpackJsonp||[]).push([[2],{175:function(t,n,e){var content=e(177);"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);(0,e(38).default)("2e1a6cac",content,!0,{sourceMap:!1})},176:function(t,n,e){"use strict";var r=e(175);e.n(r).a},177:function(t,n,e){(t.exports=e(37)(!1)).push([t.i,".input[data-v-320a3212]{width:500px;margin-bottom:20px}input[data-v-320a3212]{display:inline}.output-list[data-v-320a3212]{display:inline-block;width:500px}",""])},178:function(t,n,e){"use strict";e.r(n);e(12);var r={name:"HomePage",data:function(){return{start:"",words:[],thinking:!1,hasError:!1}},methods:{triggerGetWords:function(t){13===t.keyCode&&this.getWords()},getWords:function(){var t=this;this.thinking||(this.words=[],this.hasError=!1,this.start&&(this.thinking=!0,this.$axios.get("word-from/"+this.start).then((function(n){for(var e=function(i){var e=(0===i?"":"→ ")+n.data.words[i];setTimeout((function(){return t.words.push(e)}),500*i)},i=0;i<n.data.words.length;i++)e(i)})).catch((function(){t.hasError=!0})).finally((function(){t.thinking=!1}))))}}},o=(e(176),e(23)),component=Object(o.a)(r,(function(){var t=this,n=t.$createElement,e=t._self._c||n;return e("div",[e("section",{staticClass:"section has-text-centered"},[e("div",[e("input",{directives:[{name:"model",rawName:"v-model",value:t.start,expression:"start"}],staticClass:"input is-large",attrs:{type:"text",placeholder:"何から始めますか？",autofocus:""},domProps:{value:t.start},on:{keydown:function(n){return!n.type.indexOf("key")&&t._k(n.keyCode,"enter",13,n.key,"Enter")?null:t.triggerGetWords(n)},input:function(n){n.target.composing||(t.start=n.target.value)}}})]),t._v(" "),e("div",[e("button",{staticClass:"button is-info is-large",class:{"is-loading":t.thinking},on:{click:t.getWords}},[t._v("\n        スタート\n      ")])]),t._v(" "),e("div",[e("transition-group",{staticClass:"output-list has-text-left",attrs:{name:"custom-classes-transition","enter-active-class":"animated fadeInLeft",tag:"ul"}},t._l(t.words,(function(n){return e("li",{key:n},[e("span",{staticClass:"is-size-3"},[t._v(t._s(n))])])})),0),t._v(" "),e("transition",{attrs:{"enter-active-class":"animated fadeIn"}},[t.hasError?e("p",{staticClass:"is-size-5"},[t._v("\n          うーん、そんな単語は聞いたことがないですね。\n        ")]):t._e()])],1)])])}),[],!1,null,"320a3212",null);n.default=component.exports}}]);