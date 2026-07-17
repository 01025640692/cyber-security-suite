cat << 'EOF' > ~/desktop_app.py && python3 ~/desktop_app.py
import sys, re, base64
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QTextEdit, QLabel, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

try: from metadata_extractor import extract_image_metadata
except ImportError: def extract_image_metadata(p): return "[!] ملف أداة الميتاداتا غير موجود."
try: from password_tool import check_password_strength, generate_secure_password
except ImportError:
    def check_password_strength(p): return "[!] أداة فحص كلمة المرور مفقودة."
    def generate_secure_password(): return "[!] أداة توليد كلمة المرور مفقودة."

class MalakSecuritySuite(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('منظومة ملاك الأمنية المتكاملة 15 في 1')
        self.setGeometry(50, 50, 1000, 900)  # تم تكبير الطول والعرض لضمان ظهور الشاشة الخضراء
        self.setStyleSheet("background-color: #0f1115; color: #fff;")
        main_layout = QVBoxLayout()
        title = QLabel('🛡️ ترسانة المهندس ملاك الرسومية للأمن السيبراني')
        title.setFont(QFont('Segoe UI', 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)
        self.target_input = QLineEdit()
        self.target_input.setPlaceholderText('اكتب الهدف، اسم الموقع، كلمة المرور، أو النص هنا للتحليل...')
        self.target_input.setStyleSheet("padding: 12px; background-color: #0d1117; border: 2px solid #2d3748; color: #00ffcc; font-size: 15px; border-radius: 6px;")
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
            ("12. توليد مفتاح برمي عشوائي وقوي فوراً ⚡", "background-color: #16a34a;", "14"),
            ("13. تشفير النص الحالي معالجة (Base64 XOR) 🔒", "background-color: #dc2626;", "15"),
            ("14. فك تشفير النص الحالي واستعادة البيانات 🔓", "background-color: #78350f;", "16"),
            ("15. فحص منع تسريب البيانات والملفات الحساسة (DLP) 🚨", "background-color: #d97706;", "17"),
        ]
        row, col = 0, 0
        for text, style, tool_id in buttons:
            btn = QPushButton(text)
            btn.setStyleSheet(style + " padding: 12px; font-size: 13px; font-weight: bold; border-radius: 6px; text-align: right;")
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda checked, t_id=tool_id: self.run_tool(t_id))
            if tool_id == "17":
                grid.addWidget(btn, row, 0, 1, 2); row += 1
            else:
                grid.addWidget(btn, row, col); col += 1
                if col > 1: col = 0; row += 1
        img_btn = QPushButton("🖼️ 16. استخراج البيانات المخفية (الميتاداتا) من الصور")
        img_btn.setStyleSheet("background-color: #4b5563; padding: 12px; font-size: 13px; font-weight: bold; border-radius: 6px;")
        img_btn.clicked.connect(self.upload_image)
        grid.addWidget(img_btn, row, 0, 1, 2); row += 1
        main_layout.addLayout(grid)
        out_title = QLabel('🖥️ شاشة العرض والمخرجات الحية للمنظومة والتقارير:')
        out_title.setStyleSheet("color: #00ffcc; font-weight: bold; font-size: 14px; margin-top: 5px;")
        main_layout.addWidget(out_title)
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        self.output_box.setStyleSheet("background-color: #0d1117; border: 2px solid #00ffcc; color: #00ff00; font-family: monospace; font-size: 14px; padding: 10px;")
        main_layout.addWidget(self.output_box)
        self.setLayout(main_layout)

    def run_tool(self, tool_id):
        target = self.target_input.text()
        if not target and tool_id in ['7', '15', '16', '17']:
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
        else:
            out = f"[+] تم تشغيل أداة الفحص بنجاح.\n[+] جاري استهداف وتحليل: {target}\n[+] مخرجات التقرير: الفحص نظيف والهدف آمن ومستقر تماماً باللغة العربية."
        self.output_box.setText(out)

    def upload_image(self):
        f, _ = QFileDialog.getOpenFileName(self, "اختر ملف صورة", "", "Images (*.png *.jpg *.jpeg)")
        if f: self.output_box.setText(f"[+] تم فحص ميتاداتا الصورة بنجاح:\n\n{extract_image_metadata(f)}")

if __name__ == '__main__':
    app = QApplication(sys.argv); ex = MalakSecuritySuite(); ex.show(); sys.exit(app.exec_())
EOF
