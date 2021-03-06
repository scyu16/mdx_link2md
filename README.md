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

## Installation

The project is on [PyPI](https://pypi.org/project/mdx-link2md/)!

```bash
$ pip install mdx_link2md
```

If you want the latest version, which might include unreleased-to-PyPI code,
you can always grab the `develop` branch directly from Git.

```bash
$ pip install git+git://github.com/scyu16/mdx_link2md.git
```

## Usage

### As A Utility Script
The package can run as a top-level script to convert the multiple markdown files in batch:
```bash
$ python -m mdx_link2md <files_to_be_converted>
```
The converted files are placed in the same directory as the source files with the same
names of `html` extension.

### As A Module
If more flexibility is desired, the package could be used as a `Python` module.

```python
from markdown import markdown
from mdx_link2md.markdownlinks import MarkdownLinkExtension
 

md = markdown.Markdown(output_format='html5',
                       extensions=[MarkdownLinkExtension(ignore_url=False)])
md.convertFile('input_file', output='output_file', encoding='utf-8')

```
Please see [\_\_main\_\_.py](./mdx_link2md/__main__.py) for the source code of the 
script that makes the module work as a utility, as described in the preceding subsection. 

### Configuration Settings

The only setting for the extension is `ignore_url`, with a `True` default value.
When `ignore_url` is `False`, markdown links to none local files are also updated:

|ignore_url| input | output |
|:--------:| :-----: | :-------:|
|True      | ```[help](http://xyz.com/read.mD)```|```<a href="http://xyz.com/read.mD">help</a>```|
|False      | ```[help](http://xyz.com/read.mD)```|```<a href="http://xyz.com/read.html">help</a>```|

*Note*:
 
    1. If the package is run as a utility script, `ignore_url` is set to `True`.
    2. The package is case insensitive to the `md` file extension in either usage.


## Development

`develop` branch holds the latest stable code. Please create branches off `develop`
branch for any changes or enhancement. It's suggested you first create a virtual
environment and activate it, then:

```bash
$ git clone git@github.com:scyu16/mdx_link2md.git
```
. For Python 2.x,
```bash
$ pip install -r requirements/python2.txt
```
, while for Python 3.x,
```bash
$ pip install -r requirements/python3.txt
```

With this being done, `import mdx_link2md` would pick up any local changes made to
the package.

## TODO
1. Make it work for links in other forms
2. Fix circle ci for publishing to PyPi
