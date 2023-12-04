#
from random import sample


class WrongCountOfNumbersError(Exception):
    def __init__(self, numbers):
        super().__init__("Lotto machine requires 6 numbers")
        self.numbers = numbers


class NumbersNotUniqueError(Exception):
    def __init__(self, numbers):
        super().__init__("Lotto machine requires unique numbers")
        self.numbers = numbers


class NumbersNotInRangeError(Exception):
    def __init__(self, numbers):
        super().__init__("Lotto machine requires numbers between 1 and 49")
        self.numbers = numbers


class LottoGame:
    def __init__(self):
        self._player_numbers = set()
        self._winning_numbers = set()

    def player_numbers(self):
        return self._player_numbers

    def winning_numbers(self):
        return self._winning_numbers

    def draw_winning_numbers(self):
        self._winning_numbers = set(sample(range(1, 49), 6))

    def set_player_numbers(self, numbers=None):
        if not numbers:
            self._player_numbers = set(sample(range(1, 49), 6))
        else:
            self.check_player_numbers(numbers)
            self._player_numbers = set(numbers)

    def check_player_numbers(self, numbers):
        self._if_six(numbers)
        self._if_unique(numbers)
        self._if_in_range(numbers)

    def matching_numbers(self):
        return self._player_numbers.intersection(self._winning_numbers)

    def _if_six(self, numbers):
        if not len(numbers) == 6:
            raise WrongCountOfNumbersError(numbers)

    def _if_unique(self, numbers):
        if not len(set(numbers)) == 6:
            raise NumbersNotUniqueError(numbers)

    def _if_in_range(self, numbers):
        if not all(0 < int(i) < 50 for i in numbers):
            raise NumbersNotInRangeError(numbers)

    def play(self, numbers=None):
        self.set_player_numbers(numbers)
        self.draw_winning_numbers()
        matching_numbers = self.matching_numbers()
        return self.results(matching_numbers)

    def results(self, numbers):
        joined_numbers = ', '.join(str(i) for i in self._winning_numbers)
        winning_numbers_str = f"Wylosowane liczby to: {joined_numbers}\n"
        player_numbers_str = (
            f"Trafiłeś poprawnie liczby: {', '.join(str(i) for i in numbers)}"
            if len(numbers)
            else "Brak trafionych cyfr"
        )
        return winning_numbers_str + player_numbers_str

#brak zaimplementowanej opcji "chybił trafił"
#napisać testy do tych funkcji
#zrefaktoryzować ten kod -> nie ruszamy jednak refaktoryzacji dopóki nie wiemy, że funkcja działa
#czyli musimy zacząć od testów

def main():
    lotto_game = LottoGame()
    numbers = None
    while True:
        print("Witaj w Lotto")
        print("1 - wybierz wlasne liczby")
        print("2 - chybil trafil")
        option = input("> ").strip()
        if not (option == "1" or option == "2"):
            print("Bledna opcja. Sprobuj ponownie")
            continue
        if option == "1":
            print(
                "Podaj 6 różnych liczb z zakresu od 1 do 49"
                " (oddzielonych spacjami)"
            )
            numbers = input("> ").strip()
            numbers = [int(i) for i in numbers.split(" ")]
        results = lotto_game.play(numbers)
        print(results)


if __name__ == "__main__":
    main()
