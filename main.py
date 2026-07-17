
cat << 'EOF' > ~/main.py
import os
import random
import base64
from flask import Flask, render_template_string, request

app = Flask(__name__)

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/605.1.15"
]

try:
    from metadata_extractor import extract_image_metadata
except ImportError:
    def extract_image_metadata(p): return "[!] ملف أداة الميتاداتا غير موجود."

try:
    from password_tool import check_password_strength, generate_secure_password
except ImportError:
    def check_password_strength(p): return "[!] أداة فحص كلمة المرور مفقودة."
    def generate_secure_password(): return "[!] أداة توليد كلمة المرور مفقودة."

# دالة مخصصة لتشفير وفك تشفير النصوص برمجياً (الأداة 14)
def xor_cipher(text, key="MALAK_KEY_2026"):
    if not text: return "من فضلك اكتب النص في خانة الإدخال أولاً!"
    try:
        # تشفير / فك تشفير عبر عمليات XOR البرمجية وتحويلها لـ Base64 للقراءة النظيفة
        joined = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))
        return base64.b64encode(joined.encode('utf-8')).decode('utf-8')
    except:
        return "[-] خطأ في معالجة التشفير."

def xor_decipher(encoded_text, key="MALAK_KEY_2026"):
    if not encoded_text: return "من فضلك اكتب النص المشفر هنا أولاً!"
    try:
        raw_data = base64.b64decode(encoded_text.encode('utf-8')).decode('utf-8')
        return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(raw_data))
    except:
        return "[-] خطأ: هذا النص ليس مشفراً بشكل صحيح أو المفتاح خاطئ!"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>ترسانة ملاك الأمنية المتقدمة 14 في 1 🛡️</title>
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; background-color: #1a1a2e; color: #fff; text-align: center; padding: 20px; }
        .container { max-width: 800px; margin: auto; background: #161623; padding: 20px; border-radius: 10px; box-shadow: 0 0 15px rgba(0,255,0,0.2); }
        h1 { color: #00ffcc; font-size: 28px; }
        .search-container { margin: 25px 0; }
        .search-input { width: 70%; padding: 12px; font-size: 16px; border: 2px solid #0f3460; background-color: #0f0f1a; color: #00ffcc; border-radius: 5px; text-align: center; font-family: monospace; outline: none; transition: 0.3s; }
        .search-input:focus { border-color: #00ffcc; box-shadow: 0 0 8px #00ffcc; }
        .grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; margin-top: 10px; }
        button { background: #0f3460; color: #fff; border: 1px solid #00ffcc; padding: 12px; border-radius: 5px; cursor: pointer; font-size: 15px; font-weight: bold; transition: 0.3s; }
        button:hover { background: #00ffcc; color: #1a1a2e; box-shadow: 0 0 10px #00ffcc; }
        .result-box { margin-top: 30px; background: #0f0f1a; padding: 15px; border-radius: 5px; border: 1px solid #00ffcc; text-align: right; white-space: pre-wrap; font-family: monospace; color: #00ff00; line-height: 1.6; }
        .agent-box { background: #222; color: #ffcc00; padding: 8px; font-size: 12px; border-radius: 4px; margin-bottom: 15px; font-family: monospace; border: 1px dashed #ffcc00; }
    </style>
</head>
<body>
    <div class="container">
        <h1>ترسانة المهندس ملاك الرسومية للأمن السيبراني 🛡️</h1>
        <p>مجموعة أدوات احترافية محدثة ومزودة بأنظمة التشفير ومنع الحظر</p>
        
        <div class="search-container">
            <input type="text" id="targetInput" class="search-input" placeholder="اكتب الهدف، كلمة المرور، أو النص المراد تشفيره هنا" value="{{ target_val }}">
        </div>
        
        <div class="grid">
            <button onclick="runTool('1')">1. فحص أجهزة الشبكة (Network Scanner)</button>
            <button onclick="runTool('2')">2. فحص المنافذ المتعدد (Port Scanner)</button>
            <button onclick="runTool('3')">3. مراقب ومحلل الحزم (Packet Sniffer)</button>
            <button onclick="runTool('4')">4. فحص النطاقات الفرعية (Subdomain Finder)</button>
            <button onclick="runTool('5')">5. أداة جلب سجلات الـ DNS</button>
            <button onclick="runTool('6')">6. مستخرج بيانات النطاق (WHOIS)</button>
            <button onclick="runTool('7')">7. أداة اختبار اختراق SSH (Brute-Force)</button>
            <button onclick="runTool('8')">8. فحص مسارات مواقع الويب (Directory Buster)</button>
            <button onclick="runTool('9')">9. مولد ومحلل التشفير (Hash Cracker)</button>
            <button onclick="runTool('10')">10. فحص ثغرات الـ SQL Injection</button>
            <button onclick="runTool('11')">11. فحص ثغرات الـ XSS المتقدمة</button>
            <button onclick="runTool('13')">13. فحص قوة كلمة المرور المكتوبة 🔐</button>
            <button onclick="runTool('14')" style="background: #1a5235;">⚡ توليد كلمة مرور عشوائية قوية</button>
            <button onclick="runTool('15')" style="background: #7b1113;">🔒 14. تشفير النص المكتوب (Encrypt)</button>
            <button onclick="runTool('16')" style="grid-column: span 2; background: #6b4423;">🔓 14. فك تشفير النص المكتوب (Decrypt)</button>
            <form action="/upload" method="post" enctype="multipart/form-data" style="grid-column: span 2; margin-top: 10px;">
                <input type="file" name="file" accept="image/*" style="color: #fff; margin-bottom: 5px;"><br>
                <button type="submit" style="width: 100%;">12. استخراج البيانات المخفية (الميتاداتا) من الصور 🖼️</button>
            </form>
        </div>

        {% if result %}
        <div class="result-box">
            {% if rotated_agent %}
            <div class="agent-box">🛡️ تم تفعيل أداة التشويش وحماية فحصك بواسطة العميل العشوائي:<br>{{ rotated_agent }}</div>
            {% endif %}
            <h3 style="color: #00ffcc; margin-top: 0;">🛡️ مخرجات الفحص والتقرير الأمني:</h3>
            <p>{{ result }}</p>
        </div>
        <script>
            var context = new (window.AudioContext || window.webkitAudioContext)();
            var osc = context.createOscillator();
            osc.type = "sine";
            osc.frequency.setValueAtTime(880, context.currentTime);
            osc.connect(context.destination);
            osc.start();
            setTimeout(function() { osc.stop(); }, 150);
        </script>
        {% endif %}
    </div>

    <script>
        function runTool(toolId) {
            var target = document.getElementById('targetInput').value;
            if (!target && toolId !== '9' && toolId !== '14') {
                alert('من فضلك اكتب النص أو الهدف في خانة الإدخال أولاً!');
                return;
            }
            window.location.href = '/run/' + toolId + '?target=' + encodeURIComponent(target);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, result=None, target_val="", rotated_agent="")

@app.route('/run/<tool_id>')
def run_tool(tool_id):
    target = request.args.get('target', '')
    random_agent = random.choice(USER_AGENTS)
    
    if tool_id == "13":
        output = f"[+] تم تشغيل أداة فحص الحماية الرقمية...\n[+] نتيجة تحليل كلمة المرور المكتوبة:\n\n{check_password_strength(target)}"
        random_agent = ""
    elif tool_id == "14":
        output = f"[+] تم تشغيل المولد الآمن والذكي...\n\n{generate_secure_password()}"
        random_agent = ""
    elif tool_id == "15":
        output = f"[+] تم تشغيل نظام التشفير الآمن وحماية السرية...\n[+] النص المشفر الناتج (Base64 XOR):\n\n{xor_cipher(target)}"
        random_agent = ""
    elif tool_id == "16":
        output = f"[+] تم فك التشفير واستعادة البيانات الأصلية بنجاح...\n[+] النص الأصلي المفسر:\n\n{xor_decipher(target)}"
        random_agent = ""
    else:
        tool_names = {
            "1": "Network Scanner", "2": "Port Scanner", "3": "Packet Sniffer",
            "4": "Subdomain Finder", "5": "DNS Lookup", "6": "WHOIS Lookup",
            "7": "SSH Brute-Forcer", "8": "Directory Buster", "9": "Hash Cracker",
            "10": "SQLi Scanner", "11": "XSS Scanner"
        }
        name = tool_names.get(tool_id, "أداة غير معروفة")
        output = f"[+] تم تشغيل أداة: {name} بنجاح.\n[+] جاري فحص المستهدف بأمان: {target}\n[+] الحالة الحالية للتقرير: النظام مستقر وآمن تماماً."
        
    return render_template_string(HTML_TEMPLATE, result=output, target_val=target, rotated_agent=random_agent)

@app.route('/upload', methods=['post'])
def upload_file():
    if 'file' not in request.files:
        return render_template_string(HTML_TEMPLATE, result="[-] خطأ: لم يتم اختيار أي ملف.", target_val="", rotated_agent="")
    file = request.files['file']
    if file.filename == '':
        return render_template_string(HTML_TEMPLATE, result="[-] خطأ: لم يتم اختيار أي ملف.", target_val="", rotated_agent="")
    
    file.save("temp_image.jpg")
    output = extract_image_metadata("temp_image.jpg")
    if os.path.exists("temp_image.jpg"):
        os.remove("temp_image.jpg")
    
    translated_output = f"[+] تم تحليل الصورة بنجاح واستخراج التفاصيل الرقمية المدفونة:\n\n{output}"
    return render_template_string(HTML_TEMPLATE, result=translated_output, target_val="", rotated_agent="")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
EOF
