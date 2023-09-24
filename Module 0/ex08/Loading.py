def print_prog(current: int, total: int, total_bwidth: int):
    '''Helper function that updates and prints the bar'''
    percentage = int(current / total * 100)
    per_str = str(percentage).rjust(3)
    bar_pc = int(total_bwidth * (percentage / 100))
    bar_prog = "{}{}".format("█" * bar_pc, " " * (total_bwidth - bar_pc))
    print(f"\r{per_str}%|{bar_prog}|{current}/{total}", end="")


def ft_tqdm(lst: range) -> None:
    '''This function is an oversimplified copy of the tqdm function'''
    total = len(lst)

    for current in lst:
        yield
        print_prog(current, total, 200)
    print_prog(total, total, 200)
