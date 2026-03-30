"""Tests for strutils.core."""

from strutils.core import camel_to_snake, slugify, snake_to_camel, truncate


class TestSlugify:
    def test_basic(self):
        assert slugify("Hello World") == "hello-world"

    def test_unicode(self):
        assert slugify("Ångström café") == "angstrom-cafe"

    def test_custom_separator(self):
        assert slugify("one two three", separator="_") == "one_two_three"


class TestTruncate:
    def test_short_string(self):
        assert truncate("hi", 10) == "hi"

    def test_long_string(self):
        result = truncate("a" * 100, 20)
        assert len(result) <= 20
        assert result.endswith("…")


class TestCamelToSnake:
    def test_simple(self):
        assert camel_to_snake("CamelCase") == "camel_case"

    def test_acronym(self):
        assert camel_to_snake("HTTPResponse") == "http_response"


class TestSnakeToCamel:
    def test_upper(self):
        assert snake_to_camel("hello_world") == "HelloWorld"

    def test_lower(self):
        assert snake_to_camel("hello_world", upper=False) == "helloWorld"
