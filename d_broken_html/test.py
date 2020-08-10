from broken_html import broken_html


def should_eq(expected, got, comment=""):
    if expected != got:
        print(f"WRONG: expected={expected} got={got} cm={comment}")


def test():
    data = "<Y> <X> <Y> </X> </Y>"
    should_eq(
        "ALMOST <Y>",
        broken_html(data.split(" ")),
        data
    )

    should_eq(
        "CORRECT",
        broken_html(["<X>", "<Y>", "</Y>", "</X>"]),
        ["<X>", "<Y>", "</Y>", "</X>"]
    )

    should_eq(
        "ALMOST </KUKA>",
        broken_html(["<HTML>", "<biba>", "</BIBA>", "</KUKA>", "</HTML>"]),
        ["<HTML>", "<biba>", "</BIBA>", "</KUKA>", "</HTML>"]
    )

    should_eq(
        "INCORRECT",
        broken_html(["<X>", "<Y>", "</X>", "</Y>"]),
        ["<X>", "<Y>", "</X>", "</Y>"]
    )

    should_eq(
        "ALMOST <A>",
        broken_html(["<A>", "<X>", "<Y>", "</Y>", "</X>"]),
        ["<A>", "<X>", "<Y>", "</Y>", "</X>"]
    )

    should_eq(
        "ALMOST <A>",
        broken_html(["<X>", "<Y>", "<A>", "</Y>", "</X>"]),
        ["<X>", "<Y>", "<A>", "</Y>", "</X>"]
    )

    # strip check
    data = ["<HTML> ", "<TAG>", "<button>", "</tag>",
            "</BUTTON>", "</tag>", "</html>", ]
    should_eq(
        "ALMOST </TAG>",
        broken_html(data),
        data
    )

    data = ["<X>", "<X>", "<X>", "</X>", "</X>"]
    should_eq(
        "ALMOST <X>",
        broken_html(data),
        data
    )
    data = ["<X>", "<X>", "</X>", "</X>", "</X>"]
    should_eq(
        "ALMOST </X>",
        broken_html(data),
        data
    )

    data = ["<X>"]
    should_eq(
        "ALMOST <X>",
        broken_html(data),
        data
    )

    data = ["</X>"]
    should_eq(
        "ALMOST </X>",
        broken_html(data),
        data
    )

    data = []
    should_eq(
        "CORRECT",
        broken_html(data),
        data
    )

    data = ["<X>", "<Y>", "<X>", "</X>", "</Y>", "</X>"]
    should_eq(
        "CORRECT",
        broken_html(data),
        data
    )

    data = ["<X>", "<Y>", "<X>", "</X>", "</X>", "</Y>", "</X>"]
    should_eq(
        "ALMOST </X>",
        broken_html(data),
        data
    )

    data = ["<X>", "</X>", "<Y>", "<X>", "</X>", "</Y>", "</X>"]
    should_eq(
        "ALMOST </X>",
        broken_html(data),
        data
    )

    data = ["<X>", "<Y>", "</X>", "<X>", "</X>", "</Y>", "</X>"]
    should_eq(
        "ALMOST </X>",
        broken_html(data),
        data
    )

    data = ["<X>", "<Y>", "<X>", "</X>", "</X>", "</Y>", "</X>"]
    should_eq(
        "ALMOST </X>",
        broken_html(data),
        data
    )

    data = ["<X>", "<Y>", "<X>", "</X>", "</Y>", "</X>", "</X>"]
    should_eq(
        "ALMOST </X>",
        broken_html(data),
        data
    )

    data = "<HTML> <X> <Y> <B> <X> <A> </B> </A> </X> </B> </Y> </X> </HTML>"
    should_eq(
        "ALMOST </B>",
        broken_html(data.split(" ")),
        data
    )

    data = "<X> <Y> </X> </Y> </X>"
    should_eq(
        "ALMOST </X>",
        broken_html(data.split(" ")),
        data
    )

    data = "<Y> <X> <Y> </X> </Y> </X> </Y>"
    should_eq(
        "ALMOST </X>",
        broken_html(data.split(" ")),
        data
    )

    data = "<X> <Y> </Y> <Z> </Z> </X>"
    should_eq(
        "CORRECT",
        broken_html(data.split(" ")),
        data
    )

    data = "<X> <Y> <Z> </Z> </Y> </X>"
    should_eq(
        "CORRECT",
        broken_html(data.split(" ")),
        data
    )

    data = "<X> <X> </X> </X>"
    should_eq(
        "CORRECT",
        broken_html(data.split(" ")),
        data
    )

    data = "<x> <y> <a> <b> <c> </c> </b> </a> </y> </x>"
    should_eq(
        "CORRECT",
        broken_html(data.split(" ")),
        data
    )


if __name__ == "__main__":
    test()
