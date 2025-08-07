# -*- coding: utf-8 -*-
# 徹底攻略 Python3エンジニア認定試験　問題集2章

print("#1")
x = 100 - 5**2 + 5 / 5
print(x)

print("#2")
text = {
  "Usage:"
  "-h help "
  "-v version"
}
print(text)

print("#3")
text = """spam
ham
eggs
"""
print(text)

print("#4")
#NG "abc".length
#NG length("abc")
#NG strlen("abc")
print(len("abc"))

print("#5")
word = "abcdefg"
sliced_word = word[2:5]
print(sliced_word)


print("#6")
word = "abcdefg"
sliced_word = word[-5:]
print(sliced_word)

print("#7")
price = 15000
print(f"価格:{price:7d}")