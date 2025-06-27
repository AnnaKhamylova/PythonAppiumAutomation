
class MainTest():
    def get_local_number(self) -> int:
        return 14


class MainClassTest(MainTest):
    def test_get_local_number(self) -> None:
        assert MainTest().get_local_number() == 14, "Метод get_local_number() должен возвращать 14"
