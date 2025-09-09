from page_objects.base_page import (
    BasePageObject,
)


class ArticlePageObject(BasePageObject):

    def article_name(self, article_name):
        return self.wait_for_el_and_click(
            by="xpath", locator=article_name
        )
