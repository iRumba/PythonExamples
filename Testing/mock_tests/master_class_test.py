from unittest.mock import Mock
from Testing.mock_tests.master_class import MasterClass
from Testing.mock_tests.nested_class import NestedClass

def test_func():
    nested_mock: NestedClass = Mock()
    nested_mock.AnyFunc.return_value = 4

    svc = MasterClass(nested_mock)

    assert svc.Func() == "4"