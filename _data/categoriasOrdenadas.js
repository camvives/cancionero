const obtenerCanciones = require("./canciones.js");

module.exports = () => {
  const canciones = obtenerCanciones();

  const orden = [
    "Entrada",
    "Perdón",
    "Gloria",
    "Aleluya",
    "Post-homilia",
    "Ofrenda",
    "Santo",
    "Cordero",
    "Comunion",
    "Meditación",
    "Salida",
    "María"
  ];

  return orden
    .map(categoria => ({
      categoria,
      canciones: canciones.filter(c => c.category === categoria)
    }))
    .filter(grupo => grupo.canciones.length > 0);
};