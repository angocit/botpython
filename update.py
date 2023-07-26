# coding=utf-8
import urllib.request
import urllib.parse
from database import *
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
# locale.setlocale(locale.LC_ALL, 'en_US')

def downloadimage(url,name):
    output = '/home/news.pomeraniandog.info/public_html/public/data/images'
    path = output+'/'+name
    if not os.path.exists(path):
        os.makedirs(path)
    filename = url.split('/')[-1]
    if not os.path.exists('/home/news.pomeraniandog.info/public_html/public/data/images/'+name+'/'+filename):
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url, path+'/'+filename)
    return '/public/data/images/'+name+'/'+filename
def get_famous_url(url):
    try:
        req = urllib.request.Request(url)
        req.add_header('User-agent',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5')
        page = urlopen(req)
        soup = BeautifulSoup(page.read(), "html.parser")
        main = soup.find(id="primary")
        name = main.find('h1',class_="post-title").string
# Quick info
        quickinfo = main.find('div',class_="star-quick-info")
        table_quick = quickinfo.find('table')
        ns = table_quick.findAll('tr')
        birtharr = ns[1].find('td',class_="quick-facts-td2").findAll('a')
        birthstring = ''
        for a in birtharr:
            birthstring += a.string+' '
        birth = datetime.strptime(birthstring.strip().replace(' ','-'), '%B-%d-%Y')
        professiontext = ns[5].find('td',class_="quick-facts-td2").string.strip()
        profession = id_profession(professiontext)
        biography = ''
        biography = main.find('div',class_="intro")
        h2bio = biography.find('h2')
        h2bio.replace_with()
        biography = biography.encode_contents().strip()
        biography = biography.decode()
        biography = biography.strip()
        dating = ''
        dating = main.find('div',class_="dating")
        h2d = dating.find('h2')
        h2d.replace_with()
        dating = dating.encode_contents().strip()
        dating = dating.decode()
        dating = dating.strip()
        content = main.find('div',class_="post-content").findAll('table')
        profile = content[0].findAll('tr')
        parent = ''
        father = ''
        mother = ''
        siblings = ''
        spouse =''
        children = ''
        if (profile[1].find('td',class_="quick-facts-td").string.strip())=='Father':
            father = profile[1].find('td',class_="quick-facts-td2").string.strip()
            mother = profile[2].find('td',class_="quick-facts-td2").string.strip()
            siblings = profile[3].find('td',class_="quick-facts-td2").string.strip()
            spouse = profile[4].find('td',class_="quick-facts-td2").string.strip()
            children = profile[5].find('td',class_="quick-facts-td2").string.strip()
        else:
            parent = profile[1].find('td',class_="quick-facts-td2").string.strip()
            father = profile[2].find('td',class_="quick-facts-td2").string.strip()
            mother = profile[3].find('td',class_="quick-facts-td2").string.strip()
            siblings = profile[4].find('td',class_="quick-facts-td2").string.strip()
            spouse = profile[5].find('td',class_="quick-facts-td2").string.strip()
            children = profile[6].find('td',class_="quick-facts-td2").string.strip()        
# --------------------------------------------------------  
        update_famous(
                    name,
                    birth,
                    profession,
                    biography,
                    dating,
                    parent                   
                    )
    except Exception as e:
        print(e)
def get_page_famous(url):
    f = open('logupdate.txt','w')
    f.write(str(url))
    f.close()
    req = urllib.request.Request(url)
    req.add_header('User-agent',
                   'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5')
    page = urlopen(req)
    soup = BeautifulSoup(page.read(), "html.parser")
    main = soup.find(id="primary")
    acticle = main.findAll('article',class_="post")
    for link in acticle:
        link = link.find('h2',class_="post-title").find('a')
        link = link.get('href')
        get_famous_url(link)
    nextpage = main.find('div',class_="nav-previous")
    if (nextpage.text.strip()!=''):
        nextp = nextpage.find('a').get('href')
        get_page_famous(nextp)
r = open('logupdate.txt','r')
page = r.read()
r.close() 
get_page_famous(page)