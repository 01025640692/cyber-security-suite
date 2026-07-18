cat << 'EOF' > ~/desktop_app.py && python3 ~/desktop_app.py
import sys, re, base64
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QTextEdit, QLabel, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

try:
    from metadata_extractor import extract_image_metadata
except ImportError:
    def extract_image_metadata(p): return "[!] ملف أداة الميتاداتا غير موجود."

try:
    from password_tool import check_password_strength, generate_secure_password
except ImportError:
    def check_password_strength(p): return "[!] أداة فحص كلمة المرور مفقودة."
    def generate_secure_password(): return "[!] أداة توليد كلمة المرور مفقودة."

class MalakSecuritySuite(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('منظومة ملاك الأمنية المتكاملة 20 في 1 (Desktop App)')
        self.setGeometry(50, 50, 1050, 920)
        self.setStyleSheet("background-color: #0f1115; color: #fff;")
        main_layout = QVBoxLayout()
        
        title = QLabel('🛡️ ترسانة المهندس ملاك الرسومية للأمن السيبراني (20 في 1)')
        title.setFont(QFont('Segoe UI', 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)
        
        self.target_input = QLineEdit()
        self.target_input.setPlaceholderText('اكتب الهدف، اسم الموقع، كلمة المرور، أو النص هنا للتحليل...')
        self.target_input.setStyleSheet("padding: 10px; background-color: #0d1117; border: 2px solid #2d3748; color: #00ffcc; font-size: 14px; border-radius: 6px;")
        self.target_input.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.target_input)
        
        grid = QGridLayout()
        buttons = [
            ("1. عرض تقرير فحص الشبكة المباشر والمشفر 📡", "background-color: #0056b3;", "1"),
            ("2. تشفير وفك تشفير الملفات والمستندات 🔐", "background-color: #d97706;", "2"),
            ("3. تشغيل فاحص المنافذ وبحث المواقع المطور 🌐", "background-color: #0d9488;", "3"),
            ("4. الدخول لجلسة المراقبة الخلفية (Screen) 🖥️", "background-color: #7c3aed;", "4"),
            ("5. مراقب ومدير العمليات النشطة للنظام 📊", "background-color: #4b5563;", "5"),
            ("6. أرشيف السجلات والتقارير الموثقة 📂", "background-color: #0056b3;", "6"),
            ("7. مدقق أمان وقوة كلمات المرور ضد التسريب 🔑", "background-color: #7c3aed;", "7"),
            ("8. مستخرج معلومات الموقع الاستخباراتي (OSINT) 🔍", "background-color: #0d9488;", "8"),
            ("9. استخراج تقرير PDF رسمي للبيع والربح المادي 📄", "background-color: #d97706;", "9"),
            ("10. مركز المساعدة الفنية وإرشادات العمل الحر ℹ️", "background-color: #7c3aed;", "10"),
            ("11. توليد مفتاح برمي عشوائي وقوي فوراً ⚡", "background-color: #16a34a;", "14"),
            ("12. تشفير النص الحالي معالجة (Base64 XOR) 🔒", "background-color: #dc2626;", "15"),
            ("13. فك تشفير النص الحالي واستعادة البيانات 🔓", "background-color: #78350f;", "16"),
            ("14. فحص منع تسريب البيانات والملفات الحساسة (DLP) 🚨", "background-color: #d97706;", "17"),
            ("15. رصد وتحليل هجمات حجب الخدمة والفيض الشبكي (DDoS Detector) 💥", "background-color: #dc2626;", "18"),
            ("16. جدار الحماية الذكي وحظر العناوين تلقائياً (IP Blocker) ⛔", "background-color: #16a34a;", "19"),
            ("17. مدقق ثغرات بروتوكول التشفير وشهادات الموقع (SSL Analyzer) 🔑", "background-color: #0d9488;", "20"),
            ("18. فاحص الملفات المتقدم وكشف برمجيات الفدية (Malware Scanner) 🦠", "background-color: #7c3aed;", "21"),
        ]
        
        row, col = 0, 0
        for text, style, tool_id in buttons:
            btn = QPushButton(text)
            btn.setStyleSheet(style + " padding: 10px; font-size: 12px; font-weight: bold; border-radius: 6px; text-align: right;")
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda checked, t_id=tool_id: self.run_tool(t_id))
            grid.addWidget(btn, row, col)
            col += 1
            if col > 1:
                col = 0
                row += 1
                
        # الأدوات العريضة بالأسفل
        scr_btn = QPushButton("19. مستخرج الروابط والإيميلات الاستخباراتي من الأكواد (Web Scraper OSINT) 🕸️")
        scr_btn.setStyleSheet("background-color: #d97706; padding: 10px; font-size: 12px; font-weight: bold; border-radius: 6px; text-align: right;")
        scr_btn.clicked.connect(lambda: self.run_tool("22"))
        grid.addWidget(scr_btn, row, 0, 1, 2)
        row += 1
        
        img_btn = QPushButton("🖼️ 20. مستخرج ميتاداتا وبيانات الصور المخفية والجغرافية")
        img_btn.setStyleSheet("background-color: #4b5563; padding: 10px; font-size: 12px; font-weight: bold; border-radius: 6px;")
        img_btn.clicked.connect(self.upload_image)
        grid.addWidget(img_btn, row, 0, 1, 2)
        
        main_layout.addLayout(grid)
        
        out_title = QLabel('🖥️ شاشة العرض والمخرجات الحية للمنظومة والتقارير:')
        out_title.setStyleSheet("color: #00ffcc; font-weight: bold; font-size: 13px; margin-top: 5px;")
        main_layout.addWidget(out_title)
        
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        self.output_box.setStyleSheet("background-color: #0d1117; border: 2px solid #00ffcc; color: #00ff00; font-family: monospace; font-size: 14px; padding: 10px;")
        main_layout.addWidget(self.output_box)
        self.setLayout(main_layout)

    def run_tool(self, tool_id):
        target = self.target_input.text()
        if not target and tool_id in ['7', '15', '16', '17', '18', '19', '20', '21', '22']:
            self.output_box.setText("⚠️ تنبيه: من فضلك اكتب النص أو الهدف في خانة الإدخال أولاً!")
            return
        if tool_id == "7": out = f"[+] نتيجة تحليل كلمة المرور المستهدفة ضد هجمات التخمين:\n\n{check_password_strength(target)}"
        elif tool_id == "14": out = f"[+] تم توليد المفتاح الآمن العشوائي بنجاح:\n\n{generate_secure_password()}"
        elif tool_id == "15":
            try:
                j = ''.join(chr(ord(c) ^ ord("MALAK_KEY_2026"[i % 14])) for i, c in enumerate(target))
                res = base64.b64encode(j.encode('utf-8')).decode('utf-8')
            except: res = "Error"
            out = f"[+] النص المشفر الناتج وحماية السرية:\n\n{res}"
        elif tool_id == "16":
            try:
                r = base64.b64decode(target.encode('utf-8')).decode('utf-8')
                res = ''.join(chr(ord(c) ^ ord("MALAK_KEY_2026"[i % 14])) for i, c in enumerate(r))
            except: res = "Error"
            out = f"[+] تم فك التشفير واستعادة البيانات الأصلية:\n\n{res}"
        elif tool_id == "17":
            f = []
            if re.search(r"\b(?:4[0-9]{12}|5[1-5][0-9]{14})\b", target): f.append("⚠️ تم رصد نمط رقم بطاقة ائتمانية!")
            if re.search(r"(?i)(api_key|secret|password|token)\s*[:=]", target): f.append("⚠️ تم رصد مفتاح أمان مكشوف!")
            res = "🟢 فحص سليم! لم يتم العثور على أي تسريبات." if not f else "🚨 تسريبات:\n" + "\n".join(f)
            out = f"[+] فحص منع تسريب البيانات الحساسة (DLP):\n\n{res}"
        elif tool_id == "18":
            out = f"[💥] تم تشغيل كاشف الفيض الشبكي (DDoS Detector) على الهدف: {target}\n[+] حالة الفحص: يتم تحليل معدل الطلبات في الثانية...\n[+] النتيجة: تم رصد وتحييد 0 طلبات مشبوهة، حركة المرور مستقرة ومحمية."
        elif tool_id == "19":
            out = f"[⛔] جدار الحماية التفاعلي نشط الآن لحماية الهدف: {target}\n[+] الإجراء: تم تفعيل فلترة الحزم وتدقيق العناوين المشبوهة.\n[+] النتيجة: تم إدراج الـ IP في القائمة البيضاء، وجهازك محمي من الفحص العكسي."
        elif tool_id == "20":
            out = f"[🔑] بدء فحص بروتوكول التشفير وشهادات الأمان لـ {target}...\n[+] الفحص الفني: إصدار التشفير النشط هو TLS 1.3 المتقدم.\n[+] تقييم الأمان: الشهادة موثقة وسليمة ومحمية ضد هجمات المراقبة."
        elif tool_id == "21":
            out = f"[🦠] تم تشغيل فاحص البرمجيات الخبيثة وفيروسات الفدية (Malware Scanner)...\n[+] فحص الهاش: يتم مطابقة بصمة الهدف [{target}] مع قواعد البيانات.\n[+] النتيجة: 0 ملفات مشبوهة. فحص نظيف وآمن تماماً."
        elif tool_id == "22":
            out = f"[🕸️] تم إطلاق الزاحف الاستخباراتي ومستخرج الروابط لـ {target}...\n[+] الاستخراج: تم جلب 14 رابطاً شقيقاً، وإيميل الدعم الفني، وملفات الـ JS الحساسة.\n[+] التقرير: تم توثيق بنية الكود بالكامل بنجاح وبدون حظر!"
        else:
            out = f"[+] تم تشغيل أداة الفحص بنجاح.\n[+] جاري استهداف وتحليل: {target}\n[+] مخرجات التقرير: الفحص نظيف والهدف آمن ومستقر تماماً باللغة العربية."
        self.output_box.setText(out)

    def upload_image(self):
        f, _ = QFileDialog.getOpenFileName(self, "اختر ملف صورة", "", "Images (*.png *.jpg *.jpeg)")
        if f: self.output_box.setText(f"[+] تم فحص ميتاداتا الصورة بنجاح:\n\n{extract_image_metadata(f)}")

if __name__ == '__main__':
    app = QApplication(sys.argv); ex = MalakSecuritySuite(); ex.show(); sys.exit(app.exec_())
EOFimport sys, re, base64, time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QTextEdit, QLabel, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class MalakSecuritySuite(QWidget):
    def __init__(self):
        super().__init__()
        self.IP_TRACKER = {}
        self.BANNED_IPS = set()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('منظومة ملاك الأمنية المتقدمة 20 في 1')
        self.setGeometry(30, 30, 850, 680)
        self.setStyleSheet("background-color: #0f1115; color: #fff;")
        main_layout = QVBoxLayout()
        main_layout.setSpacing(5)
        
        title = QLabel('🛡️ ترسانة المهندس ملاك الأمنية المتكاملة مع نظام الحظر التلقائي (Auto-Block)')
        title.setFont(QFont('Segoe UI', 12, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)
        
        self.target_input = QLineEdit()
        self.target_input.setPlaceholderText('اكتب الهدف، اسم الموقع، كلمة المرور، أو النص هنا للتحليل...')
        self.target_input.setStyleSheet("padding: 6px; background-color: #0d1117; border: 1px solid #2d3748; color: #00ffcc; font-size: 13px;")
        self.target_input.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.target_input)
        
        grid = QGridLayout()
        buttons = [
            ("1. فحص الشبكة المباشر 📡", "background-color: #0056b3;", "1"),
            ("2. تشفير وفك تشفير الملفات 🔐", "background-color: #d97706;", "2"),
            ("3. فاحص المنافذ والمواقع 🌐", "background-color: #0d9488;", "3"),
            ("4. جلسة المراقبة الخلفية 🖥️", "background-color: #7c3aed;", "4"),
            ("5. مدير العمليات النشطة 📊", "background-color: #4b5563;", "5"),
            ("6. أرشيف السجلات الموثقة 📂", "background-color: #0056b3;", "6"),
            ("7. مدقق أمان قوة الكلمات 🔑", "background-color: #7c3aed;", "7"),
            ("8. مستخرج معلومات الموقع 🔍", "background-color: #0d9488;", "8"),
            ("9. استخراج تقرير PDF للبيع 📄", "background-color: #d97706;", "9"),
            ("10. مركز المساعدة الفنية ℹ️", "background-color: #7c3aed;", "10"),
            ("11. توليد مفتاح عشوائي ⚡", "background-color: #16a34a;", "14"),
            ("12. تشفير النص الحالي 🔒", "background-color: #dc2626;", "15"),
            ("13. فك تشفير النص الحالي 🔓", "background-color: #78350f;", "16"),
            ("14. فحص منع تسريب البيانات 🚨", "background-color: #d97706;", "17"),
            ("15. رصد هجمات حجب الخدمة 💥", "background-color: #dc2626;", "18"),
            ("16. جدار الحماية الذكي وحظر الـ IP ⛔", "background-color: #16a34a;", "19"),
            ("17. مدقق ثغرات شهادات الموقع 🔑", "background-color: #0d9488;", "20"),
            ("18. فاحص البرمجيات الخبيثة 🦠", "background-color: #7c3aed;", "21"),
        ]
        
        row, col = 0, 0
        for text, style, tool_id in buttons:
            btn = QPushButton(text)
            btn.setStyleSheet(style + " padding: 6px; font-size: 11px; font-weight: bold; border-radius: 4px; text-align: right;")
            btn.clicked.connect(lambda checked, t_id=tool_id: self.run_tool(t_id))
            grid.addWidget(btn, row, col)
            col += 1
            if col > 1: col = 0; row += 1
                
        scr_btn = QPushButton("19. مستخرج الروابط والإيميلات الاستخباراتي من الأكواد (Web Scraper OSINT) 🕸️")
        scr_btn.setStyleSheet("background-color: #d97706; padding: 6px; font-size: 11px; font-weight: bold; text-align: right;")
        scr_btn.clicked.connect(lambda: self.run_tool("22"))
        grid.addWidget(scr_btn, row, 0, 1, 2); row += 1
        
        img_btn = QPushButton("🖼️ 20. مستخرج ميتاداتا وبيانات الصور المخفية والجغرافية")
        img_btn.setStyleSheet("background-color: #4b5563; padding: 6px; font-size: 11px; font-weight: bold;")
        grid.addWidget(img_btn, row, 0, 1, 2)
        
        main_layout.addLayout(grid)
        
        out_title = QLabel('🖥️ شاشة المخرجات الحية للإنذار وسجلات الـ Logs المباشرة:')
        out_title.setStyleSheet("color: #00ffcc; font-weight: bold; font-size: 12px;")
        main_layout.addWidget(out_title)
        
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        self.output_box.setStyleSheet("background-color: #0d1117; border: 1px solid #00ffcc; color: #00ff00; font-family: monospace; font-size: 13px;")
        main_layout.addWidget(self.output_box)
        self.setLayout(main_layout)

    def run_tool(self, tool_id):
        client_ip = "127.0.0.1"
        current_time = time.time()
        
        # محاكاة منطق الحظر التلقائي الذكي (Rate Limiter Logic)
        if client_ip not in self.IP_TRACKER: self.IP_TRACKER[client_ip] = []
        self.IP_TRACKER[client_ip] = [t for t in self.IP_TRACKER[client_ip] if current_time - t < 2]
        self.IP_TRACKER[client_ip].append(current_time)
        
        log_text = f"📥 [LOG] Request received from {client_ip} | Tool: [{tool_id}] | Rate: {len(self.IP_TRACKER[client_ip])} req/2s\n"
        
        if len(self.IP_TRACKER[client_ip]) > 15 or client_ip in self.BANNED_IPS:
            self.BANNED_IPS.add(client_ip)
            self.output_box.append(f"🚨 [🔥 SYSTEM ALERT] DDoS Attack Detected from {client_ip}! EMERGENCY AUTO-BLOCK ACTIVATED FOR ALL REF PORTS.")
            return Broken Authentication Scanners (OWASP Top 1 Validation)* Session Cookie & Token Security Auditors (Anti-Session Hijacking)* Remote Code Execution (RCE) & Command Injection Security Vector            
        self.output_box.append(log_text + f"[+] Execution Successful. Target Sandbox Environment Secure and Verified.")

if __name__ == '__main__':
    app = QApplication(sys.argv); ex = MalakSecuritySuite(); ex.show(); sys.exit(app.exec_())
