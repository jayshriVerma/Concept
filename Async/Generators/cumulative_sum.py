from typing import Generator


def cumulative_sum() -> Generator[float, float, None]:
    total: float = 0
    while True:
        # new_value: float = yield total # this total has been called twice  it retrieves the value and add it to the
        # total and then sends the new total,so basically no need to create new_value here can be squeezed to one line
        # total += new_value
        total += yield total


def main() -> None:
    cumulative_generator: Generator[float, float, None] = cumulative_sum()
    next(cumulative_generator)
    while True:
        value: float = float(input('Enter a vaue: '))
        current_sum: float = cumulative_generator.send(value)
        print(f'Cumulative Sum: {current_sum}')


if __name__ == "__main__":
    main()

# here yield retrieves the value send to the function by using send function and
# then it loops and add to the total and next time it yield so basically yield
# calls twice,so we can remove the new_value and just write total += yield total
# practically it should yield zero first , but when we call next(cumulative_generator) the yield
# keyword retrieves the value and passes to total so first time it should be value entered by user