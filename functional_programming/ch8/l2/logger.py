def args_logger(*args, **kwargs):
    counter = 0
    for arg in args:
        counter += 1

        print(f"{counter}. {arg}")

    itemized_kwargs = kwargs.items()
    sorted_items = sorted(itemized_kwargs)

    for kwarg in sorted_items:
        print(f"* {kwarg[0]}: {kwarg[1]}")