class NormalizerPhone:
    @staticmethod
    def normalize_phone(phone: str) -> str:
        """
        Normalize Iranian phone numbers.

        Examples:
            +989121234567 -> 09121234567
            989121234567  -> 09121234567
            0912 123 4567 -> 09121234567
        """
        phone = phone.replace(" ", "").replace("-", "")

        if phone.startswith("+98"):
            phone = "0" + phone[3:]

        elif phone.startswith("98"):
            phone = "0" + phone[2:]

        return phone
