(window.webpackJsonp=window.webpackJsonp||[]).push([[2],{301:function(t,r,e){var content=e(303);"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);(0,e(11).default)("4ab117c6",content,!0,{sourceMap:!1})},302:function(t,r,e){"use strict";var c=e(301);e.n(c).a},303:function(t,r,e){(r=e(10)(!1)).push([t.i,".recipe-card{box-shadow:0 1rem 1.5rem rgba(0,0,0,.6);padding:5px;background-color:#4e667b}.router-link{text-decoration:none!important;font-size:12px}.gold-text{color:gold}",""]),t.exports=r},304:function(t,r,e){"use strict";e.r(r);e(72);var c=e(26),n={props:["product","onDelete"]},o=(e(302),e(53)),l={components:{ProductCard:Object(o.a)(n,(function(){var t=this,r=t.$createElement,e=t._self._c||r;return e("div",{staticClass:"card recipe-card text-center"},[e("img",{staticClass:"card-img-top",attrs:{height:"150px",src:t.product.image_url}}),t._v(" "),e("div",{staticClass:"card-body"},[e("h5",{staticClass:"card-title"},[t._v(t._s(t.product.item_name))]),t._v(" "),e("h5",{staticClass:"card-title"},[t._v("စျေးနှုန်း : "+t._s(t.product.sell_price_per_item))]),t._v(" "),e("p",{staticClass:"card-text"}),t._v(" "),e("nuxt-link",{staticClass:"router-link",attrs:{to:"/products/"+t.product.id+"/"}},[e("p",{staticClass:"gold-text"},[t._v("\n        အသေးစိတ်ကြည့်မယ်\n      ")])])],1)])}),[],!1,null,null,null).exports},data:function(){return{products:[]}},asyncData:function(t){return Object(c.a)(regeneratorRuntime.mark((function r(){var e,c,n;return regeneratorRuntime.wrap((function(r){for(;;)switch(r.prev=r.next){case 0:return e=t.$axios,t.params,r.prev=1,r.next=4,e.$get("/products/product_list/");case 4:return c=r.sent,n=c,r.abrupt("return",{products:n});case 9:return r.prev=9,r.t0=r.catch(1),r.abrupt("return",{products:[]});case 12:case"end":return r.stop()}}),r,null,[[1,9]])})))()}},d=Object(o.a)(l,(function(){var t=this.$createElement,r=this._self._c||t;return r("main",{staticClass:"container mt-5"},[r("div",{staticClass:"row"},[this._l(this.products,(function(t){return[r("div",{key:t.id,staticClass:"col-lg-3 col-md-4 col-sm-6 mb-4"},[r("product-card",{attrs:{product:t}})],1)]}))],2)])}),[],!1,null,null,null);r.default=d.exports}}]);