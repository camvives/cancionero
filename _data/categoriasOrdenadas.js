const obtenerCanciones = require("./canciones.js");

module.exports = () => {
  const canciones = obtenerCanciones();

  const orden = [
    "Entrada",
    "Aleluya",
    "Post-Homilía",
    "Ofrendas",
    "Santo",
    "Cordero",
    "Comunión",
    "Meditación",
    "Salida",
    "María",
    "Adoración",
    "Perdón",
    "Gloria",
    "Navidad",
  ];

  return orden
    .map(categoria => ({
      categoria,
      canciones: canciones.filter(c => c.category === categoria)
    }))
    .filter(grupo => grupo.canciones.length > 0);
};