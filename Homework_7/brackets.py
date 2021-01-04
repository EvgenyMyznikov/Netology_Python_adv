from Homework_7.stack import Stack


def get_check_brackets(symbols):
    stack = Stack()
    mapping = {'(': ')', '[': ']', '{': '}'}
    for elem in symbols:
        if elem in mapping.keys():
            stack.push(elem)
        elif elem in mapping.values():
            if mapping.get(stack.peek()) == elem:
                stack.pop()
            else:
                return False
    if stack.isEmpty():
        return True
    return False


if __name__ == '__main__':
    while True:
        brackets = input('input brackets or "q" for exit:  ')
        if brackets == 'q':
            break
        print('balanced' if get_check_brackets(brackets) else 'unbalanced')
