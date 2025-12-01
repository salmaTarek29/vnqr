import pytest

from vnqr.vietqr import generate_vietqr_image, generate_vietqr_string


@pytest.mark.parametrize(
    "bank_bin,bank_account,total_amount,content,expected",
    [
        (
            "970425",
            "123456789",
            1000000,
            "V1TH1375842",
            "00020101021238530010A0000007270123000697042501091234567890208QRIBFTTA5303704540710000005802VN62150811V1TH137584263043158",
        ),
    ],
)
def test_generate_vietqr_string(
    bank_bin, bank_account, total_amount, content, expected
):
    assert (
        generate_vietqr_string(
            bank_bin=bank_bin,
            bank_account=bank_account,
            total_amount=total_amount,
            content=content,
        )
        == expected
    )


@pytest.mark.parametrize(
    "bank_bin,bank_account,total_amount,content,expected",
    [
        (
            "970425",
            "123456789",
            1000000,
            "V1TH1375842",
            "iVBORw0KGgoAAAANSUhEUgAAALkAAAC5AQAAAABc1qPxAAACG0lEQVR4nOWYMY7cMAxFP8cGpE6+gXyR2HOtAcY7HswC2+REqSznIvIBAkidDNjzUzipskm1YZGwESQWD5T0SUpCvGv30/vrwL/jCCJiZ2BZReplPWUROWnBhSSAe2smN7Rmwo2c1LYkSws2V6wvACywi/1wxp8deQQkVXF9+XuMX6w+hg6AFVxqIuvBT4BjxIwqcsomYkbFoganiEDS3lvg0lvgLnLWgYOHpYoQMppwzEclnTe7WOAifOahX894XbR0DjJVZCCjeQK+9OkWjVrkwEVkkNHnKl1hg5de68KBk3uwwG3g5DaYkAAGrcgl7eKYXoF+GX3uPaO8aEmty6Mvc95gAcCEBF9mNZ37R7D0hln8I6DLIuapBf+6jCgdsBw5dnbjxzN+6+hwaeWU196FZWjLJ2G0etvevEVOrl7WE16xVglYlS4cGBIA4YMF7hHRJ0ArvYJMQIEjCxwJ4QiIls5n3KLtgMVxEeHeVFEvwwVuIDmC5IbSH/VNKfIu197OqKKcUUV394NQSedHPS+SqljgHrH0qdKs5zIutnMjzJTX1tybXa1v/9HJTAAM09UzcPNaZ46D+8TVl84xFklXaDUTYCBpJgClQ0UIN5ReB14DufGA+1abkD8Lg8C7L4rp1ZunYzSBm+cTN0WdH5aHvrDBYoX1oqXzny8WZyI6vMUy56GVs+qLBbi0dsbe4lNzo1YbJf/tt8h3ijlG4Fm3XCkAAAAASUVORK5CYII=",
        ),
    ],
)
def test_generate_qr_image(bank_bin, bank_account, total_amount, content, expected):
    assert (
        generate_vietqr_image(
            bank_bin=bank_bin,
            bank_account=bank_account,
            total_amount=total_amount,
            content=content,
        )
        == expected
    )
