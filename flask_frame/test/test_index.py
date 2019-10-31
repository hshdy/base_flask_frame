#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
--------------------------------------------
# Author: hsh
# Name: test_index
# DATE: 19-10-31-下午2:16
--------------------------------------------
"""
import pytest
import requests


@pytest.fixture()
def requests_api():
    url = "http://192.168.1.188:55455/"
    respnse = requests.get(url)

    return respnse


class TestIndex:
    def test_index_first_method(self, requests_api):
        status_code = requests_api.status_code
        assert status_code == 200

        data = requests_api.json()
        status = data.get("status")
        assert status == "success"

    def test_index_second_method(self):
        url = "http://192.168.1.188:55455/"
        respnse = requests.get(url)

        status_code = respnse.status_code
        assert status_code == 200

        data = respnse.json()
        status = data.get("status")
        assert status == "success"
