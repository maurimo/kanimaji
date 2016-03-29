# Kanimaji #

## Generation of animations ##

This is a small utility for transforming KanjiVG images into animates SVG of GIF files.

SVG samples:

![084b8 GIF](https://raw.github.com/maurimo/kanimaji/gh-pages/samples/084b8_anim.svg)
![08972 GIF](https://raw.github.com/maurimo/kanimaji/gh-pages/samples/08972_anim.svg)

GIF samples:

![084b8 GIF](https://raw.github.com/maurimo/kanimaji/gh-pages/samples/084b8_anim.gif)
![08972 GIF](https://raw.github.com/maurimo/kanimaji/gh-pages/samples/08972_anim.gif)

## Dependencies ##

Kanimaji depends on
 * [Python 2.7]() with lxml support.
 * [svg.path](https://pypi.python.org/pypi/svg.path)  Python library, for approximating path lengths.
If you want to be able to generate animated GIF, you will also need:
 * [svgexport](https://github.com/shakiba/svgexport) Python library, for exporting SVG to PNG.
 * [ImageMagick](www.imagemagick.org)'s convert program to merge PNG's into a GIF

## Usage ##

Just run
```
./kanimaji.py file1.svg file2.svg ...
```
where the files are KanjiVG SVG files (could work with other SVG files, but it hasn't been tested).

## Settings ##

Just edit the settings.py file, all settings are explained there. In this file you can also enable/disable SVG and GIF generation.

## License ##

You are free to do what you want with this program, please credit my work you use it.
If you find it useful and feel like, you may give a donation on my github page!
