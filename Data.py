from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Bot ini khusus pengambilan String Session, jika kamu masih ragu silahkan!
1) Blok bot ini
2) Hapus pesan bot ini

Budayakan membaca!
Create by @shockingsoda
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("Start Generating Session", callback_data="generate")],
        [InlineKeyboardButton(text="Return Home", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("Start Generating Session", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("Start Generating Session", callback_data="generate")],
        [InlineKeyboardButton("Support Channel", url="https://t.me/zyrosofficial")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("About", callback_data="about")
        ],
        [InlineKeyboardButton("Support Group", url="https://t.me/zyrosupdates")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**About This Bot** 

Bot khusus pengambilan String Session Telethon dan Pyrogram, create by @shockingsoda

Channel : [Support Channel](https://t.me/zyrosofficial)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @zyrosofficial
    """
