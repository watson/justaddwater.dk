/* Local adaptations of the archived examples. No server calls or persistence. */
(() => {
  'use strict';
  const demo = document.documentElement.dataset.archiveDemo;
  if (demo === 'table-height') {
    // Original example used Prototype to make exactly this DOM change.
    for (const cell of document.querySelectorAll('.slimTable td')) {
      const wrapper = document.createElement('div');
      Object.assign(wrapper.style, { height: '18px', textOverflow: 'ellipsis', overflow: 'hidden', width: '100%' });
      wrapper.append(...cell.childNodes);
      cell.append(wrapper);
    }
  }
  if (demo === 'undo') {
    const list = document.getElementById('todo-list');
    const undo = document.getElementById('undo');
    const levels = document.getElementById('levels');
    const deleted = [];
    let dragged = null;
    const update = () => {
      undo.hidden = deleted.length === 0;
      levels.textContent = deleted.length > 1 ? ` (${deleted.length})` : '';
    };
    list.addEventListener('click', (event) => {
      const link = event.target.closest('[data-delete]');
      if (!link) return;
      event.preventDefault();
      const item = link.closest('li');
      deleted.push(item);
      item.hidden = true;
      update();
    });
    undo.addEventListener('click', (event) => {
      event.preventDefault();
      const item = deleted.pop();
      if (item) item.hidden = false;
      update();
    });
    list.addEventListener('dragstart', (event) => {
      dragged = event.target.closest('li');
      if (dragged) event.dataTransfer.setData('text/plain', dragged.id);
    });
    list.addEventListener('dragover', (event) => {
      if (dragged) event.preventDefault();
    });
    list.addEventListener('drop', (event) => {
      event.preventDefault();
      const target = event.target.closest('li');
      if (dragged && target && target !== dragged) {
        const below = event.clientY > target.getBoundingClientRect().top + target.offsetHeight / 2;
        list.insertBefore(dragged, below ? target.nextSibling : target);
      }
      dragged = null;
    });
    list.addEventListener('dragend', () => { dragged = null; });
    update();
  }
})();
