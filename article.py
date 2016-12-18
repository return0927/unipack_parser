import urllib2
import bs4

def get_board_link():
    url = "http://cafe.naver.com/ArticleList.nhn?search.clubid=28506240&search.menuid=11&search.boardtype=L"
    html = urllib2.urlopen(url)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    output = soup.findAll("span", {'class':'aaa'})
    notice = len(soup.findAll("img", {'class':'ico-list-notice'}))

    articles = list()

    for l in range(notice, len(output)):
        for n in str(output[l]).split("\n"):
            if 'a class="m-tcol-c" href=' in n:
                articles.append("http://cafe.naver.com" + n.split("href=")[1].split('"')[1])
    return articles

def get_article_count():
    
    url = "http://cafe.naver.com/ArticleList.nhn?search.clubid=28506240&search.menuid=11&search.boardtype=L"
    html = urllib2.urlopen(url)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    output = soup.findAll("td", {'class':'on'})
    output = str(output[0]).split(";")

    for l in output:
        if "totalCount" in l:
            return (l.split("=")[1].replace("&amp",""))
            break
