from enum import Enum

logger = True


class LoggerType(Enum):
    SUBSCRIBE = ("SUBSCRIBE",)
    PUBLISH = "PUBLISH"


def log_repl_message(who: LoggerType, message: str) -> None:
    if logger:
        print("{:10s} {:4s}  {:50s}".format(who.name, "-- ", message))
