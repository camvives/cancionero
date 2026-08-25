const fs = require("fs");
const path = require("path");
const ChordSheetJS = require("chordsheetjs");

module.exports = () => {
  const dir = path.join(__dirname, "..", "canciones");
  const archivos = fs.readdirSync(dir).filter(f => f.endsWith(".cho"));
  const parser = new ChordSheetJS.ChordProParser();

  return archivos.map(nombreArchivo => {
    const contenido = fs.readFileSync(path.join(dir, nombreArchivo), "utf8");
    const song = parser.parse(contenido);
    const slug = nombreArchivo.replace(".cho", "");

    return {
      slug,
      title: song.title || slug,
      key: song.key || "",
      category: song.metadata.get("category") || "Sin categoría",
      chordpro: contenido
    };
  });
};