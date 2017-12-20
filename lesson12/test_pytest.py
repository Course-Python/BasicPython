import pytest

from main import args_sum


class TestArgsSumPytest:
    def test_1_2_3(self):
        assert args_sum(1, 2, 3) == 6
 
    def test_1(self):
        assert args_sum(1) == 1
    
    def test_exception(self):
        with pytest.raises(TypeError):
            args_sum('a', 2, 'c')
