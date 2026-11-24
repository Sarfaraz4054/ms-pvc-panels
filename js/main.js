(function(){var $=function(s,r){return(r||document).querySelector(s)},$$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
var b=$('.burger'),nav=$('.nav');b.onclick=function(){var o=nav.classList.toggle('open');b.setAttribute('aria-expanded',o)};
$$('select[name=to]').forEach(function(s){s.innerHTML=MS.numbers.map(function(n){return'<option value="'+n.n+'">'+n.label+'</option>'}).join('')});
$$('.card[data-dims]').forEach(function(c){var u=$('.specs',c);if(u)u.innerHTML=WA.parse(c.dataset.dims).map(function(d){return'<li><b>'+(d.l==='Size'?'Available Sizes':d.l)+':</b> '+d.v.join(' &amp; ')+'</li>'}).join('')});
var dlg=$('#enq'),f=$('#enq-form'),cur;
$$('.enq-btn').forEach(function(btn){btn.onclick=function(){var c=btn.closest('.card');var ci=$('img',c).src;cur={prices:c.dataset.prices||'',product:c.dataset.name,code:c.dataset.code,cat:c.dataset.cat,dims:WA.parse(c.dataset.dims),image:/^https?:/.test(ci)&&!/placeholder\.svg/.test(ci)?ci:''};
$('#enq-title').textContent=cur.product;$('#enq-meta').textContent=cur.code+' | '+cur.cat;var im=$('#enq-img');im.src=$('img',c).src;im.alt=cur.product;
$('#enq-opts').innerHTML=cur.dims.map(function(d,i){return d.v.length>1?'<label>'+d.l+'<select data-i="'+i+'">'+d.v.map(function(v){return'<option>'+v+'</option>'}).join('')+'</select></label>':''}).join('');
dlg.showModal()}});
$('.x',dlg).onclick=function(){dlg.close()};dlg.addEventListener('click',function(e){if(e.target===dlg)dlg.close()});
function go(form,extra){var d=new FormData(form),o=Object.assign({name:d.get('name'),mobile:d.get('mobile'),qty:d.get('qty'),msg:d.get('msg')},extra||{});
window.open(WA.url(d.get('to'),WA.message(o)),'_blank','noopener')}
f.onsubmit=function(e){e.preventDefault();var dims=cur.dims.map(function(d,i){var s=$('[data-i="'+i+'"]',f);return{l:d.l,v:s?s.value:d.v[0]}});var pm={};cur.prices.split('|').forEach(function(x){var a=x.split('=');if(a[1])pm[a[0]]=a[1]});var sz=dims.filter(function(d){return d.l==='Size'})[0];go(f,{product:cur.product,code:cur.code,cat:cur.cat,dims:dims,image:cur.image,price:pm.all||(sz&&pm[sz.v])||''});dlg.close()};
var cf=$('#contact-form');if(cf)cf.onsubmit=function(e){e.preventDefault();go(cf)};
})();
