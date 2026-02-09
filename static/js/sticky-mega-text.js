document.addEventListener('DOMContentLoaded', function() {
  const megaTextLeft = document.querySelector('.services-layout__mega-text--left');
  const megaTextRight = document.querySelector('.services-layout__mega-text--right');
  const servicesLayout = document.querySelector('.services-layout');
  const contact = document.querySelector('.contact');

  if (!megaTextLeft || !megaTextRight || !servicesLayout || !contact) return;

  function updateMegaTextPosition() {
    const viewportWidth = window.innerWidth;
    const viewportHeight = window.innerHeight;
    const scrollY = window.scrollY;

    // Get services layout bounds
    const servicesRect = servicesLayout.getBoundingClientRect();
    const servicesTop = scrollY + servicesRect.top;

    // Get contact section bounds
    const contactRect = contact.getBoundingClientRect();
    const contactTop = scrollY + contactRect.top;
    const contactHeight = contact.offsetHeight;
    
    // Start showing text 150px below services top
    const startPoint = servicesTop + 150;
    const stopPoint = contactTop - 150; // Stop in middle of contact section

    // Check if we're in the visible range
    const isInRange = scrollY >= startPoint && scrollY <= stopPoint;

    if (isInRange) {
      // Position text fixed in center of viewport, at 7.5% boundaries
      megaTextLeft.style.position = 'fixed';
      megaTextLeft.style.left = (viewportWidth * 0.075) + 'px';
      megaTextLeft.style.top = (viewportHeight / 2) + 'px';
      megaTextLeft.style.transform = 'translateY(-50%)';

      megaTextRight.style.position = 'fixed';
      megaTextRight.style.right = (viewportWidth * 0.075) + 'px';
      megaTextRight.style.left = 'auto';
      megaTextRight.style.top = (viewportHeight / 2) + 'px';
      megaTextRight.style.transform = 'translateY(-50%)';
    } else {
      // Reset to absolute positioning at 150px when not in scroll range
      megaTextLeft.style.position = 'absolute';
      megaTextLeft.style.left = '7.5%';
      megaTextLeft.style.right = 'auto';
      megaTextLeft.style.top = '150px';
      megaTextLeft.style.transform = 'none';

      megaTextRight.style.position = 'absolute';
      megaTextRight.style.right = '7.5%';
      megaTextRight.style.left = 'auto';
      megaTextRight.style.top = '150px';
      megaTextRight.style.transform = 'none';
    }
  }

  // Update on scroll
  window.addEventListener('scroll', updateMegaTextPosition, { passive: true });
  
  // Update on resize
  window.addEventListener('resize', updateMegaTextPosition, { passive: true });

  // Initial update
  updateMegaTextPosition();
});
