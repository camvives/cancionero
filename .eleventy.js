module.exports = function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy("assets");

  return {
    pathPrefix: "/cancionero/",
    dir: {
      input: ".",
      includes: "_includes",
      output: "_site"
    }
  };
};