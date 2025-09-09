from page_objects.base_page import (
    BasePageObject,
)

FIRST_PAGE_IOS = 'name:Свободная энциклопедия'
SECOND_PAGE_IOS = 'name:Новые способы изучения'
THIRD_PAGE_IOS = 'name:Искать на более чем 300 языках'
FOURTH_PAGE_IOS = 'name:Помогите сделать это приложение лучше'
PAGE_ANDROID = "id:org.wikipedia:id/primaryTextView"
SKIP_BUTTON_IOS = 'name:Пропустить'
SKIP_BUTTON_ANDROID = 'xpath://*[contains(@resource-id, "org.wikipedia:id/fragment_onboarding_skip_button")]'
REJECT_BUTTON_ANDROID = 'xpath://android.widget.Button[@resource-id="org.wikipedia:id/rejectButton"]'
CONTINUE_BUTTON_IOS = 'name:Начать'


class WelcomePageObject(BasePageObject):
    def __init__(self, driver, set_up):
        super().__init__(driver=driver, set_up=set_up)

    def first_page(self):
        if self.platform == 'android':
            return self.assert_element_has_text(locator=PAGE_ANDROID, text="Свободная энциклопедия\n…более, чем на 300 языках")
        elif self.platform == 'ios':
            return self.wait_for_el_present(locator=FIRST_PAGE_IOS)

    def second_page(self):
        if self.platform == 'android':
            return self.assert_element_has_text(locator=PAGE_ANDROID, text="Новые способы исследований")
        elif self.platform == 'ios':
            return self.wait_for_el_present(locator=SECOND_PAGE_IOS)

    def third_page(self):
        if self.platform == 'android':
            return self.assert_element_has_text(locator=PAGE_ANDROID, text="Списки для чтения с синхронизацией")
        elif self.platform == 'ios':
            return self.wait_for_el_present(locator=THIRD_PAGE_IOS)

    def fourth_page(self):
        if self.platform == 'android':
            return self.assert_element_has_text(locator=PAGE_ANDROID, text="Отправлять отчёты об использовании")
        elif self.platform == 'ios':
            return self.wait_for_el_present(locator=FOURTH_PAGE_IOS)

    def click_skip_button(self):
        if self.platform == 'android':
            return self.wait_for_el_and_click(locator=SKIP_BUTTON_ANDROID)
        elif self.platform == 'ios':
            return self.wait_for_el_and_click(locator=SKIP_BUTTON_IOS)

    def click_reject_button(self):
        if self.platform == 'android':
            return self.wait_for_el_and_click(locator=REJECT_BUTTON_ANDROID)
        elif self.platform == 'ios':
            return self.wait_for_el_and_click(locator=CONTINUE_BUTTON_IOS)




