import re
import secrets
import string

def check_password_strength(password):
    if not password: return "من فضلك اكتب كلمة المرور أولاً!"
    if len(password) < 8: return "❌ ضعيفة جداً! يجب أن تكون 8 أحرف على الأقل."
    score = 0
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"\d", password): score += 1
    if re.search(r"[ !@#$%^&*(),.?\":{}|<>]", password): score += 1
    if score == 4 and len(password) >= 12: return "🟢 قوية جداً ومثالية!"
    elif score >= 3: return "🟡 متوسطة الأمان."
    return "🔴 ضعيفة! يسهل اختراقها."

def generate_secure_password(length=16):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(secrets.choice(characters) for _ in range(length))
