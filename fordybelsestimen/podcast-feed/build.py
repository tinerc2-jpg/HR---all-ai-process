import json,os,email.utils,html
D=os.path.dirname(os.path.abspath(__file__));T=open(D+'/TOKEN').read().strip()
B=f"https://fordybelsestimen-feed.vercel.app/{T}"
eps=json.load(open(D+'/episodes.json'))
e=html.escape
items="".join(f"""<item><title>{e(x['title'])}</title><description>{e(x['desc'])}</description><enclosure url="{e(x['url'])}" length="{x['bytes']}" type="audio/mpeg"/><guid isPermaLink="false">{e(x['guid'])}</guid><pubDate>{x['date']}</pubDate><itunes:duration>{x['dur']}</itunes:duration><itunes:episode>{x['nr']}</itunes:episode></item>""" for x in sorted(eps,key=lambda x:-x['nr']))
feed=f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"><channel>
<title>Fordybelsestimen</title><link>{B}/</link><language>da</language>
<description>Ledelse, teams og motivation – fra bøgerne til mandag morgen.</description>
<itunes:author>Fordybelsestimen</itunes:author><itunes:image href="{B}/cover.png"/><itunes:block>Yes</itunes:block><itunes:explicit>false</itunes:explicit>
<itunes:category text="Business"><itunes:category text="Management"/></itunes:category>
{items}</channel></rss>"""
open(f"{D}/{T}/feed.xml","w").write(feed)
open(f"{D}/{T}/index.html","w").write(f"""<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width"><meta name=robots content=noindex><title>Fordybelsestimen</title><body style="font-family:system-ui;max-width:600px;margin:40px auto;padding:0 16px;background:#1c2b3a;color:#f5eee1"><h1>Fordybelsestimen</h1><p>Abonnér i Apple Podcasts: Bibliotek → … → Følg en serie via URL, og indsæt:</p><p style="word-break:break-all;background:#0003;padding:12px">{B}/feed.xml</p><p><a style="color:#d6aa62" href="podcast://{B[8:]}/feed.xml">Åbn i Apple Podcasts</a></p></body>""")
open(D+'/robots.txt','w').write("User-agent: *\nDisallow: /\n")
