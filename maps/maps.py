from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        rating_list = []

        for item in list_of_movies:
            counter = item.get('country', ' ')
            if (item['rating_kinopoisk'] != ''
                    and item['rating_kinopoisk'] != '0' and counter.count(',') >= 1):
                rating_list.append(item['rating_kinopoisk'])

        str_to_float = list(map(float, rating_list))

        return sum(str_to_float) / len(str_to_float)

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        rating_films = filter(lambda item: item['rating_kinopoisk'] != '', list_of_movies)

        count_map = map(lambda movie:
                        movie['name'].count('и')
                        if float(movie['rating_kinopoisk']) >= rating else 0,
                        rating_films)

        return sum(count_map)
