import random, base64


數量 = 10  # 換成數量
用戶id = "1234567890"  # 換成用戶id

def generate_token(id:str):
        characs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        characs2 = '01zr'
        id_encoded = base64.b64encode(bytes(id, 'utf-8'))
        random1 = f".X{random.choices(characs2, k=1)}{random.choices(characs, k=4)}.{random.choices(characs, k=27)}"
        random2 = random1.replace("'", "")
        random3 = random2.replace(",", "")
        random4 = random3.replace("[", "")
        random5 = random4.replace("]", "")
        random_final = random5.replace(" ", "")
        random_token = (id_encoded.decode('utf-8') + random_final).replace("=", "")
        return random_token


for i in range(數量):
    token = generate_token(用戶id)
    print(token)
