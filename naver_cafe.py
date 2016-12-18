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

def get_board_info(url):
    if not url:
        url = "http://cafe.naver.com/ArticleList.nhn?search.clubid=28506240&search.menuid=11&search.boardtype=L"
    html = urllib2.urlopen(url)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    output = soup.findAll("td", {'class':'on'})
    output = str(output[0]).split(";")

    for l in output:
        if "totalCount" in l:
            articlec = int(l.split("=")[1].replace("&amp",""))
            if articlec%50:
                return {"count":{"article":articlec, "board":articlec/50+1}, "request_url":url}
            else:
                return {"count":{"article":articlec, "board":articlec/50}, "request_url":url}
            break

def make_board_url(info):
    board_count = info["count"]["board"]
    artc_count = info["count"]["article"]
    urlform = info["request_url"]
    urlform += "&search.questionTab=A&search.marketBoardTab=D&search.specialmenutype=&search.totalCount="+str(artc_count)+"&userDisplay=50"
    url = list()
    for l in range(1, board_count+1):
        url.append(urlform+"&search.page="+str(l))
    return url

def get_data_from_board(url):
    html = urllib2.urlopen(url)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    output = soup.findAll("span", {"class":"aaa"})
    return output
    
