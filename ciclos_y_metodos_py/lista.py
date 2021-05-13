import sys

html = "<ul>\n"
items = int(sys.argv[1])
i = 0

while i < items:
    i += 1
    html += "\t<li> item {} </li>\n".format(i)

html += "</ul>"
print(html)