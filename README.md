# Mdx Link2MD: Convert markdown to HTML in batch

[![PyPI](https://img.shields.io/pypi/v/mdx_link2md.svg)](https://pypi.org/project/mdx-link2md/)
[![PyPI](https://img.shields.io/pypi/pyversions/mdx_link2md.svg)](https://pypi.org/project/mdx-link2md/)
[![CircleCI](https://img.shields.io/circleci/project/github/scyu16/mdx_link2md/develop.svg)](https://circleci.com/gh/scyu16/mdx_link2md)
[![MIT License](http://img.shields.io/badge/license-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This extension for [Python Markdown](https://github.com/waylan/Python-Markdown)
changes `md` extension in the markdown links to `html` before links in the text 
are converted to HTML hyperlinks. For example, the sample text in markdown format,

```markdown
Please read [help](../read.md)
```

would be converted to
```html
Please read <a href="../read.html">help</a>
```
.

This would allow converting markdown files to HTML format in batch,
with internal links to markdown files being updated to the corresponding HTML files. It
helps most when there are cross references among the markdown documents of 
interest.

## Usage

### Minimal Example

```python
from markdown import markdown
from mdx_link2md.markdownlinks import MarkdownLinkExtension
 

md = markdown.Markdown(output_format='html5',
                       extensions=[MarkdownLinkExtension(ignore_url=False)])
md.convertFile('input_file', output='output_file', encoding='utf-8')

```
Please see [markdown2html.py](./examples/markdown2html.py) for a working example, which
could also be used as a utility to convert markdown files in batch. 

### Configuration Settings

The only setting for the extension is `ignore_url`, with a `True` default value.
When `ignore_url` is `False`, markdown links to none local files are also updated:

|ignore_url| input | output |
|:--------:| :-----: | :-------:|
|True      | ```[help](http://xyz.com/read.mD)```|```<a href="http://xyz.com/read.mD">help</a>```|
|False      | ```[help](http://xyz.com/read.mD)```|```<a href="http://xyz.com/read.html">help</a>```|

*Note*: the preprocessing is case insensitive to the `md` file extension.

## Installation

The project is [on PyPI](https://pypi.org/project/mdx-link2md/)!

```bash
pip install mdx_link2md
```

If you want the latest version, which might include unreleased-to-PyPI code,
you can always grab the master branch directly from Git.

```bash
pip install git+git://github.com/scyu16/mdx_link2md.git
```

## Development

`develop` branch has the latest stable code base. Please create branches off `develop` 
branch for any changes or enhancement.


## TODO
1. Allow to run with -m flag from the command line
2. Make it work for links in other forms
