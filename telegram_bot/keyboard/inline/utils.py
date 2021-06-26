from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram_bot.commands.manage_data import CONFIRM_DECLINE_BROADCAST, CONFIRM_BROADCAST, DECLINE_BROADCAST
from telegram_bot.commands.static_text import confirm_broadcast, decline_broadcast


def keyboard_confirm_decline_broadcasting():
    buttons = [[
        InlineKeyboardButton(confirm_broadcast, callback_data=f'{CONFIRM_DECLINE_BROADCAST}{CONFIRM_BROADCAST}'),
        InlineKeyboardButton(decline_broadcast, callback_data=f'{CONFIRM_DECLINE_BROADCAST}{DECLINE_BROADCAST}')
    ]]

    return InlineKeyboardMarkup(buttons)


def make_addresses_inline_keyboard(customers) -> InlineKeyboardMarkup:
    addresses_buttons = []
    for customer in customers:
        addresses_buttons.append(
            [InlineKeyboardButton(text=f'🔹{customer.login}\n'
                                       f'🏠{customer.street} {customer.build} кв {customer.apartment}',
                                  callback_data=f'{customer.login}')]
        )

    return InlineKeyboardMarkup(addresses_buttons, row_width=1)
