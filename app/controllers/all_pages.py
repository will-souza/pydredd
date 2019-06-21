from requests_html import HTMLSession


def all_pages(url):
  def main_url(url):
    url = url.split('//')
    url = url[1].split('/')
    return url[0]
  root = main_url(url)

  def valid_url(url):
    if '?' not in url and '#' not in url and '.jpg' not in url and '.jpeg' not in url and '.png' not in url and '.png' not in url and '.pdf' not in url:
      return True
    else:
      return False

  session = HTMLSession()
  r = session.get(url)
  insideLinks = r.html.absolute_links

  links = []
  visitedLinks = [url]

  def site_urls(insideLinks):
    for link in insideLinks:
      if 'http' in link and root in link:
        if valid_url(link):
          links.append(link)
    for link in links:
      if link not in visitedLinks:
        visitedLinks.append(link)
        r = session.get(link)
        pageLinks = r.html.absolute_links
        site_urls(pageLinks)
  site_urls(insideLinks)
  return visitedLinks

