from Levenshtein import distance
from dataclasses import dataclass

file = open('numbers.txt')
text = file.read()
file.close()

numerals = []
line = text.split(',')
for j in line:
    words = j.split()
    res_line = []
    for k in words:
        res_line.append(k.strip())
    numerals.append(res_line)


@dataclass
class Numeral:
    value: int
    multiply: bool


templates = {
    "ноль": Numeral(0, False),
    "один": Numeral(1, False),
    "одна": Numeral(1, False),
    "два": Numeral(2, False),
    "две": Numeral(2, False),
    "три": Numeral(3, False),
    "четыре": Numeral(4, False),
    "пять": Numeral(5, False),
    "шесть": Numeral(6, False),
    "семь": Numeral(7, False),
    "восемь": Numeral(8, False),
    "девять": Numeral(9, False),
    "десять": Numeral(10, False),
    "одиннадцать": Numeral(11, False),
    "двенадцать": Numeral(12, False),
    "тринадцать": Numeral(13, False),
    "четырнадцать": Numeral(14, False),
    "пятнадцать": Numeral(15, False),
    "шестнадцать": Numeral(16, False),
    "семнадцать": Numeral(17, False),
    "восемнадцать": Numeral(18, False),
    "девятнадцать": Numeral(19, False),
    "двадцать": Numeral(20, False),
    "тридцать": Numeral(30, False),
    "сорок": Numeral(40, False),
    "пятьдесят": Numeral(50, False),
    "шестьдесят": Numeral(60, False),
    "семьдесят": Numeral(70, False),
    "восемьдесят": Numeral(80, False),
    "девяносто": Numeral(90, False),
    "сто": Numeral(100, False),
    "двести": Numeral(200, False),
    "триста": Numeral(300, False),
    "четыреста": Numeral(400, False),
    "пятьсот": Numeral(500, False),
    "шестьсот": Numeral(600, False),
    "семьсот": Numeral(700, False),
    "восемьсот": Numeral(800, False),
    "девятьсот": Numeral(900, False),
    "тысяч": Numeral(1000, True),
    "тысяча": Numeral(1000, True),
    "тысячи": Numeral(1000, True),
}

numbers = []
for i in numerals:
    result = 0
    for j in i:
        best_distance = 99999
        best_template = None
        for k in templates:
            dist = distance(j, k)
            if dist < best_distance:
                best_distance = dist
                best_template = templates[k]

        if best_template.multiply:
            result *= best_template.value
        else:
            result += best_template.value
    numbers.append(result)

even_sum = 0
even_count = 0
for i in numbers:
    if i % 2 == 0:
        even_sum += i
        even_count += 1
print(even_sum / even_count)
