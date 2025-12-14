# Chapter03_2
# 파이썬 완전 기초
# Print 사용법

# format 사용(d : 3, s = 'python', f = 3.141592)
# d - 정수, s - 문자열, f - 실수
print('%s %s' %('one', 'two'))          # 값이 뭐가 나와야하는지 명확하게 명시
print('{} {}'.format('one', 'two'))     # 좀더 유연하게 사용 가능
print('{1} {0}'.format('one', 'two'))

print()

# %s
# 오른쪽 정렬
print('%10s' %('nice'))
print('{:>10}'.format('nice'))
# 왼쪽 정렬
print('%-10s' %('nice'))
print('{:10}'.format('nice'))   # 여기서만 s 생략 가능함
# 중앙 정렬
print('{:^10}'.format('nice'))
# 빈 글자 자리에 문자 삽입
print('{:_>10}'.format('nice'))
print('{:$>10}'.format('nice'))
# 자리수 만큼 잘라서 출력
print('%.5s' %('nice'))
print('%.5s' %('pythonnice~'))
print('{:10.5s}'.format('pythonnice~'))

print()

# %d
print('%d %d' %(1, 2))
print('{} {}'.format(1,2))

print('%4d' %(42))
print('{:4d}'.format(42))

print()

# %f
print('%f' %(3.1414141414))
print('{:f}'.format(3.1414141414))

print('%06.2f' %(3.141592123456789))        # 출력값 : 003.14
print('{:06.2f}'.format(3.141592123456789))