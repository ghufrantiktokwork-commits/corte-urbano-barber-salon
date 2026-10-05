const b=document.querySelector('.menu'),u=document.querySelector('nav ul');
b.addEventListener('click',()=>{const o=u.classList.toggle('open');b.setAttribute('aria-expanded',o)});
const d=new Date().getDay(),r=document.querySelectorAll('tr[data-d]');r.forEach(t=>{if(+t.dataset.d===d)t.classList.add('today')});
