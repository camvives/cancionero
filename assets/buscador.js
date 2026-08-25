document.addEventListener("DOMContentLoaded", () => {
  const input = document.getElementById("buscador");
  if (!input) return;

  input.addEventListener("input", () => {
    const termino = input.value.toLowerCase().trim();

    document.querySelectorAll(".categoria").forEach((bloque) => {
      let algunoVisible = false;

      bloque.querySelectorAll("li").forEach((li) => {
        const titulo = li.querySelector("a").textContent.toLowerCase();
        const coincide = titulo.includes(termino);
        li.style.display = coincide ? "" : "none";
        if (coincide) algunoVisible = true;
      });

      bloque.style.display = algunoVisible ? "" : "none";
    });
  });
});