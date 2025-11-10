import allure

from page_objects.base_page import (
    BasePageObject,
)

SAVE_BUTTON_ANDROID = "xpath://*[@resource-id='org.wikipedia:id/page_save' and @text='Сохранить']"
SAVE_BUTTON_IOS = 'name:Сохранить на потом'
SAVE_BUTTON_MWEB = 'xpath://*[@id="page-actions-watch"]'
ADD_TO_LIST_BUTTON_ANDROID = "xpath://*[@resource-id='org.wikipedia:id/snackbar_action' and @text='Добавить в список']"
ADD_TO_LIST_BUTTON_IOS = 'xpath://XCUIElementTypeButton[contains(@name, "добавить в список")]'
CREATE_NEW_LIST = 'name:Создать новый список'
LIST_NAME_ANDROID = "xpath://*[@resource-id='org.wikipedia:id/text_input' and @text='Название этого списка']"
LIST_NAME_IOS = 'xpath://XCUIElementTypeTextField[@value="заголовок списка для чтения"]'
CREATE_LIST_OK_ANDROID = "xpath://*[@resource-id='android:id/button1' and @text='ОК']"
CREATE_LIST_OK_IOS = 'name:Создать список для чтения'
SEE_LIST_ANDROID = "xpath://*[@resource-id='org.wikipedia:id/snackbar_action' and @text='Посмотреть список']"
SEE_LIST_IOS = 'name:Статья добавлена в «Python»'
SEARCH_BAR_MWEB_IN_ARTICLE = 'xpath://*[@id="searchIcon"]'


class ArticlePageObject(BasePageObject):
    def __init__(self, driver, set_up):
        super().__init__(driver=driver, set_up=set_up)

    def article_name(self, article_name):
        if self.platform == 'android':
            return self.wait_for_el_present(locator=SAVE_BUTTON_ANDROID)
        elif self.platform == 'ios':
            return self.wait_for_el_present(locator=f'name:{article_name}')

    def click_save_button(self):
        with allure.step("Нажимаем кнопку 'Сохранить' в статье"):
            if self.platform == 'android':
                return self.wait_for_el_and_click(locator=SAVE_BUTTON_ANDROID)
            elif self.platform == 'ios':
                return self.wait_for_el_and_click(locator=SAVE_BUTTON_IOS)
            elif self.platform == 'mobile_web':
                try:
                    watch_button = self.wait_for_el_present(locator=SAVE_BUTTON_MWEB, timeout=5)
                    button_text = watch_button.text.strip()
                    if "Не следить" in button_text:
                        with allure.step("Уже следим за страницей, пропускаем клик"):
                            pass
                    elif "Следить" in button_text:
                        with allure.step("Начинаем следить за страницей"):
                            watch_button.click()
                    else:
                        with allure.step("Текст кнопки не распознан, выполняем клик"):
                            watch_button.click()
                            return True

                except Exception as e:
                    with allure.step(f"Ошибка: {e}, используем обычный клик"):
                        return self.wait_for_el_and_click(locator=SAVE_BUTTON_MWEB)

    def click_add_to_list(self):
        if self.platform == 'android':
            return self.wait_for_el_and_click(locator=ADD_TO_LIST_BUTTON_ANDROID)
        elif self.platform == 'ios':
            return self.wait_for_el_and_click(locator=ADD_TO_LIST_BUTTON_IOS)

    def click_create_new_list(self):
        if self.platform == 'ios':
            return self.wait_for_el_and_click(locator=CREATE_NEW_LIST)

    def send_keys_list_name(self, keys):
        if self.platform == 'android':
            return self.wait_for_el_and_send_keys(locator=LIST_NAME_ANDROID, keys=keys)
        elif self.platform == 'ios':
            return self.wait_for_el_and_send_keys(locator=LIST_NAME_IOS, keys=keys)

    def click_create_list_ok(self):
        if self.platform == 'android':
            return self.wait_for_el_and_click(locator=CREATE_LIST_OK_ANDROID)
        elif self.platform == 'ios':
            return self.wait_for_el_and_click(locator=CREATE_LIST_OK_IOS)

    def click_see_list(self, name):
        if self.platform == 'android':
            return self.wait_for_el_and_click(locator=SEE_LIST_ANDROID)
        elif self.platform == 'ios':
            return self.wait_for_el_and_click(locator=f'name:Статья добавлена в «{name}»')

    def click_search_icon(self):
        if self.platform == 'mobile_web':
            return self.wait_for_el_and_click(locator=SEARCH_BAR_MWEB_IN_ARTICLE)
