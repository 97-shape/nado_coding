import requests
import re
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_sug.asiw&fbm=1&acr=1&acq=%EB%8C%80%EA%B5%AC&qdt=0&ie=utf8&acir=1&query=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    cast = soup.find("p", attrs={"class": "summary"}).get_text()
    cast = cast[-3:-1] + ", " + cast[:-5]
    curr_temp = soup.find("div", attrs={"class": "temperature_text"}).get_text().replace("°", "")[6:]
    min_temp = soup.find("span", attrs={"class": "lowest"}).get_text().replace("°", "")[4:]
    max_temp = soup.find("span", attrs={"class": "highest"}).get_text().replace("°", "")[4:]
    rain_rates = []
    for idx, rain_rate in enumerate(soup.find_all("span", attrs={"class": "rainfall"})):
        if idx >= 2:
            break
        rain_rates.append(rain_rate.get_text().replace("%", ""))

    # 미세먼지
    url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&pkid=227&qvt=0&query=%EB%8C%80%EA%B5%AC%EA%B4%91%EC%97%AD%EC%8B%9C%20%EC%A4%91%EA%B5%AC%20%EB%8F%99%EC%9D%B8%EB%8F%991%EA%B0%80%20%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80"
    soup = create_soup(url)

    micro_dusts = soup.find_all("span", attrs={"class": "num _value"})[:2]

    # 출력
    print(cast)
    print("현재 : {} (최저 {} / 최고 {})".format(curr_temp, min_temp, max_temp))
    print("강수량 : (오전 {} / 오후 {})".format(rain_rates[0], rain_rates[1]))
    print()
    print("미세먼지 {}".format(micro_dusts[0].get_text()))
    print("초 미세먼지 {}".format(micro_dusts[1].get_text()))
    print("\n ------------------------------------------------------------------------------------------ \n ")

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/"
    soup = create_soup(url)
    news_list = soup.find_all("div", attrs={"class": "cjs_journal_wrap _item_contents"}, limit=3)  # 3개 까지
    for idx, news in enumerate(news_list):
        title = news.find("div", attrs={"class": "cjs_t"}).get_text()
        link = news.find("a")["href"]
        print("{}. {}".format(idx+1, title))
        print("  (링크 : {})".format(link))
    print("\n ------------------------------------------------------------------------------------------ \n ")

def scrape_it_news():
    print("[it 뉴스]")
    url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
    soup = create_soup(url)
    it_news_list = soup.find_all("a", attrs={"class": "cluster_text_headline nclicks(cls_sci.clsart)"}, limit=3)
    for idx, it_news in enumerate(it_news_list):
        title = it_news.get_text()
        link = it_news["href"]
        print("{}. {}".format(idx + 1, title))
        print("  (링크 : {})".format(link))
    print("\n ------------------------------------------------------------------------------------------ \n ")

def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id": re.compile("^conv_kor_t")})
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())
    print()
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())

if __name__ == "__main__":
    scrape_weather()  # 오늘의 날씨 정보 가져오기
    scrape_headline_news()  # 헤드라인 가져오기
    scrape_it_news()  # it 뉴스 가져오기
    scrape_english()  # 오늘의 영어 회화 가져오기