import pytest

from vnqr.vietqr import generate_vietqr_string, generate_vietqr_image


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
            "iVBORw0KGgoAAAANSUhEUgAAALkAAAC5AQAAAABc1qPxAAABrElEQVR4nN2XMa6DMBBEF6Wg5Ai+SbhYJCLlYnATH8GlC8T+mbH5X/lK"
            "yxZxgQTPheWZnV3MP6+nfT9YzWzc3HM1u+U6FLwPUQDfHIBbJr6WxX0LA8XSuE671TvAuJWHjcHAHlZnf2Wb48EBABV2eCMWUI/Vlowt"
            "t/xfqItBc2J5pPPxbtFrQVvl5nj1zIJ4K85rAU04UgVKkUDhiCEK8EAUJcMRlupcljx6HIAJ77Y4ggensumZPAys08ur4V7a5dAM3YkBg"
            "I/fO0jY4kiBKOAIAFfgEagk6xAFjumVx34vnrnPmh4RQJlDitBXDT4DgZxohuBRIR4IwU4DwIH2rjZr7PGohaWbIQL0oJUeand/elwPqD5"
            "9IDO4Uu+MvuvBxjuQD2RC2SIOqL03/2HOmVvvCQIMAFiPUjD5NeF5GFDcoBBlBp0qDnC6Mc51zglPQ8c5flwPtDTn9NzdUxzQN0yWSdHHh"
            "tsbUATokyUK8W4yIe0YBs6/CSUwD5n+/WZcDY7WbPbE0D+LMwxAjz5j0pMeBqQHGr1Sr/WAOQrIiThQasFzaMaMAp/X94Mf/XaONpKl6i"
            "MAAAAASUVORK5CYII=",
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
