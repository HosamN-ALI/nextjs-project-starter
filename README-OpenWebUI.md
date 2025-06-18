# 🔒 AI Pentest Agent مع Open WebUI

## نظرة عامة

تم تطوير AI Pentest Agent ليعمل مع واجهة Open WebUI المتقدمة، مما يوفر تجربة مستخدم محسنة وميزات إضافية لاختبار الاختراق الذكي.

## 🚀 الميزات الجديدة مع Open WebUI

### 1. **واجهة مستخدم متقدمة**
- تصميم حديث ومتجاوب
- دعم الوضع المظلم والفاتح
- واجهة محادثة محسنة مع تمييز الأكواد
- دعم Markdown كامل

### 2. **إدارة الجلسات**
- حفظ تاريخ المحادثات
- إدارة مشاريع الاختبار المختلفة
- تصدير التقارير بصيغ متعددة

### 3. **ميزات الأمان المحسنة**
- نظام مصادقة متقدم
- تسجيل جميع العمليات
- تحكم في معدل الطلبات
- تحذيرات أمنية تلقائية

### 4. **تكامل AI محسن**
- استجابة أسرع وأكثر دقة
- دعم النماذج المتعددة
- تحكم في معاملات AI
- معاينة مباشرة للنتائج

## 📦 التثبيت والإعداد

### الطريقة الأولى: Docker Compose (الموصى بها)

```bash
# 1. استنساخ المشروع
git clone <repository-url>
cd ai-pentest-agent

# 2. تشغيل الخدمات
docker-compose up -d

# 3. الوصول للواجهات
# Open WebUI: http://localhost:3000
# API Backend: http://localhost:8000
# MongoDB: localhost:27017
# Redis: localhost:6379
```

### الطريقة الثانية: التثبيت اليدوي

```bash
# 1. تثبيت Open WebUI
docker run -d \
  --name ai-pentest-webui \
  -p 3000:8080 \
  -e WEBUI_NAME="AI Pentest Agent" \
  -e WEBUI_AUTH=false \
  -e DEFAULT_MODELS=ai-pentest-agent \
  -v open-webui:/app/backend/data \
  -v ./custom:/app/backend/data/custom \
  ghcr.io/open-webui/open-webui:main

# 2. تشغيل API Backend
npm install
npm run build
npm start
```

## 🔧 التكوين

### 1. **إعداد API Key**

قم بتحديث ملف `custom/openai_config.json`:

```json
{
  "models": [
    {
      "id": "ai-pentest-agent",
      "api_key": "YOUR_DEEPSEEK_API_KEY_HERE"
    }
  ]
}
```

### 2. **تخصيص الواجهة**

يمكنك تعديل ملف `custom/pentest-theme.css` لتخصيص المظهر:

```css
:root {
  --primary-color: #your-color;
  --secondary-color: #your-secondary-color;
}
```

### 3. **إعداد قاعدة البيانات**

```bash
# الاتصال بـ MongoDB
mongo mongodb://admin:pentestpass123@localhost:27017/ai_pentest

# إنشاء مجموعات البيانات
db.createCollection("pentest_sessions")
db.createCollection("audit_logs")
db.createCollection("user_preferences")
```

## 🎯 كيفية الاستخدام

### 1. **الوصول للواجهة**

1. افتح المتصفح واذهب إلى `http://localhost:3000`
2. قم بإنشاء حساب جديد أو تسجيل الدخول
3. اختر نموذج "AI Pentest Agent"

### 2. **إنشاء خطة اختبار اختراق**

```
مثال على الطلبات:

1. "قم بفحص شامل لموقع example.com"
2. "اختبر ثغرات SQL Injection في testsite.com"
3. "فحص الشبكة والخدمات لـ 192.168.1.0/24"
4. "تقييم أمني شامل لتطبيق الويب myapp.com"
```

### 3. **ميزات متقدمة**

#### أ. **حفظ وإدارة المشاريع**
- انقر على "New Chat" لبدء مشروع جديد
- استخدم "Save Chat" لحفظ الجلسة
- "Export Chat" لتصدير التقرير

#### ب. **تخصيص معاملات AI**
- اضبط Temperature للتحكم في الإبداع
- حدد Max Tokens للاستجابات الطويلة
- استخدم System Prompts المخصصة

#### ج. **المشاركة والتعاون**
- شارك الجلسات مع الفريق
- اضف تعليقات وملاحظات
- تتبع تقدم المشروع

## 📊 لوحة التحكم والمراقبة

### 1. **إحصائيات الاستخدام**
- عدد الطلبات اليومية
- أنواع الاختبارات المطلوبة
- معدل نجاح العمليات

### 2. **سجلات الأمان**
- جميع الطلبات مسجلة
- تتبع IP addresses
- تحليل أنماط الاستخدام

### 3. **تقارير الأداء**
- زمن الاستجابة
- استهلاك الموارد
- معدل الأخطاء

## 🛡️ الأمان والامتثال

### 1. **إرشادات الأمان**
- استخدم فقط على الأنظمة المصرح بها
- احترم قوانين الخصوصية
- لا تستخدم للأنشطة الضارة

### 2. **التحكم في الوصول**
- نظام مصادقة قوي
- أذونات مبنية على الأدوار
- تسجيل جميع العمليات

### 3. **حماية البيانات**
- تشفير البيانات الحساسة
- نسخ احتياطية منتظمة
- حذف البيانات القديمة

## 🔧 استكشاف الأخطاء

### مشاكل شائعة وحلولها:

#### 1. **خطأ في الاتصال بـ API**
```bash
# تحقق من حالة الخدمات
docker-compose ps

# إعادة تشغيل الخدمات
docker-compose restart
```

#### 2. **مشاكل في قاعدة البيانات**
```bash
# تحقق من سجلات MongoDB
docker logs ai-pentest-mongo

# إعادة تعيين قاعدة البيانات
docker-compose down -v
docker-compose up -d
```

#### 3. **مشاكل في الواجهة**
```bash
# مسح cache المتصفح
# تحقق من console للأخطاء
# إعادة تشغيل Open WebUI
docker restart ai-pentest-webui
```

## 📈 التطوير والتخصيص

### 1. **إضافة أدوات جديدة**

قم بتعديل ملف `custom/functions.py`:

```python
def add_new_tool(self, tool_name: str, command: str, description: str):
    # إضافة أداة جديدة للقائمة
    pass
```

### 2. **تخصيص النماذج**

أضف نماذج AI جديدة في `custom/openai_config.json`:

```json
{
  "models": [
    {
      "id": "custom-model",
      "name": "Custom Pentest Model",
      "provider": "custom"
    }
  ]
}
```

### 3. **إضافة ميزات جديدة**

```python
# في custom/functions.py
def new_feature_function(user_input: str) -> str:
    # تنفيذ الميزة الجديدة
    return result
```

## 🤝 المساهمة والدعم

### كيفية المساهمة:
1. Fork المشروع
2. إنشاء branch جديد
3. إضافة التحسينات
4. إرسال Pull Request

### الحصول على الدعم:
- GitHub Issues للمشاكل التقنية
- Documentation للإرشادات
- Community Forum للنقاشات

## 📄 الترخيص

هذا المشروع مرخص تحت رخصة MIT. راجع ملف LICENSE للتفاصيل.

---

**تحذير مهم:** استخدم هذه الأداة بمسؤولية وفقط على الأنظمة التي تملك إذناً صريحاً لاختبارها. المطورون غير مسؤولين عن أي استخدام غير قانوني أو ضار.
