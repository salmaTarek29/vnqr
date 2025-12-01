import crcmod

_crc_func = crcmod.mkCrcFun(0x11021, initCrc=0xFFFF, xorOut=0x0000, rev=False)


def get_final_crc_hex_string(hex_str: str) -> str:
    return hex_str.upper()[2:].zfill(4)


def crc_func(data: str | bytes) -> str:
    if isinstance(data, str):
        return get_final_crc_hex_string(hex(_crc_func(data.encode())).upper())

    return get_final_crc_hex_string(hex(_crc_func(data)).upper())
