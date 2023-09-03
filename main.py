from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Запускаємо веб-драйвер (наприклад, Chrome)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)


# Відкриваємо сторінку
driver.get("https://coinmarketcap.com/ru/")
time.sleep(2)

# Змінюємо мову на англійську
element_buttom = driver.find_element(By.CLASS_NAME, 'cmc-popover__trigger')
element_buttom.click()
time.sleep(2)

change = driver.find_element(By.XPATH, "//a[text()='English']")
change.click()
time.sleep(2)

# Прокручуємо сторінку до кінця
for _ in range(15):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(2)  # Зачекайте 2 секунди для завантаження даних

# Отримуємо HTML-код сторінки після прокрутки
page_source = driver.page_source

# Закриваємо веб-драйвер
driver.quit()

# Розпарсуємо отриманий HTML-код за допомогою BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Знайти таблицю з інформацією про криптовалюти
table = soup.find("table", class_="cmc-table")

# Витягти дані з таблиці
rows = table.find_all("tr")

# Вивести інформацію про криптовалюти
for row in rows:
    # Витягти назву криптовалюти
    name = row.find("p", class_="sc-4984dd93-0 kKpPOn")

    # Витягти ринкову капіталізацію криптовалюти
    market_cap = row.find("span", class_="sc-f8982b1f-1 bOsKfy")

    # Вивести інформацію про криптовалюту (текстовий вміст)
    if name and market_cap:
        print(f"Назва: {name.text}")
        print(f"Ринкова капіталізація: {market_cap.text}")