document.addEventListener("DOMContentLoaded", () => {
  const input = document.getElementById("buscador");
  if (!input) return;

  input.addEventListener("input", () => {
    const termino = input.value.toLowerCase().trim();

    // "13", "sp 13" o "bp 63": busca por número de cancionero.
    // Se compara como número para que "13" encuentre "013".
    const busquedaNumero = termino.match(/^(sp|bp)?\s*(\d+)$/);

    document.querySelectorAll(".categoria").forEach((bloque) => {
      let algunoVisible = false;

      bloque.querySelectorAll("li").forEach((li) => {
        const titulo = li.querySelector("a").textContent.toLowerCase();
        let coincide = titulo.includes(termino);

        if (!coincide && busquedaNumero) {
          const [, cancionero, numero] = busquedaNumero;
          const valores = cancionero === "sp" ? [li.dataset.sp]
            : cancionero === "bp" ? [li.dataset.bp]
            : [li.dataset.sp, li.dataset.bp];
          coincide = valores.some((v) => v && Number(v) === Number(numero));
        }

        li.style.display = coincide ? "" : "none";
        if (coincide) algunoVisible = true;
      });

      bloque.style.display = algunoVisible ? "" : "none";
    });
  });
});
