# ДЗ 
Требуется реализовать методы в `contact_book.py`, и проверить их тестами `test_contact_book.py`

Запуск тестов командой `python -m unittest` в терминале.

### 1. Адресная книга
★★☆☆☆

Вам нужно помочь реализовать класс для хранения адресной книги и поиска по ней.

Для этого потребуется реализовать несколько функций. 

```python
def add(self, s: Contact):
		"""Добавляет имя нового контакта в адресную книгу."""
```

```python
def contains(self, name: str) -> bool:
    """Возвращает true, если контакт с именем name есть в книге."""
```

```python
def count_starts_with(self, pref: str) -> int:
    """Возвращает количество контактов, добавленных в адресную книгу, имена которых начинаются с pref."""
```

```python
def starts_with(self, pref: str) -> List[Contact]:
    """Возвращает все контакты, имена которых начинаются с префикса pref."""
```
