import pytest
from one_hot_encoder import fit_transform


class TestOneHotEncoder:
    def test_one_element(self):
        element = ['Moscow']
        actual = fit_transform(*element)
        expected = [('Moscow', [1])]

        assert actual == expected

    def test_many_elements(self):
        elements = ['Food', 'Drink', 'Potato']
        actual = fit_transform(*elements)
        expected = [
            ('Food', [0, 0, 1]),
            ('Drink', [0, 1, 0]),
            ('Potato', [1, 0, 0]),
        ]

        assert actual == expected

    def test_same_elements(self):
        elements = ['Food', 'Food', 'Food']
        actual = fit_transform(*elements)
        expected = [
            ('Food', [1]),
            ('Food', [1]),
            ('Food', [1]),
        ]

        assert actual == expected

    def test_other_words_presense(self):
        elements = ['Apple', 'Orange']
        actual = fit_transform(*elements)
        expected = [
            ('Apple', [0, 1]),
            ('Orange', [1, 0]),
        ]
        names = [element[0] for element in actual]
        other_name = 'Banana'

        assert other_name not in names
        assert actual == expected

    def test_bad_input(self):
        elements = 123
        with pytest.raises(TypeError):
            assert fit_transform(elements)

    def test_empty_input(self):
        with pytest.raises(TypeError):
            assert fit_transform()
