# Chapter03_5
# 파이썬 완전 기초
# 파이썬 변수

# id(identity) 확인 : 객체의 고유값 확인
m = 600
n = 700

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

m = 900
n = 900

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> 주로 메소드를 선언할 때
# Pascal Case : NumberOfCollegeGraduates -> 주로 클래스를 선언할 때
# Snake Case : number_of_college_graduates -> 파이썬에서 주로 변수 선언할 때

# 허용하는 변수 선언법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# 예약어는 변수명으로 사용 불가능
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""
