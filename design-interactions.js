/* Native progressive enhancement. Reading-progress principle: Magic UI Scroll Progress (MIT).
   Independent implementation; no framework or copied template code. */
(() => {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  document.querySelectorAll('[data-work-switcher]').forEach(switcher => {
    const buttons = [...switcher.querySelectorAll('[data-preview]')];
    buttons.forEach(button => button.addEventListener('click', () => {
      buttons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
      switcher.querySelectorAll('[data-panel]').forEach(panel => {
        panel.hidden = panel.dataset.panel !== button.dataset.preview;
      });
    }));
  });
  const progress = document.querySelector('.reading-progress');
  if (progress) {
    let pending = false;
    const update = () => {
      const range = document.documentElement.scrollHeight - window.innerHeight;
      progress.style.transform = `scaleX(${range > 0 ? Math.min(1, window.scrollY / range) : 0})`;
      pending = false;
    };
    window.addEventListener('scroll', () => {
      if (!pending) { pending = true; window.requestAnimationFrame(update); }
    }, {passive:true});
    window.addEventListener('resize', update);
    update();
  }
  const toc = document.querySelector('.case-toc');
  if (toc && 'IntersectionObserver' in window) {
    const links = [...toc.querySelectorAll('a[href^="#"]')];
    const observer = new IntersectionObserver(entries => {
      const entered = entries.filter(e => e.isIntersecting).sort((a,b) => a.boundingClientRect.top-b.boundingClientRect.top);
      if (!entered.length) return;
      links.forEach(link => {
        if (link.hash === '#' + entered[0].target.id) link.setAttribute('aria-current','location');
        else link.removeAttribute('aria-current');
      });
    }, {rootMargin:'-15% 0px -65% 0px'});
    links.forEach(link => { const target=document.getElementById(link.hash.slice(1)); if(target)observer.observe(target); });
  }
  document.documentElement.classList.toggle('reduce-motion', reduced.matches);
  reduced.addEventListener('change', e => document.documentElement.classList.toggle('reduce-motion',e.matches));
})();
