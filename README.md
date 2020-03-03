# unichars

`unichars` is a simple tool for identifying unicode characters. Whether your
fonts can't display them, you need to distinguish between lookalike glyphs, or
you just want to know what characters you're looking at, 'unichars' can help.

With no arguments, `unichars` reads a single line of input, and tells you the
code point and name of each character in it.

Given filenames as arguments (or `-` for standard input), `unichars` displays
that same information for each character in each of the files.

```console
$ unichars
Enter string: u𝗇ι̇ϲοⅾе
U+0075	LATIN SMALL LETTER U
U+1D5C7	MATHEMATICAL SANS-SERIF SMALL N
U+03B9	GREEK SMALL LETTER IOTA
U+0307	COMBINING DOT ABOVE
U+03F2	GREEK LUNATE SIGMA SYMBOL
U+03BF	GREEK SMALL LETTER OMICRON
U+217E	SMALL ROMAN NUMERAL FIVE HUNDRED
U+0435	CYRILLIC SMALL LETTER IE
```
