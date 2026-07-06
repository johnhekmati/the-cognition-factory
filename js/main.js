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
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('[data-nav]');

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

/* ── Contact form (placeholder — wire to your backend or Formspree) ── */
function initContactForm() {
  const form = document.getElementById('contact-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    /*
     * ASSET PLACEHOLDER: Connect form submission
     * Options:
     *   1. Formspree — action="https://formspree.io/f/YOUR_ID"
     *   2. Cloudflare Workers endpoint
     *   3. Custom API at api.thecognitionfactory.com
     */
    const btn = form.querySelector('[type="submit"]');
    const originalText = btn.textContent;
    btn.textContent = 'Message Sent';
    btn.disabled = true;

    setTimeout(() => {
      btn.textContent = originalText;
      btn.disabled = false;
      form.reset();
    }, 3000);
  });
}

/* ── Hero video slide transition (HAL-E ↔ AAE), Gravatar-style ── */
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

/* ── Section video banners — play when in view ── */
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

/* ── Scroll-reveal for cards and sections ── */
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