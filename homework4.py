class Transformer:
    # converts roman numerals to decimal
    # and decimal numerals to roman
    def __init__(self, tallies = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}):
        self.tallies = tallies

    def roman_to_decimal(self, roman_number):
        # converts roman numerals to decimal
        sum = 0
        for i in range(len(roman_number) - 1):
            left = roman_number[i]
            right = roman_number[i + 1]
            if self.tallies[left] < self.tallies[right]:
                sum -= self.tallies[left]
            else:
                sum += self.tallies[right]
        sum += self.tallies[roman_number[-1]]
        return sum

    def decimal_to_roman(self, decimal_number):
        # converts decimal numerals to roman
        # this function can't work with values 4 and 9
        result = ""
        for key, value in list(sorted(self.tallies.items(), key=lambda item: item[1], reverse=True)):
            while decimal_number >= value:
                result += key
                decimal_number -= value
        return result

number = Transformer()
print(number.decimal_to_roman(4494))
print(number.roman_to_decimal("MMMMCDXLIV"))


# converts decimal numerals to roman
# this function can work with values 4
'''def decimal_to_roman(decimal_number):
    result = ""
    lst = list(sorted(tallies.items(), key=lambda item: item[1], reverse=True))
    for key, value in lst:
        int_from_div = decimal_number // value
        print(int_from_div)
        if int_from_div < 0:
            continue
        elif int_from_div == 4 and key != "M":
            for i in range(len(lst)):
                if lst[i][0] == key:
                    result[:-1]
                    result += key + lst[i-1][0]
                    decimal_number -= value * int_from_div
        else:
            result += key*int_from_div
            decimal_number -= value*int_from_div
    return result

print(decimal_to_roman(494))'''