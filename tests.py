from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_book_twice(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(list(collector.books_rating.items())) == 1

    def test_set_book_rating_one_to_ten(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 8)

        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 8

    def test_set_book_rating_more_then_ten(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 11)

        assert collector.get_book_rating('Что делать, если ваш кот хочет вас убить') == 1

    def test_get_books_with_specific_rating(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 8)
        collector.set_book_rating('Гордость и предубеждение и зомби', 8)
        collector.get_books_with_specific_rating(8)

        assert collector.get_books_with_specific_rating(8) == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']

    def test_get_books_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.get_books_rating()

        assert collector.get_books_rating() == {'Гордость и предубеждение и зомби': 1,'Что делать, если ваш кот хочет вас убить': 1}

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.favorites.append('Что делать, если ваш кот хочет вас убить')

        assert collector.favorites == ['Что делать, если ваш кот хочет вас убить']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.favorites.append('Что делать, если ваш кот хочет вас убить')
        collector.favorites.append('Гордость и предубеждение и зомби')
        collector.favorites.remove('Что делать, если ваш кот хочет вас убить')

        assert collector.favorites == ['Гордость и предубеждение и зомби']


    def test_add_book_in_favorites_book_not_from_books_rating(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.favorites.append('Что делать, если ваш кот хочет вас убить')
        collector.favorites.append('Джедайские техники')

        assert collector.favorites == ['Что делать, если ваш кот хочет вас убить', 'Джедайские техники']