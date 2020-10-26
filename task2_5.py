'''Користувачем  вводяться  з  клавіатури 10 цілих  чисел,  при  цьому враховуються лише натуральні числа (цілі додатні).Необхідно з’ясувати, скільки чисел серед 10 введених були простими'''
i, flag, result, divisor, countDivisor = 0, False, 0, 2, 0;

while (i < 10):
	number = int(input("Введите целое число:"));
	while (divisor <= number):
		divisor += 1;
		if (number % divisor == 0 and divisor != number):
			countDivisor += 1;
			continue;
		elif (divisor == number and (countDivisor == 1 or countDivisor == 0)):
			result += 1;
	i += 1;
	divisor = 0;
	countDivisor = 0;
print("Количество простых чисел из списка введённых: %i" % result);
