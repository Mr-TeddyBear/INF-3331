import re
import requests as req

def find_emails(text):
    """
    Funtion for scraping text for emails
    """

    emails = re.findall(r'[\w\.#$%&~’*+-/=? ‘|{}]+@[\w\.#$%&~’*+-/=? ‘|{}]*?\.[a-zA-Z\.]+(?!\d)',text)
    return emails

def find_urls(text):
    """
    Function to scrape raw HTML for URLs with regualr expressions
    """
    URLs = re.findall(r"<a href=([\"'])((?:https?)://(?:www\.)?(?:[\w~\.-]+)[\w~/\.-]+)(?=\1)\1>",text)

    return [i[-1] for i in URLs]


def all_the_emails(url,depth):
    counter = 0
    emails = []
    url_scraped = []
    def recursive_url_search(list_url,counter):
        counter += 1
        for i in list_url:
            r = req.get(i).text
            tmp_emails = find_emails(r)
            url_scraped_tmp = find_urls(r)
            print (url_scraped_tmp)
            for j in tmp_emails:
                if j not in emails:
                    emails.append(j)
            if counter <= depth:
                url_scraped.append(url_scraped_tmp)
                url_scraped_tmp = set(url_scraped_tmp)
                for i in url_scraped:
                    if i in url_scraped_tmp:
                        url_scraped_tmp.remove(i)
                recursive_url_search(url_scraped_tmp,counter)

    recursive_url_search(url,counter)
    return emails


if __name__ == "__main__":
    email = (all_the_emails(['https://vg.no/'],2))
    print (email)
