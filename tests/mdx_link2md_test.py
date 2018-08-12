#!/usr/bin/env python

import pytest
import markdown

try:
    from mdx_link2md.markdownlinks import MarkdownLinkExtension
except ModuleNotFoundError:
    import sys
    import os

    curr_dir_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(curr_dir_path))
    try:
        from mdx_link2md.markdownlinks import MarkdownLinkExtension
    except ModuleNotFoundError as e:
        sys.exit(e)


class TestMdxLink2MD:
    def test_convert_non_url_md_link(self):
        # The default value for ignore_url is True
        md = markdown.Markdown(output_format='html5',
                               extensions=[MarkdownLinkExtension(ignore_url=True)])

        input_text = '''Please read
        [help](../read.md). You will
        like it; The online version is [here](http://help.xyz/read.md)'''

        expected_output = '''<p>Please read
        <a href="../read.html">help</a>. You will
        like it; The online version is <a href="http://help.xyz/read.md">here</a></p>'''

        output_text = md.convert(input_text)

        assert output_text == expected_output

    def test_convert_any_md_links(self):
        md = markdown.Markdown(output_format='html5',
                               extensions=[MarkdownLinkExtension(ignore_url=False)])

        input_text = '''Please read
        [help](../read.md). You will
        like it; The online version is [here](http://help.xyz/read.md)'''

        expected_output = '''<p>Please read
        <a href="../read.html">help</a>. You will
        like it; The online version is <a href="http://help.xyz/read.html">here</a></p>'''

        output_text = md.convert(input_text)

        assert output_text == expected_output

    def test_convert_non_url_md_links_on_single_line(self):
        # The default value for ignore_url is True
        md = markdown.Markdown(output_format='html5',
                               extensions=[MarkdownLinkExtension(ignore_url=True)])

        input_text = 'Please read [help](../read.md). You will\
like it; A simplified online version is [here](http://help.xyz/read.md);\
A detailed online version is [available here](http://help.xyz/read_l.md)'

        expected_output = '<p>Please read <a href="../read.html">help</a>. You will\
like it; A simplified online version is <a href="http://help.xyz/read.md">here</a>;\
A detailed online version is <a href="http://help.xyz/read_l.md">available here</a></p>'

        output_text = md.convert(input_text)

        assert output_text == expected_output

    def test_convert_any_md_links_on_single_line(self):
        md = markdown.Markdown(output_format='html5',
                               extensions=[MarkdownLinkExtension(ignore_url=False)])

        input_text = 'Please read [help](../read.md). You will\
like it; A simplified online version is [here](http://help.xyz/read.md);\
A detailed online version is [available here](http://help.xyz/read_l.md)'

        expected_output = '<p>Please read <a href="../read.html">help</a>. You will\
like it; A simplified online version is <a href="http://help.xyz/read.html">here</a>;\
A detailed online version is <a href="http://help.xyz/read_l.html">available here</a></p>'

        output_text = md.convert(input_text)

        assert output_text == expected_output


if __name__ == '__main__':
    pytest.main(['-x', './'])
