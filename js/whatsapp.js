window.WA={
parse:function(s){return(s||'').split(';').filter(Boolean).map(function(p){var a=p.split('=');return{l:a[0].trim(),v:a[1].split('|').map(function(x){return x.trim()})}})},
message:function(o){var L=['Hello '+window.MS.brand+',',''];
if(o.product){L.push('I am interested in the following product:','','Product: '+o.product,'Product Code: '+o.code,'Category: '+o.cat);if(o.image)L.push('','Product Image (tap to view):',o.image,'')}else{L.push('I would like to make an enquiry.','')}
(o.dims||[]).forEach(function(d){L.push(d.l+': '+d.v)});
if(o.price)L.push('Price: Rs. '+o.price);
if(o.qty)L.push('Quantity: '+o.qty);
L.push('','Customer Name: '+o.name);if(o.mobile)L.push('Mobile Number: '+o.mobile);if(o.msg)L.push('Message: '+o.msg);
L.push('',o.product?'Please share more details and your best price.':'Please get in touch with me.','','Thank you.');return L.join('\n')},
url:function(n,t){return'https://wa.me/'+n+'?text='+encodeURIComponent(t)}};
