document.addEventListener("DOMContentLoaded", () => {
  const fuente = document.getElementById("chordpro-fuente").textContent;
  const contenedor = document.getElementById("cancion-render");
  const tonoActualEl = document.getElementById("tono-actual");
  const botonCopiar = document.getElementById("copiar");

  const parser = new ChordSheetJS.ChordProParser();
  const formatter = new ChordSheetJS.HtmlDivFormatter();
  const textFormatter = new ChordSheetJS.TextFormatter();

  const song = parser.parse(fuente);
  let semitonos = 0;
  let cancionActual = song; // se actualiza en cada render, la usa el botón de copiar

  function inyectarCSS() {
    if (document.getElementById("chordsheet-css")) return;
    const style = document.createElement("style");
    style.id = "chordsheet-css";
    style.textContent = formatter.cssString();
    document.head.appendChild(style);
  }

  function render() {
    cancionActual = semitonos === 0 ? song : song.transpose(semitonos);
    contenedor.innerHTML = formatter.format(cancionActual);
    tonoActualEl.textContent = cancionActual.key || song.key;
  }

  document.getElementById("subir").addEventListener("click", () => {
    semitonos++;
    render();
  });

  document.getElementById("bajar").addEventListener("click", () => {
    semitonos--;
    render();
  });

  botonCopiar.addEventListener("click", async () => {
    const texto = textFormatter.format(cancionActual);
    try {
      await navigator.clipboard.writeText(texto);
      const textoOriginal = botonCopiar.textContent;
      botonCopiar.textContent = "✅ ¡Copiado!";
      setTimeout(() => {
        botonCopiar.textContent = textoOriginal;
      }, 1800);
    } catch (err) {
      alert("No se pudo copiar automáticamente. Probá seleccionar el texto manualmente.");
    }
  });

  inyectarCSS();
  render();
});