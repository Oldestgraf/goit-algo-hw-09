# Видача решти: Жадібний алгоритм vs Динамічне програмування

## Опис

Цей проект реалізує два методи для визначення оптимального способу видачі решти: жадібний алгоритм та алгоритм динамічного програмування.

### Жадібний алгоритм

Жадібний алгоритм вибирає найбільші можливі монети для видачі решти. Це простий і швидкий метод, але він не завжди гарантує мінімальну кількість монет для всіх наборів монет.

### Динамічне програмування

Алгоритм динамічного програмування забезпечує мінімальну кількість монет для будь-якої суми. Він використовує результати попередніх підзадач для побудови оптимального рішення, але є повільнішим порівняно з жадібним алгоритмом.

## Порівняння ефективності

### Час виконання

- **Жадібний алгоритм:** \(O(n)\), де \(n\) - кількість номіналів монет.
- **Динамічне програмування:** \(O(n * amount)\), де \(amount\) - сума, для якої необхідно знайти решту.

### Оптимальність

- **Жадібний алгоритм:** Гарантує оптимальне рішення для певних наборів монет.
- **Динамічне програмування:** Завжди гарантує мінімальну кількість монет.

### Висновки

Жадібний алгоритм є відмінним вибором для стандартних наборів монет, таких як [50, 25, 10, 5, 2, 1], тоді як алгоритм динамічного програмування є універсальним рішенням для будь-яких наборів номіналів.

На основі оцінювання часу виконання для великих сум, жадібний алгоритм працює значно швидше, тоді як алгоритм динамічного програмування забезпечує мінімальну кількість монет, але вимагає більше часу.
