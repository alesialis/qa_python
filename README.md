Было реализовано 9 тестов:
1) test_add_new_book_valid_name - проверяет метод добавления новой книги при валидном названии/длиной граничных значений (1 символ и 40 символов)
2) test_set_book_genre_valid_genre - проверяет метод добавления жанра для книги, у которой его нет
3) test_get_book_genre_shows_genre - проверяет, что метод получения жанра действительно отображает корректный жанр для книги
4) test_get_books_with_specific_genre_shows_valid_books - проверяет, что из словаря книг возвращаются только книги с указанным жанром
5) test_get_books_genre_shows_all_genres - проверяет, что метод получения жанров возвращает актуальные данные
6) test_get_books_for_children_shows_dict_without_adult_books - проверяет, что метод получения детских книг не возвращает книги с жанром недетского рейтинга
7) test_add_book_in_favorites_doesnt_add_missing_book - проверяет, что нельзя добавить в избранное книгу не из общего словаря
8) test_delete_book_from_favorites_removes_existing_book - проверяет, что книгу, которая находится в избранном, можно удалить
9) test_get_list_of_favorites_books_returns_favorites - проверяет, что метод возвращает актуальный список избранных книг
