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

const areaSearch = document.querySelector('#area-search');
if (areaSearch) {
  const panel = areaSearch.closest('.area-search');
  const rows = [...document.querySelectorAll('[data-place]')];
  const bands = [...document.querySelectorAll('.area-band')];
  const count = document.querySelector('#area-count');
  const filterAreas = () => {
    const query = areaSearch.value.trim().toLocaleLowerCase('en-GB');
    rows.forEach(row => { row.hidden = !row.dataset.place.includes(query); });
    bands.forEach(band => {
      band.hidden = ![...band.querySelectorAll('[data-place]')].some(row => !row.hidden);
      band.open = Boolean(query) && !band.hidden;
    });
    const matches = rows.filter(row => !row.hidden).length;
    count.textContent = matches ? `${matches} nearby ${matches === 1 ? 'place' : 'places'}${query ? ' found.' : ' in the directory. Expand a distance group or search by name.'}` : 'No matching place in this directory. Ask Macy if you need help planning your visit.';
  };
  panel.hidden = false;
  areaSearch.addEventListener('input', filterAreas);
  filterAreas();
}
