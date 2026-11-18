const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#site-nav');
if (toggle && nav) {
  const narrow = window.matchMedia('(max-width: 959px)');
  const label = toggle.querySelector('span');
  const setOpen = (open, restoreFocus = false) => {
    toggle.setAttribute('aria-expanded', String(open));
    label.textContent = open ? 'Close' : 'Menu';
    nav.hidden = narrow.matches && !open;
    nav.classList.toggle('is-open', open);
    if (restoreFocus) toggle.focus();
  };
  const sync = () => {
    if (!narrow.matches && toggle.contains(document.activeElement)) nav.querySelector('a')?.focus();
    toggle.hidden = !narrow.matches;
    setOpen(false);
    if (narrow.matches && nav.contains(document.activeElement)) toggle.focus();
  };
  toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
  nav.addEventListener('click', event => {
    const anchor = event.target.closest('a');
    if (!anchor || !narrow.matches) return;
    setOpen(false);
    if (anchor.hash && anchor.origin === location.origin) {
      const heading = document.querySelector(anchor.hash)?.querySelector('h2');
      if (heading) {
        heading.setAttribute('tabindex', '-1');
        heading.focus({preventScroll: true});
        heading.addEventListener('blur', () => heading.removeAttribute('tabindex'), {once: true});
      }
    }
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') setOpen(false, true);
  });
  narrow.addEventListener('change', sync);
  sync();
}
