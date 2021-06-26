from telegram import InlineKeyboardMarkup, InlineKeyboardButton

ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT = range(8)
BACK = 'back'


def make_faq_inline_keyboard(string) -> InlineKeyboardMarkup:
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).
    buttons = globals()[string]
    return InlineKeyboardMarkup(buttons, row_width=1)


def make_faq_button_answer(string) -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='🔙 Назад', callback_data=string)],
        [InlineKeyboardButton(text='✅ Я знайшов відповідь', callback_data='thank')]
    ]
    return InlineKeyboardMarkup(buttons)


main = [
    [InlineKeyboardButton(text='Загальні питання', callback_data='g')],
    [InlineKeyboardButton(text='Підключення', callback_data='c')],
    [InlineKeyboardButton(text='Інтернет', callback_data='i')],
    [InlineKeyboardButton(text='Цифрове телебачення', callback_data='t')],
    [InlineKeyboardButton(text='Оплата', callback_data='p')],
]

general = [
    [InlineKeyboardButton(text='Як укласти договір на підключення до мережі Інтернет?',
                          callback_data='g1_1')],
    [InlineKeyboardButton(text='Я переїжджаю, але не хочу відмовлятися від послуг зв\'язку?',
                          callback_data='g1_2')],
    [InlineKeyboardButton(text='Для чого потрібен Особистий Кабінет?',
                          callback_data='g1_3')],
    [InlineKeyboardButton(text='Як мені дізнатися про новини компанії?',
                          callback_data='g1_4')],
    [InlineKeyboardButton(text='Які бувають акції?',
                          callback_data='g1_5')],
    [InlineKeyboardButton(text='Де знаходиться офіс компанії?',
                          callback_data='g1_6')],
    [InlineKeyboardButton(text='🔙Назад', callback_data='main')],
]

connect = [
    [InlineKeyboardButton(text='Як можна залишити заявку на підключення?',
                          callback_data='c1_1')],
    [InlineKeyboardButton(text='Чи є можливість підключення за моєю адресою?',
                          callback_data='c1_2')],
    [InlineKeyboardButton(text='Як підключити 2 комп\'ютери до інтернету?',
                          callback_data='c1_3')],
    [InlineKeyboardButton(text='Як краще організувати домашню мережу?',
                          callback_data='c1_4')],
    [InlineKeyboardButton(text='🔙Назад', callback_data='main')],
]

internet = [
    [InlineKeyboardButton(text='Чи є обмеження по трафіку (поріг скачування)?',
                          callback_data='i1_1')],
    [InlineKeyboardButton(text='Як налаштувати інтернет підключення після зміни системного блоку / перевстановлення мережевої карти?',
                          callback_data='i1_2')],
    [InlineKeyboardButton(text='Мені здається, що швидкість не відповідає заявленій. Що робити?',
                          callback_data='i1_3')],
    [InlineKeyboardButton(text='Як перезавантажити роутер?',
                          callback_data='i1_4')],
    [InlineKeyboardButton(text='У мене повільно завантажуються файли з визначеного сайту',
                          callback_data='i1_5')],
    [InlineKeyboardButton(text='Не можу вийти в інтернет, у мене маршрутизатор',
                          callback_data='i1_6')],
    [InlineKeyboardButton(text='🔙Назад', callback_data='main')],
]

tv = [

    [InlineKeyboardButton(text='Що це за телебачення, які канали в нього включені і яка вартість оплати?',
                          callback_data='t1_1')],
    [InlineKeyboardButton(text='Чи потрібно протягувати ще один кабель для ТВ якщо я вже підключений до інтернету?',
                          callback_data='t1_2')],
    [InlineKeyboardButton(text='Хочу підключити до однієї приставки кілька телевізорів. Чи можна це зробити?',
                          callback_data='t1_3')],
    [InlineKeyboardButton(text='Чи можу я переглядати телебачення на комп\'ютері, не використовуючи приставку?',
                          callback_data='t1_4')],
    [InlineKeyboardButton(text='Як налаштувати приставку на перегляд телебачення?',
                          callback_data='t1_5')],
    [InlineKeyboardButton(text='Чи можу я переглядати телебачення на телевізорі з функцією SMART TV?',
                          callback_data='t1_6')],
    [InlineKeyboardButton(text='Спільна робота ТВ та інтернет-з\'єднання',
                          callback_data='t1_7')],
    [InlineKeyboardButton(text='🔙Назад', callback_data='main')],

]

payment = [

    [InlineKeyboardButton(text='В який період необхідно оплачувати послуги?',
                          callback_data='p1_1')],
    [InlineKeyboardButton(text='Як списуються кошти з особового рахунку?',
                          callback_data='p1_2')],
    [InlineKeyboardButton(text='Де можна подивитися деталізацію рахунка?',
                          callback_data='p1_3')],
    [InlineKeyboardButton(text='Як перевірити баланс?',
                          callback_data='p1_4')],
    [InlineKeyboardButton(text='Як поповнити рахунок?',
                          callback_data='p1_5')],
    [InlineKeyboardButton(text='Куди необхідно звернутися, якщо платіж не дійшов або оплачений невірно?',
                          callback_data='p1_6')],
    [InlineKeyboardButton(text='Платив через термінал, але чек термінал не видав і гроші на рахунок не надійшли. Що робити?',
                          callback_data='p1_7')],
    [InlineKeyboardButton(text='Звідки у мене мінус на рахунку?',
                          callback_data='p1_8')],
    [InlineKeyboardButton(text='🔙Назад', callback_data='main')],

]
