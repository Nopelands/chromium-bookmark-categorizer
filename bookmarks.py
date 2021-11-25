bookmarks_html = open(r"bookmarks.html", "r")  # replace bookmarks.html with file name or location
lines = bookmarks_html.readlines()
sanitized_links = []
for line in lines:
    if "HREF" in line:
        working_line = line.split("\"")
        link = working_line[1]
        if "chrome://newtab" not in link:
            sanitized_links.append(link)
categories = []
for link in sanitized_links:
    working_link = link.split(":")
    working_link = working_link[1][2:]
    working_link = working_link.split("/")[0]
    if working_link not in categories:
        categories.append(working_link)
categorized_links = {}
for category in categories:
    categorized_links[category] = []
for link in sanitized_links:
    working_link = link.split(":")
    working_link = working_link[1][2:]
    working_link = working_link.split("/")[0]
    if link not in categorized_links[working_link]:
        categorized_links[working_link].append(link)
results = open(r"results.html", "w")
results.write(
    "<META HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html; charset=UTF-8\">\n<TITLE>Bookmarks</TITLE>\n<H1>Bookmarks</H1>\n<DL><p>\n")
for key in categorized_links:
    results.write(f"    <DT><H3>{key}</H3>\n")
    results.write("    <DL><p>\n")
    for link in categorized_links[key]:
        results.write("    <DT><A HREF=\"")
        results.write(link)
        results.write(f"\">{link}</A>\n")
    results.write("    </DL></p>\n")
results.write("</DL></p>\n")
bookmarks_html.close()
results.close()
