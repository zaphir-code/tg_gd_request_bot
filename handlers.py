from tg_api import dp
from aiogram import types
import gd_api
from gd.errors import MissingAccess
from helpers import isstring_int
import captions


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply('Hello! This is bot for sending GD level requests!')


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply('If you want to send a level request, then write:\n<i>/lvl_req {Your lvl ID}</i>',
                        parse_mode='html')


@dp.message_handler(commands=['lvl_req'])
async def gd_req_lvl(message: types.Message):
    message_text = message.text.split()
    if len(message_text) > 2:
        await message.reply('<strong>You entered wrong level id</strong>', parse_mode='html')
    elif len(message_text) < 2:
        await message.reply('<strong>Please, enter level id</strong>', parse_mode='html')
    else:
        if not isstring_int(message_text[1]):
            await message.reply('<strong>You entered wrong level id</strong>', parse_mode='html')
        else:
            try:
                level = await gd_api.client.get_level(int(message_text[1]))
                await message.reply(f'''
{captions.lvl_creator}{level.creator.name.capitalize()}

{captions.lvl_name}{level.name.capitalize()}

{captions.lvl_description}{level.description.capitalize()}

{captions.lvl_difficulty}{level.difficulty.name.capitalize().replace('_', ' ')}

{captions.lvl_stars}{level.stars}

{captions.lvl_coins}{level.coins}

{captions.lvl_id}{level.id}
                        ''', parse_mode='html')
            except MissingAccess:
                await message.reply('<strong>You entered wrong level id</strong>', parse_mode='html')
