
class MainClass():
    __class_number = 20

    def get_local_number(self) -> int:
        return 14

    def get_class_number(self):
        return self.__class_number


class MainClassTest(MainClass):
    def test_get_local_number(self) -> None:
        assert MainClass.get_local_number() == 14, "Метод get_local_number() должен возвращать 14"

    def testGetClassNumber(self):
        assert MainClass.get_class_number() > 45, "Метод get_class_number() должен возвращать число больше 45"
