import time

from page_objects.base_page import (
    BasePageObject,
)

SAVE_BUTTON_ANDROID = "xpath://*[@resource-id='org.wikipedia:id/page_save' and @text='Сохранить']"
SAVE_BUTTON_IOS = 'name:Сохранить на потом'
ADD_TO_LIST_BUTTON_ANDROID = "xpath://*[@resource-id='org.wikipedia:id/snackbar_action' and @text='Добавить в список']"
ADD_TO_LIST_BUTTON_IOS = 'xpath://XCUIElementTypeButton[contains(@name, "добавить в список")]'
CREATE_NEW_LIST = 'name:Создать новый список'
LIST_NAME_ANDROID = "xpath://*[@resource-id='org.wikipedia:id/text_input' and @text='Название этого списка']"
LIST_NAME_IOS = 'xpath://XCUIElementTypeTextField[@value="заголовок списка для чтения"]'
CREATE_LIST_OK_ANDROID = "xpath://*[@resource-id='android:id/button1' and @text='ОК']"
CREATE_LIST_OK_IOS = 'name:Создать список для чтения'
SEE_LIST_ANDROID = "xpath://*[@resource-id='org.wikipedia:id/snackbar_action' and @text='Посмотреть список']"
SEE_LIST_IOS = 'name:Статья добавлена в «Python»'


class ArticlePageObject(BasePageObject):
    def __init__(self, driver, set_up):
        super().__init__(driver=driver, set_up=set_up)

    def article_name(self, article_name):
        if self.platform == 'android':
            return self.wait_for_el_present(locator=SAVE_BUTTON_ANDROID)
        elif self.platform == 'ios':
            return self.wait_for_el_present(locator=f'name:{article_name}')

    def click_save_button(self):
        if self.platform == 'android':
            return self.wait_for_el_and_click(locator=SAVE_BUTTON_ANDROID)
        elif self.platform == 'ios':
            return self.wait_for_el_and_click(locator=SAVE_BUTTON_IOS)

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
