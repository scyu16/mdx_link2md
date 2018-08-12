#!/usr/bin/env python

import argparse
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


def main():
    """
    A sample script that converts markdown files to HTML files with internal links to
    local markdown files changed to corresponding HTML files with the same names.

    """

    md = markdown.Markdown(output_format='html5',
                           extensions=[MarkdownLinkExtension(ignore_url=True)])
    parser = argparse.ArgumentParser(
        description='Convert .md files to HTML with the converted files saved at the '
                    'same location as the original .md files with .html extension.')
    parser.add_argument(dest='target_files', nargs='+', help='files to be processed')

    args = parser.parse_args()

    for md_file in args.target_files:
        try:
            idx = md_file.lower().rindex('.md')
        except ValueError:
            continue

        output_file_name = md_file[:idx] + '.html'
        md.convertFile(md_file, output=output_file_name, encoding='utf-8')

        md.reset()


if __name__ == '__main__':
    main()
