from pymonad.tools import curry


#2.1

@curry(2)
def concate(left_string: str, right_string: str) -> str:
    return left_string + right_string;

hello = concate("Hello, ")
print(hello("Steve"))
print(hello("Andy"))


#2.2 - поскольку один аргумент на функцию - вкладываем несколько друг в друга:
@curry(4)
def greet(
    hello_word: str, 
    punct_sign: str,
    personal_name: str,
    dot_sign: str
    ) -> str:
    return hello_word + punct_sign + " " + personal_name + dot_sign

def first_step(hello_word_lambda: str):
    def second_step(punct_sign_lambda: str):
        def third_step(dot_sign_lambda: str):
            return lambda personal_name_lambda: greet(
                hello_word_lambda,
                punct_sign_lambda,
                personal_name_lambda,
                dot_sign_lambda
            )
        return third_step
    return second_step

final = first_step("Hello")(",")("...")

print(final("Chuck"))
print(final("Robin"))
