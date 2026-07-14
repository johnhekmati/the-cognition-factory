/**
 * The Cognition Factory — Main interactions
 */

document.addEventListener('DOMContentLoaded', () => {
  initNavigation();
  initScrollSpy();
  initMobileMenu();
  initContactForm();
  initRevealAnimations();
  initHeroVideos();
  initSectionVideos();
  initContextVideo();
  initResourceFilters();
});

/* ── Sticky nav background on scroll ── */
function initNavigation() {
  const nav = document.getElementById('main-nav');
  if (!nav) return;

  const toggleNavState = () => {
    nav.classList.toggle('nav-scrolled', window.scrollY > 40);
  };

  toggleNavState();
  window.addEventListener('scroll', toggleNavState, { passive: true });
}

/* ── Active section highlighting ── */
function initScrollSpy() {
  const navLinks = document.querySelectorAll('[data-nav]');
  const navIds = new Set(
    [...navLinks]
      .map((link) => link.getAttribute('href'))
      .filter((href) => href && href.startsWith('#'))
      .map((href) => href.slice(1))
  );

  const sections = [...document.querySelectorAll('section[id]')].filter((s) =>
    navIds.has(s.id)
  );

  if (!sections.length || !navLinks.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const id = entry.target.id;
        navLinks.forEach((link) => {
          link.classList.toggle('active', link.getAttribute('href') === `#${id}`);
        });
      });
    },
    { rootMargin: '-40% 0px -55% 0px', threshold: 0 }
  );

  sections.forEach((section) => observer.observe(section));
}

/* ── Mobile menu toggle ── */
function initMobileMenu() {
  const toggle = document.getElementById('menu-toggle');
  const menu = document.getElementById('mobile-menu');
  const iconOpen = document.getElementById('icon-open');
  const iconClose = document.getElementById('icon-close');

  if (!toggle || !menu) return;

  const closeMenu = () => {
    menu.classList.add('hidden');
    toggle.setAttribute('aria-expanded', 'false');
    iconOpen?.classList.remove('hidden');
    iconClose?.classList.add('hidden');
    document.body.style.overflow = '';
  };

  const openMenu = () => {
    menu.classList.remove('hidden');
    toggle.setAttribute('aria-expanded', 'true');
    iconOpen?.classList.add('hidden');
    iconClose?.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
  };

  toggle.addEventListener('click', () => {
    const isOpen = toggle.getAttribute('aria-expanded') === 'true';
    isOpen ? closeMenu() : openMenu();
  });

  menu.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', closeMenu);
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeMenu();
  });
}

/* ── Contact form ── */
function initContactForm() {
  const form = document.getElementById('contact-form');
  if (!form) return;

  const statusEl = document.getElementById('form-status');
  const btn = form.querySelector('[type="submit"]');

  const showStatus = (ok, message) => {
    if (!statusEl) return;
    statusEl.classList.remove('hidden');
    statusEl.textContent = message;
    statusEl.className = ok
      ? 'text-sm rounded-lg px-4 py-3 border border-electric/30 bg-electric/10 text-electric'
      : 'text-sm rounded-lg px-4 py-3 border border-red-500/30 bg-red-500/10 text-red-300';
  };

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const originalText = btn.textContent;
    btn.textContent = 'Sending...';
    btn.disabled = true;
    if (statusEl) statusEl.classList.add('hidden');

    try {
      const formData = new FormData(form);

      const res = await fetch('/api/contact', {
        method: 'POST',
        body: formData,
      });

      const result = await res.json().catch(() => ({}));

      if (res.ok && result.success) {
        btn.textContent = 'Message sent';
        form.reset();
        showStatus(true, 'Message sent. We will respond if the inquiry is a fit.');
      } else {
        const msg =
          result.error ||
          'Failed to send. Email contact@thecognitionfactory.com directly.';
        console.error('Contact form error:', msg);
        btn.textContent = 'Error — try again';
        showStatus(false, msg);
      }
    } catch (err) {
      console.error('Contact form network error:', err);
      btn.textContent = 'Error — try again';
      showStatus(
        false,
        'Network error. Email contact@thecognitionfactory.com directly.'
      );
    }

    setTimeout(() => {
      btn.textContent = originalText;
      btn.disabled = false;
    }, 3500);
  });
}

/* ── Resource filters ── */
function initResourceFilters() {
  const buttons = document.querySelectorAll('.resource-filter');
  const cards = document.querySelectorAll('.resource-card');
  if (!buttons.length || !cards.length) return;

  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      const filter = button.dataset.filter || 'all';

      buttons.forEach((b) => {
        const active = b === button;
        b.classList.toggle('is-active', active);
        b.setAttribute('aria-pressed', active ? 'true' : 'false');
      });

      cards.forEach((card) => {
        const category = card.dataset.category || '';
        const show = filter === 'all' || category === filter;
        card.classList.toggle('is-hidden', !show);
      });
    });
  });
}

/* ── Hero video slide transition (HAL-E ↔ AAE) ── */
function initHeroVideos() {
  const videos = [...document.querySelectorAll('[data-hero-video]')];
  const labelEl = document.getElementById('hero-engine-label');
  if (videos.length < 2) return;

  const LABELS = {
    'HAL-E': 'Hyper Accelerated Learning Engine',
    AAE: 'Adaptive Assessment Engine',
  };

  const setLabel = (video) => {
    if (!labelEl) return;
    const key = video.dataset.heroLabel;
    labelEl.textContent = LABELS[key] || key || labelEl.textContent;
  };

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    videos[0].classList.add('is-active');
    videos[0].play().catch(() => {});
    setLabel(videos[0]);
    return;
  }

  let current = 0;
  let transitioning = false;
  const INTERVAL_MS = 8000;
  const TRANSITION_MS = 1400;

  const playVideo = (video) => {
    video.currentTime = 0;
    return video.play().catch(() => {});
  };

  playVideo(videos[0]);
  setLabel(videos[0]);

  const slideToNext = () => {
    if (transitioning) return;
    transitioning = true;

    const outgoing = videos[current];
    const incoming = videos[(current + 1) % videos.length];

    outgoing.classList.remove('is-active');
    outgoing.classList.add('is-exiting');

    incoming.classList.add('is-active');
    playVideo(incoming);
    setLabel(incoming);

    setTimeout(() => {
      outgoing.classList.remove('is-exiting');
      outgoing.pause();
      current = (current + 1) % videos.length;
      transitioning = false;
    }, TRANSITION_MS);
  };

  setInterval(slideToNext, INTERVAL_MS);
}

/* ── Section videos — play when in view ── */
function initSectionVideos() {
  const videos = document.querySelectorAll('[data-section-video]');
  if (!videos.length) return;

  const playVideo = (video) => video.play().catch(() => {});
  const pauseVideo = (video) => {
    video.pause();
    video.currentTime = 0;
  };

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    videos.forEach((video) => {
      video.removeAttribute('autoplay');
      pauseVideo(video);
    });
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        const video = entry.target;
        entry.isIntersecting ? playVideo(video) : pauseVideo(video);
      });
    },
    { threshold: 0.35 }
  );

  videos.forEach((video) => {
    pauseVideo(video);
    observer.observe(video);
  });
}

/* ── Context portrait ── */
function initContextVideo() {
  const video = document.querySelector('[data-context-video]');
  if (!video) return;

  const playVideo = () => video.play().catch(() => {});

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    video.removeAttribute('autoplay');
    video.pause();
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        entry.isIntersecting ? playVideo() : video.pause();
      });
    },
    { threshold: 0.2 }
  );

  observer.observe(video);
  if (video.getBoundingClientRect().top < window.innerHeight) playVideo();
}

/* ── Scroll-reveal ── */
function initRevealAnimations() {
  const targets = document.querySelectorAll('[data-reveal]');

  if (!targets.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
  );

  targets.forEach((el) => observer.observe(el));
}
