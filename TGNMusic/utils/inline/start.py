from pyrogram.types import InlineKeyboardButton

import config
from TGNMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["♨️𝐀𝐃𝐃 𝐌𝐄 𝐈𝐍 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏♨️"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["𝐒𝐔𝐏𝐏𝐎𝐑𝐓"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["♨️𝐀𝐃𝐃 𝐌𝐄 𝐈𝐍 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏♨️"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["♨️𝐂𝐎𝐌𝐌𝐀𝐍𝐃♨️"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["♨️𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑♨️"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["♨️𝐒𝐔𝐏𝐏𝐎𝐑𝐓♨️"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["♨️𝐂𝐇𝐀𝐍𝐍𝐄𝐋♨️"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["♨️𝐒𝐎𝐔𝐑𝐂𝐄♨️"], url=config.UPSTREAM_REPO),
        ],
    ]
    return buttons
