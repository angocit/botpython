# coding=utf-8
import urllib.request
import urllib.parse
from database import *
import requests
from sock import *
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
        prox = Proxies()  
        sock = prox.proxieran()
        print(sock)
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
        r = requests.get(url, headers=headers,timeout=5,proxies=sock)
        soup = BeautifulSoup(r.text, "html.parser")
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
        place_of_birth = ns[3].find('td',class_="quick-facts-td2").text.strip()
        countrytext = ns[4].find('td',class_="quick-facts-td2").text.strip()
        country = id_country(countrytext)
        professiontext = ns[5].find('td',class_="quick-facts-td2").string.strip()
        profession = id_profession(professiontext)
        horoscope = ns[6].find('td',class_="quick-facts-td2").text.strip()
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
        print(horoscope)
# ----------------------------------------------------------
        content = main.find('div',class_="post-content").findAll('table')
# Short Profile
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
# Net Worth
        net = content[1].findAll('tr')
        net_worth = net[1].find('td',class_="quick-facts-td2").string.strip()
        salary = net[2].find('td',class_="quick-facts-td2").string.strip()
        source_of_income = net[3].find('td',class_="quick-facts-td2").string.strip()
        cars = net[4].find('td',class_="quick-facts-td2").string.strip()
        house = net[5].find('td',class_="quick-facts-td2").string.strip()
        print(house)
# ---------------------------------------------------------- 
# BODY STATS
        body = content[2].findAll('tr')
        height = body[1].find('td',class_="quick-facts-td2").string.strip()   
        weight = body[2].find('td',class_="quick-facts-td2").string.strip()   
        body_measurements = body[3].find('td',class_="quick-facts-td2").string.strip()   
        eye_color = body[4].find('td',class_="quick-facts-td2").string.strip()   
        hair_color = body[5].find('td',class_="quick-facts-td2").string.strip()   
        shoe_size = body[6].find('td',class_="quick-facts-td2").string.strip() 
        print(shoe_size)
# ---------------------------------------------------------------------------   
        image = ''
        img = main.find('img',class_='wp-post-image').get('src')
        if (img!='/wp-content/uploads/2021/01/no-img-1.png'):
            image = downloadimage(img,'famous')
        insert_famous(
                    name,
                    birth,                    
                    place_of_birth,
                    country,
                    profession,
                    horoscope,
                    biography,
                    dating,
                    parent,
                    father,
                    mother,
                    siblings,
                    spouse,
                    children,
                    net_worth,
                    salary,
                    source_of_income,
                    cars,
                    house,
                    height,
                    weight,
                    body_measurements,
                    eye_color,
                    hair_color,
                    shoe_size,
                    image
                    )
    except Exception as e:
        print(e)
def get_page_famous(url):
    f = open('log.txt','w')
    f.write(str(url))
    f.close()
    prox = Proxies()  
    sock = prox.proxieran()
    print(sock)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    r = requests.get(url, headers=headers,timeout=5,proxies=sock)
    soup = BeautifulSoup(r.text, "html.parser")
    main = soup.find(id="primary")
    acticle = main.findAll('article',class_="post")
    for link in acticle:        
        link = link.find('h2',class_="post-title").find('a')
        link = link.get('href')
        print(link)
        get_famous_url(link)
    nextpage = main.find('div',class_="nav-previous")
    if (nextpage.text.strip()!=''):
        nextp = nextpage.find('a').get('href')
        get_page_famous(nextp)
r = open('log.txt','r')
page = r.read()
r.close() 
print(page)
get_page_famous(page)