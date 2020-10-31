"""
	Ken Amamori
    Problem 2: Write a function that takes as input a string and returns whether the parenthesis are balanced.
    If you solve this quickly, add the following difficulty: the string may also contain [] or {}.
    Return whether all three types of brackets are balanced.
    time: O(n), space: O(c)
"""


def balancedParenthesis(testingstring, stack):
    if len(testingstring) % 2 == 1:
        print(1)
        return False
    else:
        for v in testingstring:
            if v == "(" or v == "{":
                stack.append(v)
            else:
                if stack[-1] == "{":
                    if v != "}":
                        print(2)
                        return False
                    elif v == "}":
                        stack.pop(-1)
                        continue
                    else:
                        print(3)
                        return False
                elif stack[-1] == "(":
                    if v != ")":
                        print(4)
                        return False
                    elif v == ")":
                        stack.pop(-1)
                        continue
                    else:
                        print(5)
                        return False
                else:
                    print(6)
                    return False
        return True


testingstring = "(())(){}({()}){()}"
stack = []

# print(True)

print(balancedParenthesis(testingstring, stack))
