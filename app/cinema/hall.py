from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str,
                      customers: list,
                      cleaning_staff: str) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for person in customers:
            name = person["name"]
            print(f'{name} is watching "{movie_name}".')

        print(f'"{movie_name}" ended.')
        cleaning_staff = Cleaner(cleaning_staff)
        cleaning_staff.clean_hall(self.number)