import pytest
from unittest.mock import patch
from what_is_year_now import what_is_year_now
import urllib.request
import json


class TestWhatIsYearNow:
    def test_correct_year(self):
        actual = what_is_year_now()
        expected = 2020
        assert actual == expected

    def test_wrong_year(self):
        actual = what_is_year_now()
        expected = 2019
        with pytest.raises(AssertionError):
            assert actual == expected

    def test_bad_answer(self):
        with patch(
                'what_is_year_now.what_is_year_now',
                return_value=1,
        ) as what_is_year_now:
            actual = what_is_year_now()
            expected = 2020
            with pytest.raises(AssertionError):
                assert actual == expected

    def test_DMY_year(self):
        expected = 2020
        # Намеренно оставляю не по пепу, можно было сохранить в файл и вызывать
        # Но не сохраняю, чтобы лишней путаницы не добавлять
        respstring = '{"$id": "1", "currentDateTime": "01.03.2020T11:33Z", "utcOffset": "00:00:00", "isDayLightSavingsTime": "False", "dayOfTheWeek": "Thursday", "timeZoneName": "UTC", "currentFileTime": 132508640396480844, "ordinalDate": "2020-331", "serviceResponse": "None"}'
        resp_json = json.loads(respstring)
        with patch.object(
                urllib.request,
                'urlopen',
                return_value=respstring,
        ) as urllib.request.urlopen:
            with patch.object(
                    json,
                    'load',
                    return_value=resp_json,
            ) as urllib.request.urlopen:
                actual = what_is_year_now()
                assert actual == expected

    def test_invalid_format_year(self):
        # Намеренно оставляю не по пепу, можно было сохранить в файл и вызывать
        # Но не сохраняю, чтобы лишней путаницы не добавлять
        respstring = '{"$id": "1", "currentDateTime": "124rbsd", "utcOffset": "00:00:00", "isDayLightSavingsTime": "False", "dayOfTheWeek": "Thursday", "timeZoneName": "UTC", "currentFileTime": 132508640396480844, "ordinalDate": "2020-331", "serviceResponse": "None"}'
        resp_json = json.loads(respstring)
        with patch.object(
                urllib.request,
                'urlopen',
                return_value=respstring,
        ) as urllib.request.urlopen:
            with patch.object(
                    json,
                    'load',
                    return_value=resp_json,
            ) as urllib.request.urlopen:
                with pytest.raises(ValueError):
                    assert what_is_year_now()
