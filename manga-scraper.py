import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#Funciona somente com mangas do https://mangaschan.net Exemplo: https://mangaschan.net/04092020/quanqiu-jinru-da-hongshui-shidai-evolution-in-the-flood-capitulo-1/
print("Funciona somente com mangas do https://mangaschan.net")
print("Exemplo: https://mangaschan.net/04092020/quanqiu-jinru-da-hongshui-shidai-evolution-in-the-flood-capitulo-1/")
url_first_chapter = input("Url do PRIMEIRO capítulo do manga:").strip()

chapters_list = []
pages_list = []

driver = webdriver.Firefox()
driver.get(url_first_chapter)


# Exclui todos os iframes
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
    print("Não achou select de capítulos!")
    exit()

if not select_page_element:
    print("Não achou select de páginas!")
    exit()

select_chapter_options = reversed(select_chapter_element.options)
select_pages_options = select_page_element.options

index_page = 1
index_chapter = 1
lista_capitulos = []

for cap in select_chapter_options:
    if cap.text == "Selecionar Capítulo":
        continue
    lista_capitulos.append(cap.text)

for cap in lista_capitulos:
    select_chapter_element = Select(driver.find_element(by=By.ID, value="chapter"))
    select_chapter_element.select_by_visible_text(cap)
    select_chapter_element = Select(driver.find_element(by=By.ID, value="chapter"))
    select_page_element = Select(driver.find_element(by=By.ID, value="select-paged"))
    title = driver.title.replace(" – Mangás Chan", "")

    if not select_chapter_element:
        print("Não achou select de capítulos!")
        exit()

    if not select_page_element:
        print("Não achou select de páginas!")
        exit()

    select_pages_options = select_page_element.options

    time.sleep(10)
    delete_iframes()

    for page in select_pages_options:
        select_page_element.select_by_visible_text(page.text)
        print(page.text)

        url_img = driver.find_element(by=By.CLASS_NAME, value="ts-main-image").get_attribute("src")
        if not url_img:
            print(f"Imagem não localizada, página: {page.text}")

        pages_list.append({"Página": index_page, "UrlCapitulo": url_img})

        index_page += 1

        print(f"urlImg: {url_img}")
        print(f"Selected option: {page.text}")

    index_page = 1
    chapters_list.append({title: pages_list})
    pages_list = []

with open(f"{title}.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(chapters_list, indent=4, ensure_ascii=False))

driver.quit()