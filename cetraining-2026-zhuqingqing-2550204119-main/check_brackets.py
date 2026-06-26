def check_brackets(s: str) -> bool:
    """
    判断字符串中的括号是否匹配。

    支持: () [] {}
    思路: 用栈模拟——左括号入栈，右括号与栈顶配对出栈。
    """
    stack = []
    match = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in match.values():      # 左括号
            stack.append(ch)
        elif ch in match:             # 右括号
            if not stack or stack[-1] != match[ch]:
                return False
            stack.pop()

    return not stack


def main():
    cases = [
        ("()", True),
        ("()[]{}", True),
        ("({[]})", True),
        ("(]", False),
        ("([)]", False),
        ("(((", False),
        ("())", False),
        ("a+(b*[c-{d}])", True),
        ("", True),
        ("}{", False),
        ("[(])", False),
    ]

    for s, want in cases:
        got = check_brackets(s)
        mark = "PASS" if got == want else "FAIL"
        print(f"[{mark}]  {repr(s):20s}  -> {got}  (期望 {want})")


if __name__ == "__main__":
    main()