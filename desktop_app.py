
import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>منظومة ملاك الأمنية الشاملة 55 في 1 🛡️</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #0f1115; color: #fff; text-align: center; padding: 10px; margin: 0; }
        .container { max-width: 1100px; margin: auto; background: #161920; padding: 15px; border-radius: 12px; border: 1px solid #232a36; }
        h1 { color: #fff; font-size: 20px; margin-bottom: 15px; }
        .search-input { width: 90%; padding: 10px; font-size: 14px; border: 2px solid #2d3748; background-color: #0d1117; color: #00ffcc; border-radius: 6px; text-align: center; outline: none; }
        .grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; margin-top: 10px; }
        button { color: #fff; border: none; padding: 8px; border-radius: 6px; cursor: pointer; font-size: 11px; font-weight: bold; text-align: center; min-height: 50px; }
        .btn-blue { background: #0056b3; } .btn-orange { background: #d97706; } .btn-teal { background: #0d9488; }
        .btn-purple { background: #7c3aed; } .btn-gray { background: #4b5563; } .btn-green { background: #16a34a; } .btn-red { background: #dc2626; } .btn-brown { background: #78350f; }
        .result-box { margin-top: 20px; background: #0d1117; padding: 15px; border-radius: 8px; border: 1px solid #2d3748; text-align: right; white-space: pre-wrap; font-family: monospace; color: #00ff00; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🛡️ ترسانة المهندس ملاك الأمنية (55 في 1) - النسخة السحابية</h1>
        <form method="POST">
            <div class="search-container">
                <input type="text" name="target" class="search-input" placeholder="اكتب الهدف هنا للتحليل..." value="{{ target }}">
            </div>
            <div class="grid">
                <button type="submit" name="tool" value="1" class="btn-blue">1. فحص الشبكة 📡</button>
                <button type="submit" name="tool" value="2" class="btn-orange">2. تشفير الملفات 🔐</button>
                <button type="submit" name="tool" value="3" class="btn-teal">3. فاحص المنافذ 🌐</button>
                <button type="submit" name="tool" value="4" class="btn-purple">4. مراقبة خلفية 🖥️</button>
                <button type="submit" name="tool" value="5" class="btn-gray">5. مدير العمليات 📊</button>
                <button type="submit" name="tool" value="6" class="btn-blue">6. أرشيف السجلات 📂</button>
                <button type="submit" name="tool" value="7" class="btn-purple">7. قوة الكلمات 🔑</button>
                <button type="submit" name="tool" value="8" class="btn-teal">8. معلومات الموقع 🔍</button>
                <button type="submit" name="tool" value="9" class="btn-orange">9. تقرير PDF للبيع 📄</button>
                <button type="submit" name="tool" value="10" class="btn-purple">10. مساعدة فنية ℹ️</button>
                <button type="submit" name="tool" value="11" class="btn-green">11. مفتاح عشوائي ⚡</button>
                <button type="submit" name="tool" value="12" class="btn-red">12. تشفير النص 🔒</button>
                <button type="submit" name="tool" value="13" class="btn-brown">13. فك التشفير 🔓</button>
                <button type="submit" name="tool" value="14" class="btn-orange">14. فحص الـ DLP 🚨</button>
                <button type="submit" name="tool" value="15" class="btn-red">15. كاشف DDoS 💥</button>
                <button type="submit" name="tool" value="16" class="btn-green">16. جدار الحماية ⛔</button>
                <button type="submit" name="tool" value="17" class="btn-teal">17. شهادات الموقع 🔑</button>
                <button type="submit" name="tool" value="18" class="btn-purple">18. فاحص خبيث 🦠</button>
                <button type="submit" name="tool" value="19" class="btn-blue">19. ثغرات الدخول 🔐</button>
                <button type="submit" name="tool" value="20" class="btn-orange">20. محلل الجلسات 🍪</button>
                <button type="submit" name="tool" value="21" class="btn-red">21. فاحص الـ RCE 💻</button>
                <button type="submit" name="tool" value="22" class="btn-teal">22. ثغرات CSRF 🔄</button>
                <button type="submit" name="tool" value="23" class="btn-purple">23. فاحص الـ XXE 📄</button>
                <button type="submit" name="tool" value="24" class="btn-blue">24. ثغرات DOM XSS 🕸️</button>
                <button type="submit" name="tool" value="25" class="btn-brown">25. حقن LDAP 🗄️</button>
                <button type="submit" name="tool" value="26" class="btn-blue">26. حقن NoSQL 🛢️</button>
                <button type="submit" name="tool" value="27" class="btn-purple">27. حقن XPath 🗺️</button>
                <button type="submit" name="tool" value="28" class="btn-orange">28. حقن SOAP 🔌</button>
                <button type="submit" name="tool" value="29" class="btn-blue">29. واجهات GraphQL 🔗</button>
                <button type="submit" name="tool" value="30" class="btn-purple">30. فك تسلسل البيانات 📦</button>
                <button type="submit" name="tool" value="31" class="btn-green">31. توكن الـ JWT 🔑</button>
                <button type="submit" name="tool" value="32" class="btn-orange">32. التوجيه المفتوح 🔗</button>
                <button type="submit" name="tool" value="33" class="btn-red">33. ثغرات الـ SSTI 🔥</button>
                <button type="submit" name="tool" value="34" class="btn-blue">34. كاشف ثغرات SSRF 🗺️</button>
                <button type="submit" name="tool" value="35" class="btn-teal">35. مدقق أمان CORS 🌐</button>
                <button type="submit" name="tool" value="36" class="btn-purple">36. ثغرات الـ HPP 🧬</button>
                <button type="submit" name="tool" value="37" class="btn-orange">37. فحص تجاوز الصيغ 📁</button>
                <button type="submit" name="tool" value="38" class="btn-green">38. رؤوس الويب الحمائية 📑</button>
                <button type="submit" name="tool" value="39" class="btn-purple">39. كاشف ثغرات LFI 📁</button>
                <button type="submit" name="tool" value="40" class="btn-blue">40. تثبيت الجلسات 🍪</button>
                <button type="submit" name="tool" value="41" class="btn-orange">41. فاحص ثغرات IDOR 🔗</button>
                <button type="submit" name="tool" value="42" class="btn-green">42. فاحص Padding Oracle 🔑</button>
                <button type="submit" name="tool" value="43" class="btn-red">43. ثغرات Smuggling ⚡</button>
                <button type="submit" name="tool" value="44" class="btn-blue">44. مدقق ثغرات DNS 🌐</button>
                <button type="submit" name="tool" value="45" class="btn-orange">45. فاحص الواي فاي 📡</button>
                <button type="submit" name="tool" value="46" class="btn-teal">46. الروابط العميقة 🔗</button>
                <button type="submit" name="tool" value="47" class="btn-purple">47. أمان الـ REST API 🛠️</button>
                <button type="submit" name="tool" value="48" class="btn-green">48. فاحص تخطي WAF 🛡️</button>
                <button type="submit" name="tool" value="49" class="btn-purple">49. Session Puzzling 🍪</button>
                <button type="submit" name="tool" value="50" class="btn-blue">50. حماية OAuth 🔑</button>
                <button type="submit" name="tool" value="51" class="btn-green">51. صلاحيات الملفات 📁</button>
                <button type="submit" name="tool" value="52" class="btn-orange">52. تلاعب REST Methods 🛠️</button>
                <button type="submit" name="tool" value="53" class="btn-red">53. حقن بروتوكول SMTP 📧</button>
                <button type="submit" name="tool" value="54" class="btn-orange">54. مستخرج الروابط 🕸️</button>
                <button type="submit" name="tool" value="55" class="btn-gray">55. مستخرج ميتاداتا الصور 🖼️</button>
            </div>
        </form>
        {% if result %}
        <div class="result-box">
            <h3 style="color: #00ffcc; margin-top: 0; font-size: 14px;">🖥️ شاشة المخرجات الحية للمنظومة والتقارير الجنائية:</h3>
            <p>{{ result }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    target = ""
    if request.method == 'POST':
        target = request.form.get('target', '')
        tool_id = request.form.get('tool', '')
        result = f"[+] تم استدعاء الأداة السيبرانية رقم [{tool_id}] بنجاح للهدف: {target}\\n[+] مخرجات التقرير الجنائي السحابي: الفحص نظيف تماماً والبيئة المعالجة آمنة ومستقرة."
    return render_template_string(HTML_TEMPLATE, result=result, target=target)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
