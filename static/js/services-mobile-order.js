document.addEventListener('DOMContentLoaded', function () {
  const showcases = document.querySelectorAll('.service-showcase');
  if (!showcases.length) return;

  const originalPositions = new WeakMap();

  const storeOriginal = (node) => {
    if (!node || originalPositions.has(node)) return;
    originalPositions.set(node, {
      parent: node.parentElement,
      next: node.nextElementSibling,
    });
  };

  const restoreOriginal = (node) => {
    const info = originalPositions.get(node);
    if (!info || !info.parent) return;
    if (info.next && info.parent.contains(info.next)) {
      info.parent.insertBefore(node, info.next);
    } else {
      info.parent.appendChild(node);
    }
  };

  const applyOrder = () => {
    const isMobile = window.matchMedia('(max-width: 768px)').matches;

    showcases.forEach((showcase) => {
      const image = showcase.querySelector('.service-showcase__image');
      const content = showcase.querySelector('.service-showcase__content');
      if (!image || !content) return;

      const title = content.querySelector('.service-showcase__title');
      const description = content.querySelector('.service-showcase__description');
      const actions = content.querySelector('.service-showcase__actions');

      if (isMobile) {
        [image, content, title, description, actions].forEach(storeOriginal);

        if (image.parentElement === showcase) {
          showcase.insertBefore(image, showcase.firstElementChild);
        }

        if (image) {
          image.style.setProperty('order', '1', 'important');
        }
        if (content) {
          content.style.setProperty('order', '2', 'important');
        }

        [title, description, actions].filter(Boolean).forEach((node) => {
          content.appendChild(node);
        });

        if (title) title.style.setProperty('order', '1', 'important');
        if (description) description.style.setProperty('order', '2', 'important');
        if (actions) actions.style.setProperty('order', '3', 'important');
      } else {
        [actions, description, title, content, image].forEach((node) => {
          if (node) {
            node.style.removeProperty('order');
            restoreOriginal(node);
          }
        });
      }
    });
  };

  applyOrder();
  window.addEventListener('resize', applyOrder, { passive: true });
});
