#!/usr/bin/python3
'''
A script that codes markdown to HTML
'''
import re
import sys
import os
import markdown


def markdown2html(markdown_file, output_file_name):
    """
    Write a script markdown2html.py that takes an argument 2 strings:

    First argument is the name of the Markdown file
    Second argument is the output file name
    Requirements:

    If the number of arguments is less than 2: print in STDERR Usage:
    ./markdown2html.py README.md README.html and exit 1
    If the Markdown file doesn’t exist: print in STDER Missing
    <filename> and exit 1
    Otherwise, print nothing and exit 0
    """
#     if not os.path.exists(markdown_file):
#         print(f"Missing {markdown_file}", file=sys.stderr)
#         sys.exit(1)

#     # Read the markdown file
#     with open(markdown_file, 'r') as f:
#         content = f.read()

#     # Convert markdown to html
#     html = markdown.markdown(content)

#     # Write the html to the output file
#     with open(output_file_name, 'w') as f:
#         f.write(html)

#     # Exit successfully
#     sys.exit(0)


# if __name__ == "__main__":
#     if len(sys.argv) < 3:
#         print("Usage: ./markdown2html.py README.md README.html",
#               file=sys.stderr)
#         sys.exit(1)

#     # Get the arguments
#     markdown_file = sys.argv[1]
#     output_file_name = sys.argv[2]

#     # Convert markdown to html
#     markdown2html(markdown_file, output_file_name)

# Check if the number of arguments is less than 2
# if len(sys.argv) < 3:
#     print("Usage: ./markdown2html.py README.md README.html",
#           file=sys.stderr)
#     sys.exit(1)

# Get the arguments
# markdown_file = sys.argv[1]
# output_file_name = sys.argv[2]

# Check if the Markdown file doesn't exist
# if not os.path.exists(markdown_file):
#     print(f"Missing {markdown_file}", file=sys.stderr)
#     sys.exit(1)

# if all checks pass, read the markdown file
# sys.exit(0)
    if __name__ == '__main__':

        # Test that the number of arguments passed is 2
        if len(sys.argv[1:]) != 2:
            print('Usage: ./markdown2html.py README.md README.html',
                file=sys.stderr)
            sys.exit(1)

        # Store the arguments into variables
        input_file = sys.argv[1]
        output_file = sys.argv[2]

        # Checks that the markdown file exists and is a file
        if not (os.path.exists(input_file) and os.path.isfile(input_file)):
            print(f'Missing {input_file}', file=sys.stderr)
            sys.exit(1)

        with open(input_file, encoding='utf-8') as file_1:
            html_content = []
            md_content = [line[:-1] for line in file_1.readlines()]
            for line in md_content:
                heading = re.split(r'#{1,6} ', line)
                if len(heading) > 1:
                    # Compute the number of the # present to
                    # determine heading level
                    h_level = len(line[:line.find(heading[1])-1])
                    # Append the html equivalent of the heading
                    html_content.append(
                        f'<h{h_level}>{heading[1]}</h{h_level}>\n'
                    )
                else:
                    html_content.append(line)

        with open(output_file, 'w', encoding='utf-8') as file_2:
            file_2.writelines(html_content)
