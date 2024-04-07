from stack import ArrayStack


def is_matched(expression: str) -> bool:
    """
    match delimiters like ), }, ] in a given expression.
    """

    lefty = "([{"
    righty = ")]}"

    s = ArrayStack()

    for c in expression:
        if c in lefty:
            s.push(e=c)

        elif c in righty:
            if s.is_empty():
                return False
            if righty.index(c) != lefty.index(s.pop()):
                return False
    return s.is_empty()


def is_matched_html(raw: str) -> bool:
    """
    To match html tags from the given raw string.
    """

    s = ArrayStack()
    j = raw.find("<")

    while j != -1:
        k = raw.find(">", j + 1)
        if k == -1:
            return False
        tag = raw[j + 1, k]

        if not tag.startswith("/"):
            s.push(tag)
        else:
            if s.is_empty():
                return False
            if tag[1:] != s.pop():
                return False
        j = raw.find("<", k + 1)

    return s.is_empty()
