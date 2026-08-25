document.addEventListener("DOMContentLoaded", () => {
  const fuente = document.getElementById("chordpro-fuente").textContent;
  const contenedor = document.getElementById("cancion-render");
  const tonoActualEl = document.getElementById("tono-actual");

  const parser = new ChordSheetJS.ChordProParser();
  const formatter = new ChordSheetJS.HtmlDivFormatter();

  const song = parser.parse(fuente);
  let semitonos = 0;

  function inyectarCSS() {
    if (document.getElementById("chordsheet-css")) return;
    const style = document.createElement("style");
    style.id = "chordsheet-css";
    style.textContent = formatter.cssString();
    document.head.appendChild(style);
  }

  function render() {
    const cancionActual = semitonos === 0 ? song : song.transpose(semitonos);
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

  inyectarCSS();
  render();
});