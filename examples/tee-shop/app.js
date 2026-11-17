(() => {
  const colors = [...document.querySelectorAll('.swatch')];
  const sizes = [...document.querySelectorAll('[data-size]')];
  const thumbnails = [...document.querySelectorAll('.thumbnail')];
  const message = document.querySelector('#form-message');
  const colorLabel = document.querySelector('#selected-color');
  const sizeLabel = document.querySelector('#selected-size');
  const quantityOutput = document.querySelector('#quantity');
  const addButton = document.querySelector('.add-button');
  const bag = document.querySelector('.bag-button');
  const bagCount = document.querySelector('.bag-count');
  let selectedColor = '';
  let selectedSize = '';
  let quantity = 1;
  let inBag = 0;

  colors.forEach((button) => button.addEventListener('click', () => {
    selectedColor = button.dataset.color;
    colorLabel.textContent = selectedColor;
    colors.forEach((item) => item.setAttribute('aria-pressed', String(item === button)));
    message.textContent = '';
  }));

  sizes.forEach((button) => button.addEventListener('click', () => {
    selectedSize = button.dataset.size;
    sizeLabel.textContent = selectedSize;
    sizes.forEach((item) => item.setAttribute('aria-pressed', String(item === button)));
    message.textContent = '';
  }));

  document.querySelectorAll('[data-quantity]').forEach((button) => button.addEventListener('click', () => {
    quantity = Math.max(1, Math.min(9, quantity + (button.dataset.quantity === 'plus' ? 1 : -1)));
    quantityOutput.value = String(quantity);
    quantityOutput.textContent = String(quantity).replace(/[0-9]/g, (digit) => '۰۱۲۳۴۵۶۷۸۹'[Number(digit)]);
  }));

  thumbnails.forEach((button) => button.addEventListener('click', () => {
    thumbnails.forEach((item) => {
      const active = item === button;
      item.classList.toggle('is-active', active);
      item.setAttribute('aria-pressed', String(active));
    });
    message.textContent = 'این تصویرها نمونهٔ نمایشی هستند.';
  }));

  addButton.addEventListener('click', () => {
    if (!selectedColor || !selectedSize) {
      message.textContent = 'لطفاً رنگ و سایز را انتخاب کن.';
      (!selectedColor ? colors[0] : sizes[0]).focus();
      return;
    }
    inBag += quantity;
    bagCount.textContent = String(inBag).replace(/[0-9]/g, (digit) => '۰۱۲۳۴۵۶۷۸۹'[Number(digit)]);
    bag.setAttribute('aria-label', `سبد خرید، ${inBag} کالا`);
    message.textContent = `یک نمونهٔ نمایشی با رنگ ${selectedColor} و سایز ${selectedSize} به سبد اضافه شد؛ خرید واقعی انجام نمی‌شود.`;
  });
})();
