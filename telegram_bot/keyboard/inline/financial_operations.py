from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def financial_operations_keyboard(string) -> InlineKeyboardMarkup:
    buttons = globals()[string]
    return InlineKeyboardMarkup(buttons, row_width=1)


all_financial_operations = [
    [InlineKeyboardButton(text='Оплати', callback_data='fpayments')],
    [InlineKeyboardButton(text='Зняття грошей', callback_data='fwithdraws')],
]

return_back_finance = [
    [InlineKeyboardButton(text='🔙 Назад', callback_data='all_financial_operations')]
]
