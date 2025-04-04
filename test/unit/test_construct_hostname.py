#!/usr/bin/env python
from __future__ import annotations

from snowflake.connector.util_text import construct_hostname


def test_construct_hostname_basic():
    assert (
        construct_hostname("eu-central-1", "account1")
        == "account1.eu-central-1.snowflakecomputing.com"
    )

    assert construct_hostname("", "account1") == "account1.snowflakecomputing.com"

    assert construct_hostname(None, "account1") == "account1.snowflakecomputing.com"

    assert (
        construct_hostname("as-east-3", "account1")
        == "account1.as-east-3.snowflakecomputing.com"
    )

    assert (
        construct_hostname("as-east-3", "account1.eu-central-1")
        == "account1.as-east-3.snowflakecomputing.com"
    )

    assert (
        construct_hostname("", "account1.eu-central-1")
        == "account1.eu-central-1.snowflakecomputing.com"
    )

    assert (
        construct_hostname(None, "account1.eu-central-1")
        == "account1.eu-central-1.snowflakecomputing.com"
    )

    assert (
        construct_hostname(None, "account1-jkabfvdjisoa778wqfgeruishafeuw89q.global")
        == "account1-jkabfvdjisoa778wqfgeruishafeuw89q.global.snowflakecomputing.com"
    )

    assert (
        construct_hostname("cn-central-1", "account1")
        == "account1.cn-central-1.snowflakecomputing.cn"
    )

    assert (
        construct_hostname(None, "account1.cn-central-1")
        == "account1.cn-central-1.snowflakecomputing.cn"
    )

    assert (
        construct_hostname("", "account1.cn-central-1")
        == "account1.cn-central-1.snowflakecomputing.cn"
    )

    assert (
        construct_hostname("CN-central-1", "account1")
        == "account1.CN-central-1.snowflakecomputing.cn"
    )
