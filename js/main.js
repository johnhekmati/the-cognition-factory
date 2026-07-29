/**
 * The Cognition Factory — Main interactions
 */

document.addEventListener('DOMContentLoaded', () => {
  initNavigation();
  initScrollSpy();
  initMobileMenu();
  initContactForm();
  initPartnerPacketForm();
  initRevealAnimations();
  initHeroSlides();
  initHeroVideos();
  initSectionVideos();
  initContextVideo();
  initResourceFilters();
  initProductLightbox();
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

/* ── Shared POST to /api/contact (Web3Forms via Pages Function) ── */
async function submitContactForm(
  form,
  { statusEl, btn, successMessage, statusTone = 'default' }
) {
  if (btn?.dataset.busy === '1') return;
  const originalText = btn?.textContent || 'Send';
  if (btn) {
    btn.dataset.busy = '1';
    btn.textContent = 'Sending...';
    btn.disabled = true;
    btn.setAttribute('aria-busy', 'true');
  }
  if (statusEl) {
    statusEl.classList.add('hidden');
  }

  const okClass =
    statusTone === 'compact'
      ? 'text-xs rounded-lg px-3 py-2 border border-electric/30 bg-electric/10 text-electric'
      : 'text-sm rounded-lg px-4 py-3 border border-electric/30 bg-electric/10 text-electric';
  const errClass =
    statusTone === 'compact'
      ? 'text-xs rounded-lg px-3 py-2 border border-red-500/30 bg-red-500/10 text-red-300'
      : 'text-sm rounded-lg px-4 py-3 border border-red-500/30 bg-red-500/10 text-red-300';

  const showStatus = (ok, message) => {
    if (!statusEl) return;
    statusEl.classList.remove('hidden');
    statusEl.textContent = message;
    statusEl.className = ok ? okClass : errClass;
  };

  try {
    const formData = new FormData(form);
    const res = await fetch('/api/contact', {
      method: 'POST',
      body: formData,
    });
    const result = await res.json().catch(() => ({}));

    if (res.ok && result.success) {
      if (btn) btn.textContent = 'Request sent';
      form.reset();
      // Restore hidden defaults after reset (partner form interest field)
      const interest = form.querySelector('input[name="interest"][type="hidden"]');
      if (interest && interest.dataset.defaultValue) {
        interest.value = interest.dataset.defaultValue;
      }
      showStatus(true, successMessage);
    } else {
      const msg =
        result.error ||
        'Failed to send. Email contact@thecognitionfactory.com directly.';
      console.error('Contact form error:', msg);
      if (btn) btn.textContent = 'Error — try again';
      showStatus(false, msg);
    }
  } catch (err) {
    console.error('Contact form network error:', err);
    if (btn) btn.textContent = 'Error — try again';
    showStatus(
      false,
      'Network error. Email contact@thecognitionfactory.com directly.'
    );
  } finally {
    // Re-enable only after the request settles (no fixed 3.5s race)
    if (btn) {
      setTimeout(() => {
        btn.textContent = originalText;
        btn.disabled = false;
        btn.dataset.busy = '0';
        btn.removeAttribute('aria-busy');
      }, 1200);
    }
  }
}

/* ── Contact form ── */
function initContactForm() {
  const form = document.getElementById('contact-form');
  if (!form) return;

  const statusEl = document.getElementById('form-status');
  const btn = form.querySelector('[type="submit"]');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    await submitContactForm(form, {
      statusEl,
      btn,
      successMessage: 'Message sent. We will respond if the inquiry is a fit.',
    });
  });
}

/* ── Partner packet request (Guides card → same Web3Forms pipeline) ── */
function initPartnerPacketForm() {
  const form = document.getElementById('partner-packet-form');
  if (!form) return;

  const interest = form.querySelector('input[name="interest"]');
  if (interest) {
    interest.dataset.defaultValue = interest.value || 'partner-packet';
  }

  const statusEl = document.getElementById('partner-packet-status');
  const btn = form.querySelector('[type="submit"]');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    await submitContactForm(form, {
      statusEl,
      btn,
      successMessage:
        'Request sent. If it is a fit, we will share the packet out of band.',
      statusTone: 'compact',
    });
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

/* ── Hero audience slides: 24s loop (equal time per slide), crossfade ── */
function initHeroSlides() {
  const stage = document.querySelector('[data-hero-slides]');
  if (!stage) return;

  const slides = [...stage.querySelectorAll('[data-hero-slide]')];
  const dots = [...stage.querySelectorAll('[data-hero-dot]')];
  if (slides.length < 2) return;

  const loopMs = Math.max(
    3000,
    parseInt(stage.getAttribute('data-hero-loop-ms') || '24000', 10) || 24000
  );
  const dwellMs = Math.floor(loopMs / slides.length);
  let index = Math.max(
    0,
    slides.findIndex((s) => s.classList.contains('is-active'))
  );
  if (index < 0) index = 0;

  let timer = null;
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const show = (next) => {
    index = ((next % slides.length) + slides.length) % slides.length;
    slides.forEach((slide, i) => {
      const on = i === index;
      slide.classList.toggle('is-active', on);
      slide.setAttribute('aria-hidden', on ? 'false' : 'true');
    });
    dots.forEach((dot, i) => {
      const on = i === index;
      dot.classList.toggle('is-active', on);
      dot.setAttribute('aria-selected', on ? 'true' : 'false');
    });
  };

  const stop = () => {
    if (timer != null) {
      window.clearInterval(timer);
      timer = null;
    }
  };

  const start = () => {
    stop();
    if (reduceMotion) return;
    timer = window.setInterval(() => show(index + 1), dwellMs);
  };

  show(index);

  dots.forEach((dot) => {
    dot.addEventListener('click', () => {
      const i = parseInt(dot.getAttribute('data-hero-dot') || '0', 10);
      show(i);
      start();
    });
  });

  // Pause while tab is hidden; resume on return
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) stop();
    else start();
  });

  if (!reduceMotion) start();
}

/* ── Hero banner: one-shot spinner, dual-tone glow always on, click to replay ── */
function initHeroVideos() {
  const videos = [...document.querySelectorAll('[data-hero-video]')];
  const bannerImg = document.querySelector('[data-hero-banner]');
  const labelEl = document.getElementById('hero-engine-label');
  const wrap = document.getElementById('hero-video-wrap');

  if (labelEl) {
    labelEl.textContent = 'The Cognition Factory';
  }

  // Static-only fallback (no <video> in DOM)
  if (bannerImg && wrap) {
    bannerImg.classList.add('is-active');
    wrap.classList.add('is-landed');
    const syncImgAspect = () => {
      const w = bannerImg.naturalWidth;
      const h = bannerImg.naturalHeight;
      if (w > 0 && h > 0) {
        wrap.style.setProperty('--hero-ar', `${w} / ${h}`);
      }
    };
    if (bannerImg.complete) syncImgAspect();
    else bannerImg.addEventListener('load', syncImgAspect);
  }

  if (!videos.length) return;

  const video = videos[0];
  video.classList.add('is-active');
  video.loop = false;
  video.muted = true;
  video.playsInline = true;

  const syncHeroAspect = () => {
    if (!wrap) return;
    const w = video.videoWidth;
    const h = video.videoHeight;
    if (w > 0 && h > 0) {
      wrap.style.setProperty('--hero-ar', `${w} / ${h}`);
    }
  };
  video.addEventListener('loadedmetadata', syncHeroAspect);
  if (video.readyState >= 1) syncHeroAspect();

  // Single hero clip — play once, hold final frame; click quietly replays
  if (videos.length < 2) {
    let landed = false;

    const setLanded = (on) => {
      landed = on;
      if (!wrap) return;
      wrap.classList.toggle('is-landed', on);
      // Subtle a11y hint only when replay is available (no visible chrome)
      if (on) {
        wrap.setAttribute('role', 'button');
        wrap.setAttribute('tabindex', '0');
        wrap.setAttribute(
          'aria-label',
          'The Cognition Factory — click or press Enter to play again'
        );
      } else {
        wrap.removeAttribute('role');
        wrap.removeAttribute('tabindex');
        wrap.setAttribute('aria-label', 'The Cognition Factory');
      }
    };

    const playOnce = () => {
      setLanded(false);
      video.currentTime = 0;
      video.playbackRate = 1;
      return video.play().catch(() => {
        // Autoplay blocked → hold poster / first frame
        setLanded(true);
      });
    };

    const land = () => {
      video.pause();
      // Hold last frame
      if (Number.isFinite(video.duration) && video.duration > 0) {
        try {
          video.currentTime = Math.max(video.duration - 0.05, 0);
        } catch (_) {
          /* ignore seek race */
        }
      }
      setLanded(true);
    };

    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      video.pause();
      video.removeAttribute('autoplay');
      setLanded(true);
      return;
    }

    video.addEventListener('ended', land);

    const tryReplay = () => {
      if (!landed) return;
      playOnce();
    };

    if (wrap) {
      wrap.addEventListener('click', tryReplay);
      wrap.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          tryReplay();
        }
      });
    }

    // Start (autoplay attr + explicit play for reliability)
    playOnce();
    return;
  }

  // Legacy multi-video path (unused when only one hero asset is present)
  const LABELS = {
    TCF: 'The Cognition Factory',
    'HAL-E': 'HAL-E · Deep Learning — build the map',
    AAE: 'AAE · Practice — check what you know',
  };

  const setLabel = (v) => {
    if (!labelEl) return;
    const key = v.dataset.heroLabel;
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

  const playVideo = (v) => {
    v.currentTime = 0;
    return v.play().catch(() => {});
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

/* ── Product gallery lightbox (full-res screenshots) ── */
function initProductLightbox() {
  const root = document.getElementById('product-lightbox');
  const img = document.getElementById('product-lightbox-img');
  const caption = document.getElementById('product-lightbox-caption');
  const triggers = document.querySelectorAll('[data-lightbox-src]');

  if (!root || !img || !triggers.length) return;

  let lastFocus = null;

  const focusableSelector =
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])';

  const close = () => {
    if (root.hasAttribute('hidden')) return;
    root.setAttribute('hidden', '');
    root.classList.remove('is-open');
    document.body.style.overflow = '';
    img.removeAttribute('src');
    img.alt = '';
    if (caption) caption.textContent = '';
    if (lastFocus && typeof lastFocus.focus === 'function') {
      lastFocus.focus();
    }
    lastFocus = null;
  };

  const open = (trigger) => {
    const src = trigger.getAttribute('data-lightbox-src');
    if (!src) return;
    lastFocus = document.activeElement;
    img.src = src;
    img.alt = trigger.getAttribute('data-lightbox-alt') || '';
    if (caption) {
      caption.textContent = trigger.getAttribute('data-lightbox-caption') || '';
    }
    root.removeAttribute('hidden');
    // next frame so CSS can transition
    requestAnimationFrame(() => root.classList.add('is-open'));
    document.body.style.overflow = 'hidden';
    const closeBtn = root.querySelector('.product-lightbox__close');
    closeBtn?.focus();
  };

  triggers.forEach((btn) => {
    btn.addEventListener('click', () => open(btn));
  });

  root.querySelectorAll('[data-lightbox-close]').forEach((el) => {
    el.addEventListener('click', close);
  });

  document.addEventListener('keydown', (e) => {
    if (root.hasAttribute('hidden')) return;
    if (e.key === 'Escape') {
      e.preventDefault();
      close();
      return;
    }
    // Focus trap while open
    if (e.key !== 'Tab') return;
    const nodes = [...root.querySelectorAll(focusableSelector)].filter(
      (el) => !el.hasAttribute('disabled') && el.offsetParent !== null
    );
    if (!nodes.length) return;
    const first = nodes[0];
    const last = nodes[nodes.length - 1];
    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  });
}
