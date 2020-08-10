from typing import List, Optional


def is_closing_tag(tag: str) -> bool:
    return tag.startswith("</")


def opening_tag_for(tag: str) -> str:
    return tag.replace("</", "<")


def peek(stack: List[str], n=1) -> Optional[str]:
    if len(stack) >= n:
        return stack[-n]
    return None


def broken_html(html: List[str], stack: Optional[List[str]] = None, errors=0) -> str:
    if stack is None:
        stack = []

    for i, tag in enumerate(html):
        tag = tag.upper().strip()
        if is_closing_tag(tag):
            otag = opening_tag_for(tag)
            prev_tag = peek(stack)
            if otag == prev_tag:
                # ok
                stack.pop()
            else:
                if errors > 0:
                    return "INCORRECT"
                errors += 1
                # два варианта -
                # либо лишний открывающийся тег до этого
                # либо лишний закрывающийся сейчас в руках
                # запустим рекурсивно 2 цепочки
                closing_tag_res = broken_html(html[i+1:], stack.copy(), errors)
                if closing_tag_res == "CORRECT":
                    return f"ALMOST {tag}"

                opening_tag_res = broken_html(
                    html[i:], stack[:-1].copy(), errors)
                if opening_tag_res == "CORRECT":
                    return f"ALMOST {prev_tag}"

                return "INCORRECT"
        else:
            stack.append(tag)

    if len(stack) > 1:
        return "INCORRECT"
    if len(stack) == 1:
        return f"ALMOST {peek(stack)}"

    return "CORRECT"


def main():
    n = int(input())
    for i in range(n):
        n_tags = int(input())
        tags = [input() for j in range(n_tags)]
        result = broken_html(tags)
        print(result)


if __name__ == "__main__":
    main()
