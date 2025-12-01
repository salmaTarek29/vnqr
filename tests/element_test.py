import pytest

from vnqr.element import Element


@pytest.mark.parametrize(
    "element_id,value,expected",
    [
        (
            "00",
            "01",
            "000201",
        ),
        (
            "00",
            0,
            "00010",
        ),
        (
            "01",
            "12",
            "010212",
        ),
        (
            "38",
            "0010A0000007270123000697042501091234567890208QRIBFTTA",
            "38530010A0000007270123000697042501091234567890208QRIBFTTA",
        ),
    ],
)
def test_element_init_success(element_id, value, expected):
    element = Element(element_id=element_id, value=value)

    assert str(element) == expected


@pytest.mark.parametrize(
    "element_id,value",
    [
        (
            "00",
            "",
        ),
        (
            "01",
            None,
        ),
    ],
)
def test_element_init_fail(element_id, value):
    with pytest.raises(AssertionError) as e:
        Element(element_id=element_id, value=value)


@pytest.mark.parametrize(
    "text,expect_element_id,expect_value",
    [
        (
            "000201",
            "00",
            "01",
        ),
        (
            "010212",
            "01",
            "12",
        ),
        (
            "38530010A0000007270123000697042501091234567890208QRIBFTTA",
            "38",
            "0010A0000007270123000697042501091234567890208QRIBFTTA",
        ),
    ],
)
def test_element_parse_success(text, expect_element_id, expect_value):
    element = Element.from_text(text)

    assert str(element) == text
    assert element.element_id == expect_element_id
    assert element.value == str(expect_value)


@pytest.mark.parametrize(
    "text",
    [
        (" 1232",),
        ("000301",),
        ("010512",),
        ("38010010A0000007270123000697042501091234567890208QRIBFTTA",),
    ],
)
def test_element_parse_failed(text):
    with pytest.raises(ValueError):
        Element.from_text(text)


@pytest.mark.parametrize(
    "text,expected",
    [
        ("00030123", ("00", "012")),
        ("01051233222", ("01", "12332")),
    ],
)
def test_element_parse_success_no_strict(text, expected):
    element = Element.from_text(text, strict=False)
    assert element.element_id == expected[0]
    assert str(element.value) == str(expected[1])
