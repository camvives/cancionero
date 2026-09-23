# Cancionero CIP

Cancionero católico web: una lista de canciones agrupadas por momento de la misa, donde cada
canción se ve con sus acordes, se puede **subir o bajar de tono** y **copiar** ya transpuesta.

Sitio publicado: **https://camvives.github.io/cancionero/**

Las canciones se escriben en archivos de texto con formato [ChordPro](https://www.chordpro.org/)
y el sitio se genera solo con [Eleventy](https://www.11ty.dev/). No hay base de datos ni panel de
administración: **agregar una canción es agregar un archivo**.

## Cómo está armado

| Archivo / carpeta | Para qué sirve |
| --- | --- |
| `canciones/*.cho` | Una canción por archivo, en ChordPro. Es todo el contenido del cancionero. |
| `_data/canciones.js` | Lee los `.cho`, los parsea con ChordSheetJS y arma la lista de canciones. Acá vive el filtro de publicación. |
| `_data/categoriasOrdenadas.js` | Agrupa las canciones por categoría y define en qué orden aparecen en el índice. |
| `indice.njk` | La portada: buscador + listado por categoría. |
| `cancion-pagina.njk` | Plantilla de la página de cada canción (genera una por canción). |
| `assets/transponer.js` | Renderiza los acordes en el navegador y maneja subir/bajar tono y copiar. |
| `assets/buscador.js` | Filtrado en vivo del índice, por título o por número de cancionero. |
| `assets/estilos.css` | Estilos del sitio. |
| `.github/workflows/deploy.yml` | Publica en GitHub Pages con cada push a `main`. |

El `_site/` es la salida del build: se regenera sola y está en el `.gitignore`.

## Publicar una canción: el estado `revisada`

Todas las canciones viven en el repo, pero **solo se publican las que están revisadas**. La marca
es una línea en la cabecera del `.cho`:

```
{meta: estado revisada}
```

Sin esa línea, la canción queda como borrador: no se genera su página ni aparece en el índice.
Eso permite ir subiendo canciones a medio corregir sin que se vean en el sitio.

El flujo de siempre:

1. Creás el `.cho` y lo commiteás (queda invisible en el sitio).
2. Cuando ya revisaste letra y acordes, le agregás `{meta: estado revisada}`.
3. Push a `main` → GitHub Actions rebuildea y la canción aparece publicada.

## Formato de un archivo `.cho`

```
{title: A la huella}
{key: Am}
{meta: category Navidad}
{meta: sanpedro 13}
{meta: buenpastor 132}
{meta: estado revisada}

{start_of_verse}
[Am]A la huella, a la h[Dm]uella, Jos[G]é y Marí[C]a,
[Am]por las pampas hel[Dm]adas, card[E7]os y ortig[Am]as.
{end_of_verse}

{start_of_chorus}
[C]Coro de la can[G]ción...
{end_of_chorus}
```

Cabecera:

| Directiva | Obligatoria | Qué hace |
| --- | --- | --- |
| `{title: ...}` | sí | Título que se muestra en el índice y en la página. Si falta, se usa el nombre del archivo. |
| `{key: ...}` | sí | Tono original. Es el punto de partida del transpositor. |
| `{meta: category ...}` | sí | Categoría; define en qué bloque del índice aparece (ver lista abajo). |
| `{meta: sanpedro N}` | si aplica | Número en el cancionero San Pedro. Se muestra como chip verde y es buscable. |
| `{meta: buenpastor N}` | si aplica | Número en el cancionero Buen Pastor. Chip rojo, también buscable. |
| `{meta: estado revisada}` | para publicar | Sin esto, la canción no se publica. |

Cuerpo: acordes entre corchetes pegados a la sílaba donde entran (`car[E7]dos`), y las secciones
envueltas en `{start_of_verse}` / `{end_of_verse}` o `{start_of_chorus}` / `{end_of_chorus}`.

### Nombre del archivo

El nombre del archivo es el slug y por lo tanto la URL: `canciones/a-la-huella.cho` se publica en
`/cancionero/canciones/a-la-huella/`. Usar minúsculas, sin acentos ni ñ, palabras separadas por
guiones. Renombrar el archivo cambia el link, así que conviene elegirlo bien de entrada.

Cuando la misma canción tiene versiones distintas en cada cancionero, se separan con sufijo:
`alma-de-cristo-sp.cho` y `alma-de-cristo-bp.cho`.

## Categorías

Solo estas categorías aparecen en el índice, y en este orden:

`Entrada` · `Aleluya` · `Post-Homilía` · `Ofrendas` · `Santo` · `Cordero` · `Comunión` ·
`Meditación` · `Salida` · `María` · `Adoración` · `Perdón` · `Gloria` · `Espíritu-Santo` ·
`Cuaresma` · `Navidad` · `Pascua` · `Alabanza` · `Animación`

⚠️ Si una canción tiene una categoría que no está en esa lista (o está mal escrita, por ejemplo
sin tilde en `Comunión`), **no aparece en el índice** aunque se genere su página. Para sumar una
categoría nueva hay que agregarla a la lista en `_data/categoriasOrdenadas.js`.

## Trabajar localmente

Requiere Node 20 o superior.

```powershell
npm install

# ver el sitio como se publica (solo canciones revisadas)
npx @11ty/eleventy --serve

# ver además los borradores, marcados con un chip gris "borrador"
$env:MOSTRAR_BORRADORES=1; npx @11ty/eleventy --serve
```

En Git Bash la última línea es `MOSTRAR_BORRADORES=1 npx @11ty/eleventy --serve`.

El sitio local queda en http://localhost:8080/cancionero/ (el `/cancionero/` viene del
`pathPrefix`, que es el nombre del repo en GitHub Pages).

`MOSTRAR_BORRADORES` solo existe en tu máquina: el workflow de GitHub Actions no la define, así
que el sitio publicado siempre muestra únicamente lo revisado.

## Buscador

El campo de búsqueda del índice filtra por:

- **título**: cualquier parte del nombre de la canción;
- **número**: `13` busca en ambos cancioneros; `sp 13` o `bp 127` buscan en uno solo. Compara como
  número, así que `13` también encuentra un `013`.

## Despliegue

Cada push a `main` dispara `.github/workflows/deploy.yml`, que instala dependencias, corre
`npx @11ty/eleventy` y publica `_site/` en GitHub Pages. No hay que buildear ni commitear nada a
mano: alcanza con pushear los `.cho`.
