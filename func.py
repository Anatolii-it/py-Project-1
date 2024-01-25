def analyze_numbers(numbers):
    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
    print("Парних   - ",even_count)
    print("Непарних - ",odd_count)
    print("Додатних - ",positive_count)
    print("Від'ємних  ",negative_count)
    return even_count, odd_count, positive_count, negative_count