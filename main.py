import flet

# Создание экземпляра игры
game = flet.Game()

# Определение функции для обработки пользовательского ввода
def on_click(row, col):
    if game.board[row][col] == " ":  # Проверяем, что ячейка пустая
        game.board[row][col] = game.current_player  # Устанавливаем символ текущего игрока в выбранную ячейку
        game.check_winner()  # Проверяем, есть ли победитель
        game.switch_player()  # Переключаем игрока

# Создание элементов управления для отображения игрового поля
    buttons = [[flet.Button(lambda row=row, col=col: on_click(row, col)) for col in range(3)] for row in range(3)]

# Размещение кнопок на игровом поле
    for i in range(3):
        for j in range(3):
            buttons[i][j].grid(row=i, column=j)

# Запуск игры
game.run()