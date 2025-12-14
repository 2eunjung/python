# Chapter03_1
# 파이썬 완전 기초
# Print 사용법

"""
    Escape 코드
    \n      : 개행
    \t      : 탭
    \\      : 문자
    \'      : 문자
    \"      : 문자
    \000    : 널문자
    ...
"""

# 기본 출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

print()

# separator 출력
print('p', 'y', 't', 'h', 'o', 'n')
print('p', 'y', 't', 'h', 'o', 'n', sep='')
print('p', 'y', 't', 'h', 'o', 'n', sep='|')
print('010','1111', '1111', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

print()

# file 옵션
import sys
print('Learn Python', file=sys.stdout)