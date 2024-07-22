import sys
from antlr4 import *
from gen.ConfRoomSchedulerLexer import ConfRoomSchedulerLexer
from gen.ConfRoomSchedulerParser import ConfRoomSchedulerParser
from gen.ConfRoomSchedulerListener import ConfRoomSchedulerListener

# time in minutes
MAX_TIME = 120


class Scheduler:
    def __init__(self):
        self.reservations = {}

    @staticmethod
    def clean_time(time):
        hour, minute = time.split(":")
        if int(hour) < 0 or int(hour) > 23:
            raise Exception("Invalid Time: Invalid hour")
        if int(minute) < 0 or int(minute) > 59:
            raise Exception("Invalid Time: Invalid minute")


        return int(time.replace(":", ""))

    @staticmethod
    def validate_max_time(start_time: str, end_time: str):
        start_hour, start_minute = start_time.split(":")
        end_hour, end_minute = end_time.split(":")

        # Convert start and end times to minutes
        start_time_minutes = int(start_hour) * 60 + int(start_minute)
        end_time_minutes = int(end_hour) * 60 + int(end_minute)

        if end_time_minutes < start_time_minutes:
            raise Exception("Invalid Time: End time is before start time")

        # Calculate elapsed time in minutes
        elapsed_minutes = end_time_minutes - start_time_minutes

        if elapsed_minutes > MAX_TIME:
            raise Exception("Invalid Time: Max time exceeded")

    def print_schedule(self):
        for room in self.reservations:
            print(f"Room: {room}")
            for reservation in self.reservations[room]:
                start_time_str = str(reservation[0])
                end_time_str = str(reservation[1])
                start_time = f"{start_time_str[:-2]}:{start_time_str[-2:]}"
                end_time = f"{end_time_str[:-2]}:{end_time_str[-2:]}"

                print(f"Start: {start_time} End: {end_time}")
            print()
        pass

    def reserve(self, start_time: int, end_time: int, room: str):

        # Si el cuarto no ha sido reservado, se agrega
        if room not in self.reservations:
            self.reservations[room] = []
            self.reservations[room].append((start_time, end_time))
            return

        # Si el cuarto ya ha sido reservado, se verifica que no haya traslape
        reservations = self.reservations[room]
        for reservation in reservations:
            scheduled_start_time = reservation[0]
            scheduled_end_time = reservation[1]

            if scheduled_end_time > start_time and scheduled_start_time < start_time:
                raise Exception("Room already reserved: start time colides with another reservation")
            if scheduled_start_time < end_time and scheduled_end_time > end_time:
                raise Exception("Room already reserved: end time colides with another reservation")

        self.reservations[room].append((start_time, end_time))


class ConfRoomSchedulerSemanticChecker(ConfRoomSchedulerListener):
    scheduler = Scheduler()

    def enterReserveStat(self, ctx):
        room = ctx.reserve().ID().getText()

        start_time = ctx.reserve().TIME(0).getText()
        end_time = ctx.reserve().TIME(1).getText()

        # Validate time
        self.scheduler.validate_max_time(start_time, end_time)

        start_time = self.scheduler.clean_time(start_time)
        end_time = self.scheduler.clean_time(end_time)

        self.scheduler.reserve(start_time, end_time, room)

    def enterListStat(self, ctx):
        self.scheduler.print_schedule()


def main():
    input_stream = FileStream(sys.argv[1])
    lexer = ConfRoomSchedulerLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ConfRoomSchedulerParser(stream)
    tree = parser.prog()

    semantic_checker = ConfRoomSchedulerSemanticChecker()
    walker = ParseTreeWalker()
    walker.walk(semantic_checker, tree)


if __name__ == '__main__':
    main()
