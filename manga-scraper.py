import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Works just with mangas from https://mangaschan.net. Example:
# https://mangaschan.net/04092020/quanqiu-jinru-da-hongshui-shidai-evolution-in-the-flood-capitulo-1/
print("Works just with mangas from https://mangaschan.net")
print("Example: https://mangaschan.net/04092020/quanqiu-jinru-da-hongshui-shidai-evolution-in-the-flood-capitulo-1/")
url_first_chapter = input("Url of the FIRST chapter of the manga:").strip()

chapters_list = []
pages_list = []

driver = webdriver.Firefox()
driver.get(url_first_chapter)


# Delete all the iframes
def delete_iframes():
    driver.execute_script("""
    var iframes = document.getElementsByTagName('iframe');
    while (iframes.length > 0) {
        iframes[0].parentNode.removeChild(iframes[0]);
    }
    """)


time.sleep(10)
title = driver.title.replace(" – Mangás Chan", "")
delete_iframes()

select_chapter_element = Select(driver.find_element(by=By.ID, value="chapter"))
select_page_element = Select(driver.find_element(by=By.ID, value="select-paged"))

if not select_chapter_element:
    print("Don't find the chapter's select!")
    exit()

if not select_page_element:
    print("Don't find the page's select!")
    exit()

select_chapter_options = reversed(select_chapter_element.options)
select_pages_options = select_page_element.options

index_page = 1
index_chapter = 1
list_chapters_text = []

for cap in select_chapter_options:
    if cap.text == "Selecionar Capítulo":
        continue
    list_chapters_text.append(cap.text)

for cap in list_chapters_text:
    select_chapter_element = Select(driver.find_element(by=By.ID, value="chapter"))

    select_chapter_element.select_by_visible_text(cap)

    select_chapter_element = Select(driver.find_element(by=By.ID, value="chapter"))

    select_page_element = Select(driver.find_element(by=By.ID, value="select-paged"))

    title = driver.title.replace(" – Mangás Chan", "")

    if not select_chapter_element:
        print("Don't find the chapter's select!")
        exit()

    if not select_page_element:
        print("Don't find the page's select!")
        exit()

    select_pages_options = select_page_element.options

    time.sleep(10)
    delete_iframes()

    for page in select_pages_options:
        select_page_element.select_by_visible_text(page.text)
        print(page.text)

        url_img = driver.find_element(by=By.CLASS_NAME, value="ts-main-image").get_attribute("src")
        if not url_img:
            print(f"Image does not exist!, page: {page.text}")

        pages_list.append({"Page": index_page, "ChapterUrl": url_img})

        index_page += 1

        print(f"urlImg: {url_img}")
        print(f"Selected option: {page.text}")

    index_page = 1
    chapters_list.append({title: pages_list})
    pages_list = []

with open(f"{title}.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(chapters_list, indent=4, ensure_ascii=False))

driver.quit()
