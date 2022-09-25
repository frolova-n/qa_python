Для проверки метода add_new_book я оставила тест из примера, так же добавила тест на то, 
что нельзя добавлять одну книгу дважды.
Метод set_book_rating проверила добавлением рейтинга в диапазоне от 1 до 10 и вне диапазона(11).
Метод get_book_rating проверяется в тестах метода set_book_rating.
Так же выполнила позитивные проверки для методов get_books_with_specific_rating, add_book_in_favorites, delete_book_from_favorites и get_list_of_favorites_booksю
Так же я хотела добавить тест на то, что метод test_add_book_in_favorites не добавляет книгу избранное, 
если ее нет в books_rating, но в итоге получилось, что он добавляет. Не могу понять почему так. 