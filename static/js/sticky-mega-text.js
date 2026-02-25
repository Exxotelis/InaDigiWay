document.addEventListener('DOMContentLoaded', function() {
  const megaTextLeft = document.querySelector('.services-layout__mega-text--left');
  const megaTextRight = document.querySelector('.services-layout__mega-text--right');
  const servicesLayout = document.querySelector('.services-layout');
  const footer = document.querySelector('.site-footer');
  const contact = document.querySelector('.contact');
  if (!megaTextLeft || !megaTextRight || !servicesLayout || !contact) return;

  const STICKY_LINE_LEFT = '10%';
  const STICKY_LINE_RIGHT = '10%';
  const TOP_OFFSET = 130;
  const BOTTOM_OFFSET = 130;

  function applyTopAbsolute() {
    megaTextLeft.style.position = 'absolute';
    megaTextLeft.style.left = '10%';
    megaTextLeft.style.right = 'auto';
    megaTextLeft.style.top = TOP_OFFSET + 'px';
    megaTextLeft.style.transform = 'translateX(-50%)';

    megaTextRight.style.position = 'absolute';
    megaTextRight.style.right = '10%';
    megaTextRight.style.left = 'auto';
    megaTextRight.style.top = TOP_OFFSET + 'px';
    megaTextRight.style.transform = 'translateX(50%)';
  }

  function applySticky() {
    megaTextLeft.style.position = 'fixed';
    megaTextLeft.style.left = STICKY_LINE_LEFT;
    megaTextLeft.style.right = 'auto';
    megaTextLeft.style.top = '50%';
    megaTextLeft.style.transform = 'translate(-50%, -50%)';

    megaTextRight.style.position = 'fixed';
    megaTextRight.style.right = STICKY_LINE_RIGHT;
    megaTextRight.style.left = 'auto';
    megaTextRight.style.top = '50%';
    megaTextRight.style.transform = 'translate(50%, -50%)';
  }

  function applyBottomAbsolute(bottomTop) {
    megaTextLeft.style.position = 'absolute';
    megaTextLeft.style.left = '10%';
    megaTextLeft.style.right = 'auto';
    megaTextLeft.style.top = bottomTop + 'px';
    megaTextLeft.style.transform = 'translateX(-50%)';

    megaTextRight.style.position = 'absolute';
    megaTextRight.style.right = '10%';
    megaTextRight.style.left = 'auto';
    megaTextRight.style.top = bottomTop + 'px';
    megaTextRight.style.transform = 'translateX(50%)';
  }

  function updateMegaTextPosition() {
    if (window.innerWidth <= 768) {
      megaTextLeft.style.position = '';
      megaTextLeft.style.left = '';
      megaTextLeft.style.right = '';
      megaTextLeft.style.top = '';
      megaTextLeft.style.transform = '';

      megaTextRight.style.position = '';
      megaTextRight.style.left = '';
      megaTextRight.style.right = '';
      megaTextRight.style.top = '';
      megaTextRight.style.transform = '';
      return;
    }

    const scrollY = window.scrollY;
    const servicesRect = servicesLayout.getBoundingClientRect();
    const servicesTop = scrollY + servicesRect.top;

    const contactRect = contact.getBoundingClientRect();
    const contactTop = scrollY + contactRect.top;
    const footerTop = footer ? scrollY + footer.getBoundingClientRect().top : contactTop;

    const stickyStart = servicesTop + TOP_OFFSET;
    const stickyEnd = Math.min(footerTop - BOTTOM_OFFSET, contactTop - BOTTOM_OFFSET);

    if (scrollY < stickyStart) {
      applyTopAbsolute();
      return;
    }

    if (scrollY <= stickyEnd) {
      applySticky();
      return;
    }

    const frozenTopInsideServices = stickyEnd - servicesTop;
    applyBottomAbsolute(frozenTopInsideServices);
  }

  window.addEventListener('scroll', updateMegaTextPosition, { passive: true });
  window.addEventListener('resize', updateMegaTextPosition, { passive: true });
  updateMegaTextPosition();
});
