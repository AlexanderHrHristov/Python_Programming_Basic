searched_book = input()
books_counter = 0
book_is_found = False
current_book = input()

while current_book != 'No More Books':
    if current_book == searched_book:
        book_is_found = True
        break
    books_counter += 1
    current_book = input()
if book_is_found:
    print(f'You checked {books_counter} books and found it.')
else:
    print(f'The book you search is not here!')
    print(f'You checked {books_counter} books.')


# Modified AI
# searched_book = input()
# books_counter = 0
# found = False
#
# while True:
#     next_book = input()
#     if next_book == "No More Books":
#         break
#     if next_book == searched_book:
#         found = True
#         break
#     books_counter += 1
#
# if found:
#     print(f"You checked {books_counter} books and found it.")
# else:
#     print("The book you search is not here!")
#     print(f"You checked {books_counter} books.")