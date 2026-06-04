// Effet de chargement sur les boutons
document.addEventListener('DOMContentLoaded', () => {
  const forms = document.querySelectorAll('.buy-form');
  
  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      const btn = form.querySelector('.buy-btn');
      const originalText = btn.innerHTML;
      
      // Feedback visuel immédiat
      btn.disabled = true;
      btn.innerHTML = '⏳ Redirection...';
      
      // La redirection se fera normalement, mais on donne un feedback
      setTimeout(() => {
        btn.innerHTML = originalText;
        btn.disabled = false;
      }, 3000); // Sécurité au cas où
    });
  });
  
  // Lazy loading simple pour les images
  const images = document.querySelectorAll('.product-image');
  images.forEach(img => {
    img.loading = 'lazy';
  });
});