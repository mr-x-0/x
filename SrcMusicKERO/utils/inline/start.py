from pyrogram.types import InlineKeyboardButton

import config
from SrcMusicKERO import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="aDD Me To Your Groups", url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="aDD Me To Your Groups",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        
        [
            InlineKeyboardButton(text="𝗗𝗲𝘃 .", url=f"https://t.me/D_S_IS") ,
        ],
        [   
            InlineKeyboardButton(text="𝗦𝗼𝘂𝗿𝗰𝗲 .", url=f"https://t.me/SOURCEZE") , 
        ],
    ]
    return buttons
