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
