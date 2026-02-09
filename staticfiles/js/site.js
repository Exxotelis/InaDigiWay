// Site.js - Main JavaScript file

document.addEventListener('DOMContentLoaded', function() {
  console.log('In A Digi Way - Site JS loaded');

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href !== '#') {
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

  const openModal = () => {
    if (!modal || !iframe || !calendlyUrl) return;
    iframe.src = calendlyUrl;
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
      openModal();
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
});

// No scroll shadow - header stays clean
