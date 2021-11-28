import math

class Loader:
    def __init__(self, width: int, msg: str, total: int) -> None:
        self.width = width
        self.msg = msg
        self.total = total

    def finish(self) -> None:
        fix = "[] 100% []"
        bar_len = self.width - len(self.msg) - len(fix)
        return f"[{self.msg}] Done [{'#' * bar_len}]"

    def load(self, current: int):
        percent = int(current / self.total * 100)
        return self.__template(percent)

    def __template(self, percent) -> None:
        """ [file.name.ext] x20% [###########                                ] """
        fix = "[] 100% []"
        bar_len = self.width - len(self.msg) - len(fix)
        hash_len =  int(math.floor(bar_len * (percent / 100)))
        space_len = bar_len - hash_len
        return f"[{self.msg}] {percent:03}% [{'#' * hash_len}{' ' * space_len}]"
