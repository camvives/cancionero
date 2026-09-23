module.exports = function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy("assets");

  // El README es documentación del repo, no una página del sitio.
  eleventyConfig.ignores.add("README.md");

  return {
    pathPrefix: "/cancionero/",
    dir: {
      input: ".",
      includes: "_includes",
      output: "_site"
    }
  };
};