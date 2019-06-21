from requests_html import HTMLSession
session = HTMLSession()


def alt_title(urls):
	imgs = {'sem_alt': [], 'sem_title': [], 'sem_alt_title': []}
	for url in urls:
		r = session.get(url)
		tags_img = r.html.find('img')

		for img in tags_img:
			if 'alt' not in img.attrs:
				imgs['sem_alt'].append(img.attrs["src"])

			if 'title' not in img.attrs:
				imgs['sem_title'].append(img.attrs["src"])

			if 'alt' not in img.attrs and 'title' not in img.attrs:
				imgs['sem_alt_title'].append(img.attrs["src"])
	return imgs
