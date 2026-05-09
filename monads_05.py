from pymonad.maybe import Just, Nothing

MAX_DIFFERENCE = 4

def begin():
    return Just((0, 0))


def is_balanced(left: int, right: int) -> bool:
    return abs(left - right) <= MAX_DIFFERENCE


def to_left(num: int):
    def step(pole):
        left, right = pole
        new_left = left + num

        if is_balanced(new_left, right):
            return Just((new_left, right))

        return Nothing

    return step


def to_right(num: int):
    def step(pole):
        left, right = pole
        new_right = right + num

        if is_balanced(left, new_right):
            return Just((left, new_right))

        return Nothing

    return step


def banana(_pole):
    return Nothing


def show(result):
    if result == Nothing:
        print("он упал")
        return

    print(f"не упал {result.value}")

# упал
show(
    begin()
    .bind(to_left(2))
    .bind(to_right(5))
    .bind(to_left(-2))
)
# не упал
show(
    begin()
    .bind(to_left(2))
    .bind(to_right(5))
    .bind(to_left(-1))
)
# упал
show(
    begin()
    .bind(to_left(2))
    .bind(banana)
    .bind(to_right(5))
    .bind(to_left(-1))
)
