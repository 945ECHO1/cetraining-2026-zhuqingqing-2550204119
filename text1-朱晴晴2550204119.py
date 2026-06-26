def is_balanced(s: str) -> bool:
    """
    判断字符串中的括号是否匹配。

    支持的括号类型: () [] {}

    参数:
        s: 输入字符串

    返回:
        True 表示括号完全匹配，False 表示不匹配
    """
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0  # 栈为空说明全部匹配


if __name__ == "__main__":
    # 测试用例
    tests = [
        ("()", True),
        ("()[]{}", True),
        ("({[]})", True),
        ("(]", False),
        ("([)]", False),
        ("(((", False),
        ("())", False),
        ("a + (b * [c - {d}])", True),
        ("", True),
    ]

    for s, expected in tests:
        result = is_balanced(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] '{s}' -> {result} (期望: {expected})")
