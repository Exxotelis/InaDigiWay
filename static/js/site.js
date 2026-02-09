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


  // Per-letter hover zoom (headings/buttons/links only)
  const letterTargets = document.querySelectorAll(
    '.service-showcase__title, .services__title, .about__title, .happy-clients__title, .service-showcase__btn, .about__cta-btn, .sticky-cta__btn'
  );

  const splitToLetters = (el) => {
    if (el.dataset.letterHover === 'true') return;
    const text = el.textContent;
    if (!text || text.trim().length === 0) return;
    el.dataset.letterHover = 'true';
    el.classList.add('letter-hover');
    const frag = document.createDocumentFragment();
    for (const ch of text) {
      const span = document.createElement('span');
      span.className = 'letter-hover__char';
      span.textContent = ch === ' ' ? '\u00A0' : ch;
      frag.appendChild(span);
    }
    el.textContent = '';
    el.appendChild(frag);
  };

  letterTargets.forEach((el) => {
    splitToLetters(el);
    el.addEventListener('mousemove', (event) => {
      const rect = el.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;
      el.style.setProperty('--lens-x', `${x}px`);
      el.style.setProperty('--lens-y', `${y}px`);
    });
  });
});

// No scroll shadow - header stays clean
