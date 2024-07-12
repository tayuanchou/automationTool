from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time
import requests

def download_publications(professor):
    driver = webdriver.Chrome()
    driver.get("https://www.most.gov.tw/")
    search = driver.find_element_by_link_text("研究人才查詢")
    search.click()

    driver.switch_to.window(driver.window_handles[1])
    public = driver.find_element_by_name("organ_1")
    public.click()
    school = Select(driver.find_element_by_name("organ_2_1"))
    school.select_by_value("FA04")
    time.sleep(3)
    Econ = Select(driver.find_element_by_name("organ_3_1"))
    Econ.select_by_value("FA04E021")
    link = driver.find_element_by_name("send")
    link.click()
    page = Select(driver.find_element_by_xpath('//*[@id="zone.content11"]/div/div[1]/select'))
    page.select_by_value("100")
    time.sleep(3)
    prof = driver.find_element_by_partial_link_text(professor)
    prof.click()
    publications = driver.find_element_by_partial_link_text("著作目錄")
    publications.click()

    soup = BeautifulSoup(driver.page_source, "html.parser")
    rows = soup.find("div", "c30Tblist2").find_all("tr")
    articles = []
    for row in rows:
        if row.find("td"):
            tds = row.find_all("td")
            author = tds[3].text.strip()
            year = tds[0].text[0:4]
            title = tds[2].text.strip()
            journal = tds[4].text.strip()
            type = tds[1].text.strip()
            articles.append({
                'author': author,
                "year": year,
                "title": title,
                "journal": journal,
                "type": type
            })
    articles_2011 = []
    for article in articles:
        if int(article["year"]) > 2010:
            articles_2011.append({
                'author': article["author"],
                "year": article["year"],
                "title": article["title"],
                "journal": article["journal"],
                "type": article["type"]
            })
    driver.quit()
    return articles, articles_2011


if __name__ == "__main__":
    profs = ["趙相科",
             "莊慧玲",
             "朱筱蕾",
             "周嗣文",
             "周瑞賢",
             "祁玉蘭",
             "馮炳萱",
             "黃朝熙",
             "黃賀寶",
             "郭俊宏",
             "李翎帆",
             "李宜",
             "廖肇寧",
             "林世昌",
             "林靜儀",
             "盧姝璇",
             "劉瑞華",
             "冼芻蕘",
             "唐震宏",
             "蔡璧涵",
             "王惠貞",
             "吳世英",
             "余朝恩"]
    for prof in profs:
        print("name = ", prof)
        articles = download_publications(prof)
        print("共", len(articles[1]), "篇文章")
        periodicals = []
        for article in articles[1]:
            if article["type"] == "期刊論文":
                periodicals.append({
                    'author': article["author"],
                    "year": article["year"],
                    "title": article["title"],
                    "journal": article["journal"]
            })
        if periodicals:
            print("一.期刊論文")
        for periodical in periodicals:
            print(periodical["author"] + ". " + periodical["year"] + ". \"" + periodical["title"] + "\" " + periodical["journal"])

        special_issues = []
        for article in articles[1]:
            if article["type"] == "專書論文":
                special_issues.append({
                    'author': article["author"],
                    "year": article["year"],
                    "title": article["title"],
                    "journal": article["journal"]
                })
        if special_issues:
            print("二.專書論文")
        for special_issue in special_issues:
            print(special_issue["author"] + ". " + special_issue["year"] + ". \"" + special_issue["title"] + "\" " + special_issue["journal"])

        books = []
        for article in articles[1]:
            if article["type"] == "專書":
                books.append({
                    'author': article["author"],
                    "year": article["year"],
                    "title": article["title"],
                    "journal": article["journal"]
                })
        if books:
            print("三.專書")
        for book in books:
            print(book["author"] + ". " + book["year"] + ". \"" + book["title"] + "\" " + book["journal"])

        others = []
        for article in articles[1]:
            if article["type"] == "其他":
                others.append({
                    'author': article["author"],
                    "year": article["year"],
                    "title": article["title"],
                    "journal": article["journal"]
                })
        if others:
            print("四.其他")
        for other in others:
            print(other["author"] + ". " + other["year"] + ". \"" + other["title"] + "\" " + other["journal"])