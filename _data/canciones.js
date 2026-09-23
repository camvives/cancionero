const fs = require("fs");
const path = require("path");
const ChordSheetJS = require("chordsheetjs");

// Solo se publican las canciones marcadas con {meta: estado revisada}.
// Para ver también los borradores al trabajar localmente:
//   MOSTRAR_BORRADORES=1 npx @11ty/eleventy --serve
const mostrarBorradores = process.env.MOSTRAR_BORRADORES === "1";

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
      sanpedro: song.metadata.get("sanpedro") || "",
      buenpastor: song.metadata.get("buenpastor") || "",
      revisada: song.metadata.get("estado") === "revisada",
      chordpro: contenido
    };
  }).filter(cancion => cancion.revisada || mostrarBorradores);
};
