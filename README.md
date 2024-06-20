# Deadlock Project

## توضیحات پروژه
در دنیای پیچیده و پویای سیستم‌های عامل، مدیریت منابع به نحوی که عملکرد سیستم بهینه و بدون اختلال باشد، اهمیت فراوانی دارد. یکی از چالش‌های مهم در این زمینه، پدیده‌ای به نام بن‌بست است که می‌تواند عملکرد سیستم را به شدت تحت تاثیر قرار دهد. بن‌بست زمانی رخ می‌دهد که دو یا چند فرآیند به گونه‌ای در انتظار منابع قفل می‌شوند که هیچ یک قادر به ادامه فعالیت خود نیستند. این وضعیت می‌تواند باعث توقف کامل سیستم و از دست رفتن کارایی شود.

این پروژه با هدف ارائه یک درک عملی و جامع از نحوه وقوع، تشخیص و رفع بن‌بست در سیستم عامل طراحی شده است. این پروژه شامل سه فاز اصلی است که هر یک به جنبه‌ای خاص از مسئله بن‌بست می‌پردازند.

## ساختار پروژه
- `banker.py`: پیاده‌سازی الگوریتم بانکدار برای مدیریت تخصیص منابع و جلوگیری از وقوع بن‌بست
- `graph.py`: پیاده‌سازی ساختار داده‌ای گراف برای نمایش منابع و فرآیندها و تشخیص بن‌بست‌ها
- `resource.py`: پیاده‌سازی کلاس منابع و فرآیندها برای سیموله‌سازی بن‌بست
- `README.md`: توضیحات پروژه

## نحوه اجرا
1. نصب کتابخانه‌های مورد نیاز:
```
pip install numpy
```

2. اجرای فایل `banker.py`:
```
python banker.py
```

3. اجرای فایل `graph.py`:
```
python graph.py
```

4. اجرای فایل `resource.py`:
```
python resource.py
```

## تحلیل و توضیحات
- `banker.py`: این فایل شامل پیاده‌سازی الگوریتم بانکدار است که با استفاده از ماتریس‌های حداکثر نیاز، تخصیص فعلی، و منابع باقی مانده، از وقوع بن‌بست جلوگیری می‌کند.
- `graph.py`: در این فایل ساختار داده‌ای گراف برای نمایش منابع و فرآیندها پیاده‌سازی شده است که از آن برای تشخیص بن‌بست‌ها استفاده می‌شود.
- `resource.py`: در این فایل کلاس منابع و فرآیندها پیاده‌سازی شده است که برای سیموله‌سازی بن‌بست مورد استفاده قرار می‌گیرد.

## گزارش
- [x] پیاده‌سازی کلاس‌های مورد نیاز
- [x] سیموله‌سازی بن‌بست با استفاده از کلاس‌ها و الگوریتم بانکدار
- [x] تشخیص بن‌بست‌ها با استفاده از ساختار داده‌ای گراف

---
