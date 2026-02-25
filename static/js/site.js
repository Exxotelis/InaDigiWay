// Site.js - Main JavaScript file

document.addEventListener('DOMContentLoaded', function() {
  console.log('In A Digi Way - Site JS loaded');

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href !== '#' && href !== '#book-call') {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          target.scrollIntoView({ behavior: 'smooth' });
        }
      }
    });
  });

  // Handle "Book a call" button with Calendly modal
  const bookCallButtons = document.querySelectorAll('[href="#book-call"]');
  const modal = document.getElementById('calendly-modal');
  const iframe = document.getElementById('calendly-iframe');
  const calendlyUrl = document.body.getAttribute('data-calendly-url');

  const openModal = (url) => {
    const resolvedUrl = url || calendlyUrl;
    if (!modal || !iframe || !resolvedUrl) return;
    iframe.src = resolvedUrl;
    modal.classList.add('calendly-modal--open');
    modal.setAttribute('aria-hidden', 'false');
  };

  const closeModal = () => {
    if (!modal || !iframe) return;
    modal.classList.remove('calendly-modal--open');
    modal.setAttribute('aria-hidden', 'true');
    iframe.src = '';
  };

  if (modal) {
    modal.addEventListener('click', (event) => {
      if (event.target.matches('[data-calendly-close]')) {
        closeModal();
      }
    });
  }

  bookCallButtons.forEach(btn => {
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      const buttonUrl = btn.getAttribute('data-calendly-url');
      openModal(buttonUrl);
    });
  });

  // Contact form handling
  const contactForm = document.querySelector('.contact__form');
  if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
      e.preventDefault();
      alert('Form submitted! Implement backend submission.');
      // You can add form submission logic here
    });
  }

  // Quote modal handling
  const quoteModal = document.getElementById('quote-modal');
  const quoteForm = document.getElementById('quote-form');

  const openQuoteModal = () => {
    if (!quoteModal) return;
    quoteModal.classList.add('quote-modal--open');
    quoteModal.setAttribute('aria-hidden', 'false');
  };
  const closeQuoteModal = () => {
    if (!quoteModal) return;
    quoteModal.classList.remove('quote-modal--open');
    quoteModal.setAttribute('aria-hidden', 'true');
  };

  document.querySelectorAll('[href="#get-quote"], [href="#quote"], [data-open-quote]').forEach(el => {
    el.addEventListener('click', function(e) {
      e.preventDefault();
      openQuoteModal();
    });
  });

  if (quoteModal) {
    quoteModal.addEventListener('click', (event) => {
      if (event.target.matches('[data-quote-close]')) closeQuoteModal();
    });
  }

  // CSRF helper
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  if (quoteForm) {
    quoteForm.addEventListener('submit', async function(e) {
      e.preventDefault();
      const formData = new FormData(quoteForm);
      const statusEl = quoteForm.querySelector('.quote-form__status');
      statusEl.textContent = '';
      try {
        const res = await fetch('/quote/submit/', {
          method: 'POST',
          headers: { 'X-CSRFToken': getCookie('csrftoken') },
          body: formData
        });
        const json = await res.json();
        if (res.ok && json.status === 'success') {
          statusEl.textContent = json.message || 'Thanks — request received.';
          quoteForm.reset();
          setTimeout(closeQuoteModal, 1200);
        } else {
          statusEl.textContent = json.message || 'An error occurred.';
        }
      } catch (err) {
        statusEl.textContent = 'Network error. Please try again.';
      }
    });
  }

  // Burger menu toggle
  const header = document.querySelector('.site-header');
  const burger = document.querySelector('.site-header__burger');
  const mobileMenu = document.getElementById('mobile-menu');
  if (burger && header && mobileMenu) {
    burger.addEventListener('click', () => {
      const isOpen = header.classList.toggle('site-header--open');
      burger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    mobileMenu.querySelectorAll('a[href^="#"]').forEach((link) => {
      link.addEventListener('click', () => {
        header.classList.remove('site-header--open');
        burger.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Mobile submenu toggle for Services
  document.querySelectorAll('.site-header__mobile-toggle').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      const li = btn.closest('.mobile-has-submenu');
      const expanded = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', expanded ? 'false' : 'true');
      if (li) li.classList.toggle('open', !expanded);
    });
  });

  // Fancy hover wave for key text blocks (lightweight)
  const waveTargets = document.querySelectorAll(
    '.service-showcase__title, .about__title, .happy-clients__title, .contact__title'
  );

  waveTargets.forEach((el) => {
    if (el.dataset.waveReady === '1') return;
    if (!el.firstChild || el.childNodes.length !== 1 || el.firstChild.nodeType !== Node.TEXT_NODE) return;

    const text = el.textContent || '';
    if (!text.trim()) return;

    const frag = document.createDocumentFragment();
    const wrapper = document.createElement('span');
    wrapper.className = 'text-wave';

    const words = text.trim().split(/\s+/);
    let charIndex = 0;

    words.forEach((word, wordIdx) => {
      const wordSpan = document.createElement('span');
      wordSpan.className = 'text-wave__word';

      Array.from(word).forEach((ch) => {
        const charSpan = document.createElement('span');
        charSpan.className = 'text-wave__char';
        charSpan.style.setProperty('--char-index', String(charIndex));
        charSpan.textContent = ch;
        wordSpan.appendChild(charSpan);
        charIndex += 1;
      });

      wrapper.appendChild(wordSpan);
      if (wordIdx < words.length - 1) {
        wrapper.appendChild(document.createTextNode(' '));
        charIndex += 1;
      }
    });

    frag.appendChild(wrapper);
    el.textContent = '';
    el.appendChild(frag);
    el.dataset.waveReady = '1';

    el.addEventListener('mouseenter', () => {
      wrapper.classList.remove('is-wave');
      // Force reflow so animation can replay on every hover
      void wrapper.offsetWidth;
      wrapper.classList.add('is-wave');
    });
  });

  // Fancy paragraph hover glow (lightweight)
  const paragraphFxTargets = document.querySelectorAll(
    '.service-showcase__description, .about__text, .hero__service-preview--hero .service-showcase__description'
  );

  paragraphFxTargets.forEach((el) => {
    el.classList.add('text-paragraph-fx');

    el.addEventListener('pointermove', (event) => {
      const rect = el.getBoundingClientRect();
      if (!rect.width || !rect.height) return;
      const x = ((event.clientX - rect.left) / rect.width) * 100;
      const y = ((event.clientY - rect.top) / rect.height) * 100;
      el.style.setProperty('--fx-x', `${Math.max(0, Math.min(100, x))}%`);
      el.style.setProperty('--fx-y', `${Math.max(0, Math.min(100, y))}%`);
    }, { passive: true });

    el.addEventListener('pointerleave', () => {
      el.style.setProperty('--fx-x', '50%');
      el.style.setProperty('--fx-y', '50%');
    }, { passive: true });
  });

  // Hero title per-letter cinematic ripple (preserves line breaks)
  function applyHeroLetterFx(target) {
    if (!target || target.dataset.heroFxReady === '1') return;

    let charIndex = 0;
    const transformNode = (node) => {
      if (node.nodeType === Node.TEXT_NODE) {
        const text = node.textContent || '';
        const fragment = document.createDocumentFragment();
        const parts = text.split(/(\s+)/);

        parts.forEach((part) => {
          if (!part) return;
          if (/^\s+$/.test(part)) {
            fragment.appendChild(document.createTextNode(part));
            return;
          }

          const wordSpan = document.createElement('span');
          wordSpan.className = 'hero-title-fx__word';

          Array.from(part).forEach((ch) => {
            const charSpan = document.createElement('span');
            charSpan.className = 'hero-title-fx__char';
            charSpan.style.setProperty('--char-index', String(charIndex));
            charSpan.textContent = ch;
            wordSpan.appendChild(charSpan);
            charIndex += 1;
          });

          fragment.appendChild(wordSpan);
        });

        return fragment;
      }

      if (node.nodeType === Node.ELEMENT_NODE) {
        const el = node;
        if (el.tagName === 'BR') return el.cloneNode(true);
        const clone = el.cloneNode(false);
        Array.from(el.childNodes).forEach((child) => {
          const transformed = transformNode(child);
          if (transformed) clone.appendChild(transformed);
        });
        return clone;
      }

      return null;
    }

    const fragment = document.createDocumentFragment();
    Array.from(target.childNodes).forEach((child) => {
      const transformed = transformNode(child);
      if (transformed) fragment.appendChild(transformed);
    });

    target.textContent = '';
    target.appendChild(fragment);
    target.classList.add('hero-title-fx');
    target.dataset.heroFxReady = '1';

    const replay = () => {
      target.classList.remove('is-letter-play');
      void target.offsetWidth;
      target.classList.add('is-letter-play');
    };

    target.addEventListener('mouseenter', replay);
    target.addEventListener('focus', replay);
  }

  applyHeroLetterFx(document.querySelector('.home-page .hero__title-normal'));
  applyHeroLetterFx(document.querySelector('.home-page .hero__title-highlight'));

  // Services reveal on scroll (lightweight)
  const serviceCards = document.querySelectorAll('.services-layout .service-showcase');
  if (serviceCards.length) {
    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('service-showcase--in-view');
            obs.unobserve(entry.target);
          }
        });
      }, {
        threshold: 0.12,
        rootMargin: '0px 0px -4% 0px'
      });

      serviceCards.forEach((card) => {
        card.classList.add('service-showcase--reveal');
        observer.observe(card);
      });
    } else {
      serviceCards.forEach((card) => card.classList.add('service-showcase--in-view'));
    }
  }

});

// No scroll shadow - header stays clean
