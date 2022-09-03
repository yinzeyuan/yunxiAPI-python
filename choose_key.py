public_key = "7d06a110e9e20a684e02934549db1d3d"  # 公用API，不定期更换。
personal_key = ""  # 个人API，如需使用请自行填入


def choose_key(public_key=public_key, personal_key=personal_key):
    if personal_key == "":
        return public_key
    else:
        return personal_key
