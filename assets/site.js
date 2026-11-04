(() => {
  // menu
  const btn = document.querySelector('.menu-btn'), nav = document.getElementById('nav');
  if (btn && nav) {
    const set = o => { nav.classList.toggle('open', o); btn.setAttribute('aria-expanded', o); btn.textContent = o ? 'Close' : 'Menu'; document.body.classList.toggle('menu-open', o); };
    btn.addEventListener('click', () => set(!nav.classList.contains('open')));
    nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => set(false)));
    addEventListener('keydown', e => { if (e.key === 'Escape' && nav.classList.contains('open')) { set(false); btn.focus(); } });
  }

  const still = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // hero video
  const film = document.getElementById('film'), pause = document.getElementById('pause');
  if (film) {
    const sync = () => { if (!pause) return; pause.textContent = film.paused ? 'Play' : 'Pause'; pause.setAttribute('aria-label', film.paused ? 'Play background video' : 'Pause background video'); };
    film.addEventListener('play', sync); film.addEventListener('pause', sync);
    if (pause) pause.addEventListener('click', () => film.paused ? film.play().catch(() => {}) : film.pause());
    if (!still) { film.muted = true; film.play().catch(() => {}); } else { sync(); }
  }
  // other looping clips respect reduced motion
  if (still) document.querySelectorAll('video[autoplay]').forEach(v => { v.removeAttribute('autoplay'); v.pause(); });

  // reveal
  const els = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window && !still) {
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: .08, rootMargin: '0px 0px -40px 0px' });
    els.forEach(el => io.observe(el));
  } else els.forEach(el => el.classList.add('in'));

  // prefill interest from ?interest=
  const sel = document.getElementById('interest');
  if (sel) {
    const q = new URLSearchParams(location.search).get('interest');
    if (q === 'support') sel.value = 'Support';
    if (q === 'collaborate') sel.value = 'Collaboration';
  }

  // forms (Netlify)
  document.querySelectorAll('form.js-form').forEach(form => form.addEventListener('submit', e => {
    e.preventDefault();
    const b = form.querySelector('button[type=submit]'), n = form.querySelector('.note');
    b.disabled = true; n.textContent = 'Sending…';
    fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams(new FormData(form)).toString() })
      .then(r => { if (!r.ok) throw 0; form.reset(); n.textContent = form.dataset.ok; })
      .catch(() => { n.textContent = 'Something went wrong. Please write to hello@togetherworx.org.'; })
      .finally(() => { b.disabled = false; });
  }));
})();
