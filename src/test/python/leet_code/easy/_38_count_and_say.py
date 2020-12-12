"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1" countAndSay(n) is the way you would "say" the digit string from
countAndSay(n-1), which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of groups so that each
group is a contiguous section all of the same character. Then for each group, say the number of
characters, then say the character. To convert the saying into a digit string, replace the counts
with a number and concatenate every saying.

Given a positive integer n, return the nth term of the count-and-say sequence.

Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.

Example 2:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
"""

# Complexity
# Time: Worst case 2 ^ n (exponential) where no two digits are identical and it doubles on every iteration
# Space: O(m) where m is the length of the count and say string

class Solution:
    def countAndSay(self, number):
        if number == 1:
            return str(number)

        result = self.generate_next("1")
        for i in range(2, number):
            result = self.generate_next(result)

        return result

    def generate_next(self, num_str):
        result = []
        count = 1

        length = len(num_str)
        for current_idx in range(0, length):
            current_number = num_str[current_idx]

            # If we are at the last number, then add count to result
            if current_idx == length - 1:
                result.extend([str(count), current_number])
                break

            next_number = num_str[current_idx + 1]

            # If next no is not equal to current then add to result and reset count
            if current_number != next_number:
                result.extend([str(count), current_number])
                count = 1
            # If they are same, add the count
            else:
                count += 1

        return ''.join(result)


def test_count_and_say():
    assert Solution().countAndSay(4) == '1211'
