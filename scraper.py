import scraperwiki
html = scraperwiki.scrape('https://inmo.ie/6022')
import lxml.html
root = lxml.html.fromstring(html) # turn our HTML into an lxml object
trs = root.cssselect('tr') # get all the <td> tags
for tr in trs:
    print tr.text_content() # just the text inside the HTML tag including inside children, without markup
for tr in trs:
    record = { "tr" : tr.text_content() } # column name and value
    try:
        scraperwiki.sqlite.save(["tr"], record) # save the records one by one
    except:
        record = { "tr" : "NO ENTRY" } # column name and value
        scraperwiki.sqlite.save(["tr"], record) # save the records one by one
  

