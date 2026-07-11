from nested_class import NestedClass

class MasterClass:
    nested_class: NestedClass

    def __init__(self, nested_class: NestedClass):
        self.nested_class = nested_class
        pass

    def Func(self) -> str:
        return str(self.nested_class.AnyFunc())