class Transformer:
    # converts roman numerals to decimal
    # and decimal numerals to roman
    def __init__(self):
        self.tallies = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def roman_to_decimal(self, roman_number):
        # converts roman numerals to decimal
        sum = 0
        for i in range(len(roman_number) - 1):
            left = roman_number[i]
            right = roman_number[i + 1]
            if self.tallies[left] < self.tallies[right]:
                sum -= self.tallies[left]
            else:
                sum += self.tallies[left]
        sum += self.tallies[roman_number[-1]]
        return sum

    def decimal_to_roman(self, decimal_number):
        # converts decimal numerals to roman
        tallies_2 = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        self.tallies.update(tallies_2)
        result = ""
        for key, value in list(sorted(self.tallies.items(), key=lambda item: item[1], reverse=True)):
            while decimal_number >= value:
                result += key
                decimal_number -= value
        return result

number = Transformer()
print(number.decimal_to_roman(4494))
print(number.roman_to_decimal("MMMMCDXCIV"))