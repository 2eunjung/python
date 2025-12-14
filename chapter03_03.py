# Chapter03_3
# 파이썬 완전 기초
# Print 사용법

### 3가지 Format Practices
x = 50
y = 100
text = 123456789
n = 'Lee'

# 출력1
ex1 = 'n = %s, s = %s, sum = %d' %(n, text, (x + y))
print(ex1)

# 출력2
ex2 = 'n = {n}, s = {s}, sum = {sum}'.format(n=n, s=text, sum=x + y)
print(ex2)

# 출력3
ex3 = f'n = {n}, s = {text}, sum = {x + y}'
print(ex3)
print(f'n = {n}, s = {text}, sum = {x + y}')

print()

### 구분기호
m = 1000000000000
print(f'm : {m:,}')

print()


### 정렬
"""
    ^ : 가운데 정렬
    < : 왼쪽 정렬
    > : 오른쪽 정렬
"""
t = 20
print(f't : {t:10}')
print(f't : {t:^10}')
print(f't : {t:>10}')
print(f't : {t:<10}')

print()

print(f't center: {t:-^10}')
print(f't center: {t:*^10}')
print(f't center: {t:#<10}')