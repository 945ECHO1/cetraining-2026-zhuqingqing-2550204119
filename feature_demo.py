def calculate_average(numbers):
    """
    计算列表的平均值
    :param numbers: 数字列表
    :return: 平均值
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    test_list = [85, 90, 78, 92, 88]
    avg = calculate_average(test_list)
    print(f"列表: {test_list}")
    print(f"平均值: {avg}")