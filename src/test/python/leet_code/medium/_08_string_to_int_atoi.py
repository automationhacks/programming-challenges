class Solution:
    def myAtoi(self, string: str) -> int:
        minus = '-'
        sign = True
        valid_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        allowed_whitespace = ' '
        result = []

        for char in string:
            if char == minus:
                sign = False
                continue

            if char in valid_chars:
                result.append(char)
            elif not char == allowed_whitespace:
                if result:
                    return self.__convert_result_to_number_by_rules(result, sign)
                else:
                    return 0
            else:
                if result:
                    break

        return self.__convert_result_to_number_by_rules(result, sign)

    @staticmethod
    def __convert_result_to_number_by_rules(result, sign):
        int_min = -2 ** 31
        int_max = 2 ** 31 - 1

        number = ''.join(result)

        converted = 0
        try:
            converted = int(number)

            if converted in range(int_min, int_max):
                if not sign:
                    converted = -1 * converted
            else:
                if sign is False:
                    converted = int_min
                else:
                    converted = int_max
        except Exception:
            pass
        finally:
            return converted


def test_only_numbers():
    assert Solution().myAtoi("42") == 42


def test_leading_whitespaces_and_minus():
    assert Solution().myAtoi("    -42") == -42


def test_invalid_symbol_between_no():
    assert Solution().myAtoi("3.145667") == 3


def test_leading_invalid_non_whitespace():
    assert Solution().myAtoi("+-12") == 0


def test_string_with_words_and_leading_numbers():
    assert Solution().myAtoi("4193 with words") == 4193


def test_string_with_words_and_trailing_numbers():
    assert Solution().myAtoi("words and 987") == 0


def test_min_overflow():
    assert Solution().myAtoi("-91283472332") == -2147483648


def test_max_overflow():
    assert Solution().myAtoi("91283472332") == 2147483647


def test_no_with_plus():
    assert Solution().myAtoi("+1") == 1
