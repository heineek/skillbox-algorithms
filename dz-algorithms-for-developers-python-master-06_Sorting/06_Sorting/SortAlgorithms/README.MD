# ДЗ
Требуется реализовать методы в модулях
`bubble_sort.py`, `counting_sort.py`, `insertion_sort.py`, `selection_sort.py` и проверить их тестами `test_sort.py`

Запуск тестов:

* командой `python -m unittest test_sort.py` в терминале

### 1. Первая сортировка
★★☆☆☆

В классе `bubble_sort.py` надо реализовать метод сортировки пузырьком.
Реализуйте метод
```python
def sort(arr: List[int]) -> None:
```

### 2. Сортировка выбором
★★★☆☆

В вашу команду пришел новый тимлид. Он уверен, что работать напрямую с массивом нельзя, нужна обертка над ним.
Для этого он создал класс:

```python
class SuperArray:
    def get_size(self) -> int:
        pass

    def get(self, position: int) -> int:
        pass

    def set(self, position: int, value: int) -> None:
        pass

```
Первый метод позволяет получить размер массива, второй - получить число, которое лежит по индексу
position, а последний метод позволяет записать новое значение по индексу.

Используя данный класс, реализуйте сортировку в классе `selection_sort.py`.
```python
def sort(arr: SuperArray) -> None:
```


### 3. Сортировка вставками
★★★☆☆

В зоопарке переполох. Кто-то сломал список, в котором были записаны веса животных и их имена.
Животные с одинаковым весом и породы сидят в двойных клетках, поэтому нам важно сохранить порядок в котором они сейчас находятся.
Для получения веса животных создан класс:
```python
class Animal:
    def get_weight(self) -> int:
        pass
```
Отсортируйте животных по весу в классе `insertion_sort.py`:
```python
def sort(arr: List[Animal]) -> None:
```

### 4. Сортировка подсчетом
★★★☆☆

Мы строим сервис для обработки пользовательских оценок. Известно, что размер
множества оценок, значительно превышает возможный диапазон значений оценок.
Все оценки находятся в диапазоне от 0 до max_value. Нам нужно реализовать метод,
который будет сортировать этот массив.

Отсортируйте оценки в классе `counting_sort.py`:
```python
def sort(arr: List[int], max_value: int) -> None:
```
