from typing import Tuple


class Element:
    def __init__(self, element_id: str, value: int | str):
        assert value is not None, "value must be int or str"
        if isinstance(value, str):
            assert len(value) > 0, "length of value must be greater than zero"
        self.element_id = element_id
        assert len(element_id) <= 2, "length of element id must be less than 2"
        self.value = value

    @property
    def value_length(self) -> int:
        return len(str(self.value))

    def __str__(self):
        return f"{self.element_id}{self.value_length:02}{self.value}"

    @classmethod
    def parse(cls, text: str, strict=True) -> Tuple[str, str | int]:
        element_id, value = cls.try_extract(
            element_id=text[:2], text=text, strict=strict
        )
        if element_id is not None and value is not None:
            return element_id, value
        raise ValueError(f"Invalid format! Can't parse `{text}`")

    @classmethod
    def from_text(cls, text: str, strict=True) -> "Element":
        element_id, value = cls.parse(text, strict=strict)
        return cls(element_id=element_id, value=value)

    @classmethod
    def try_extract(
        cls, element_id: str, text: str, strict=True
    ) -> Tuple[str, str | int | None]:
        try:
            assert element_id.isdigit(), "element_id must be digits"
            length = int(text[2:4])
            value = text[4:]
            if strict:
                assert length == len(value), "length not match value length!"

            return element_id, value[:length]
        except:
            return element_id, None

    def __eq__(self, other: "Element"):
        return (
            isinstance(self, other.__class__)
            and (self.element_id == other.element_id)
            and (str(self.value) == str(other.value))
        )

    def tuple(self):
        return (
            self.element_id,
            self.value,
        )
