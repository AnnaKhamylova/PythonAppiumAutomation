import time

from selenium.webdriver.common.by import By

from page_objects.base_page import (
    BasePageObject,
)


class SavedArticlesPageObject(BasePageObject):
    def __init__(self, driver, set_up):
        super().__init__(driver=driver, set_up=set_up)

    def click_article(self, name):
        if self.platform == 'android':
            return self.wait_for_el_and_click(locator=f"xpath://*[@resource-id='org.wikipedia:id/page_list_item_title' and @text='{name}']")
        elif self.platform == 'ios':
            return self.wait_for_el_and_click(locator=f"name:'{name}'")

    def undo_saving(self, title):
        if self.platform == 'mobile_web':
            try:
                return self.wait_for_el_and_click(locator=f"xpath://li[@title='{title}']//a[contains(@class, 'watch-this-article')]")
            except:
                print('lol')

    def undo_saving_all(self):
        if self.platform == 'mobile_web':
            try:
                saved_articles = self.driver.find_elements(
                    By.XPATH,
                    '//li//a[contains(@href, "action=unwatch")]'
                )
                removed_count = 0
                for article in saved_articles:
                    try:
                        parent_li = article.find_element(By.XPATH, './ancestor::li[1]')
                        title = parent_li.get_attribute('title')
                        article.click()
                        removed_count += 1
                        print(f"Удалено из сохраненных: '{title}'")
                        time.sleep(1)
                    except Exception as e:
                        print(f"Ошибка при удалении статьи: {e}")
                        continue

                print(f"Итого удалено из сохраненных: {removed_count} статей")
                return removed_count

            except Exception as e:
                print(f"Ошибка при поиске сохраненных статей: {e}")
                return 0

    def check_saved_article_not_title(self, title):
        if self.platform == 'mobile_web':
            try:
                self.wait_for_el_present(locator=f"xpath:'//li[@title='{title}']//a[contains(@href, 'title={title}&action=unwatch')]'")
                print(f"Cтатья с title='{title}' НАЙДЕНА в списке (а не должна быть)")
                return False
            except:
                print(f"Cтатья с title='{title}' отсутствует в списке")
                return True

    def check_list_len(self, num):
        if self.platform == 'mobile_web':
            ul_element = self.wait_for_el_present(locator=f'xpath://*[@id="mw-content-text"]/ul')
            direct_children = ul_element.find_elements(By.XPATH, './*')
            count = len(direct_children)
            assert count == num, "В списке слишком мало или много статей!"

    def refresh_page(self):
        return self.driver.refresh()