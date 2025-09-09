
class MainClass():
    __class_number = 20
    __class_string = 'Hello, world'

    def get_class_string(self) -> str:
        return self.__class_string

    def get_local_number(self) -> int:
        return 14

    def get_class_number(self) -> int:
        return self.__class_number


class MainClassTest(MainClass):
    def test_get_local_number(self) -> None:
        assert MainClass.get_local_number() == 14, "Метод get_local_number() должен возвращать 14"

    def test_get_class_number(self) -> None:
        assert MainClass.get_class_number() > 45, "Метод get_class_number() должен возвращать число больше 45"

    def test_get_class_string(self) -> None:
        assert MainClass.get_class_string().count('hello') or MainClassTest.get_class_string().count('Hello'),\
            "Метод get_class_string() должен содержать строку hello или Hello"