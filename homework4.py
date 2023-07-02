'''roman_to_decimal. Теперь оберните ее в класс Transformer.
В качестве аргумента класса храните тот самый словарик.
У этого класса должен быть метод roman_to_decimal
и обратный ему decimal_to_roman.'''

class Transformer:
    
    def __init__(self, tallies = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}):
        self.tallies = tallies

    def roman_to_decimal(self, roman_number):
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
        result = ""
        for key, value in list(sorted(self.tallies.items(), key=lambda item: item[1], reverse=True)):
            while decimal_number >= value:
                result += key
                decimal_number -= value
        return result

number = Transformer()
print(number.decimal_to_roman(5480))
print(number.roman_to_decimal("XXX"))