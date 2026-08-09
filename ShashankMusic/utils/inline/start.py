python3 << 'PYEOF'
import re

with open("ShashankMusic/utils/inline/start.py") as f:
    content = f.read()

old = '''            InlineKeyboardButton(
                text=_["S_B_6"], 
                url="https://t.me/Il_Ravan_bhai_ll",
                style=group_style
            ),
        ],'''

new = '''            InlineKeyboardButton(
                text=_["S_B_6"], 
                url="https://t.me/Il_Ravan_bhai_ll",
                style=group_style
            ),
        ],
        [
            InlineKeyboardButton(
                text="Developer",
                url=config.DEVELOPER_URL,
                style=alone_style
            ),
        ],'''

content = content.replace(old, new, 1)

with open("ShashankMusic/utils/inline/start.py", "w") as f:
    f.write(content)

print("Done")
PYEOF