from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class Firefox:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def __del__(self):
        self.driver.close()
        self.driver.quit()

    def get(self, url):
        self.driver.get(url)

    @staticmethod
    def wait_execute(func, arg, count):
        for _ in range(count):
            try:
                result = func(By.XPATH, arg)
            except:
                pass
            else:
                if result:
                    return result
            print(arg)
            time.sleep(1)
        raise TimeoutError("Wait element timeout")

    def wait_elements(self, xpath, count=10):
        return self.wait_execute(self.driver.find_elements, xpath, count)

    def wait_element(self, xpath, count=10):
        return self.wait_execute(self.driver.find_element, xpath, count)

    def get_last_news_yandex(self) -> list:
        """
        :return: Last five news from yandex.ru
        """
        xpaths = {
            'news': "//a[@data-id='news']",
            'headers': "//div[@class='mg-grid__row mg-grid__row_gap_8 news-top-flexible-stories news-app__top']/div//a[@class='mg-card__link']"
        }

        self.get("https://yandex.ru/")                                  # open yandex.ru
        self.wait_element(xpaths['news']).click()                       # click to 'news'

        self.driver.close()                                             # close yandex tab
        self.driver.switch_to.window(self.driver.window_handles[0])     # select yandex news tab

        elements = self.wait_elements(xpaths['headers'])                # get HTML news
        result = []

        for el in elements:
            result.append(el.text)                                      # get text from HTML news

        return result

ff = Firefox()
print(ff.get_last_news_yandex())