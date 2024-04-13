import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize('book_name', ['Я', 'Что делать, если ваш пес хочет вас убить'])
    def test_add_new_book_valid_name(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre

    def test_set_book_genre_valid_genre(self):
        collector = BooksCollector()
        new_book = 'Дом на холме'
        book_genre = 'Ужасы'
        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, book_genre)
        assert collector.books_genre[new_book] == book_genre

    def test_get_book_genre_shows_genre(self):
        collector = BooksCollector()
        collector.books_genre['Пуаро'] = 'Детектив'
        expected_result = 'Детектив'
        result = collector.get_book_genre('Пуаро')
        assert expected_result == result

    def test_get_books_with_specific_genre_shows_valid_books(self):
        collector = BooksCollector()
        collector.books_genre = {
            "Гарри Поттер": "Фантастика",
            "Хоббиты": "Фантастика",
            "Шопоголик": "Комедия"
        }
        expected_result = ['Гарри Поттер', 'Хоббиты']
        assert collector.get_books_with_specific_genre('Фантастика') == expected_result

    def test_get_books_genre_shows_all_genres(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == collector.books_genre

    def test_get_books_for_children_shows_dict_without_adult_books(self):
        collector = BooksCollector()
        books_genre = {
            "Гарри Поттер": "Фантастика",
            "Шопоголик": "Комедия",
            "Смерть на Ниле": "Детектив",
            "Дом у озера": "Ужасы"
        }
        adult_books = {}
        for book, genre in books_genre.items():
            if genre in collector.genre_age_rating:
                adult_books[book] = genre
        assert adult_books not in collector.get_books_for_children()

    def test_add_book_in_favorites_does_not_add_missing_book(self):
        collector = BooksCollector()
        collector.books_genre = {
            "Гарри Поттер": "Фантастика",
            "Шопоголик": "Комедия"
        }
        collector.favorites = set()
        collector.add_book_in_favorites("Дом у озера")
        assert "Дом у озера" not in collector.favorites

    def test_delete_book_from_favorites_removes_existing_book(self):
        collector = BooksCollector()
        collector.favorites = {"Гарри Поттер", "Шопоголик"}
        collector.delete_book_from_favorites("Гарри Поттер")
        assert "Гарри Поттер" not in collector.favorites

    def test_get_list_of_favorites_books_returns_favorites(self):
        collector = BooksCollector()
        collector.favorites = {"Гарри Поттер", "Шопоголик"}
        favorites_list = collector.get_list_of_favorites_books()
        assert favorites_list == {"Гарри Поттер", "Шопоголик"}