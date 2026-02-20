# Dynamic Content Management System - User Guide

## Overview
Το σύστημα διαχείρισης δυναμικού περιεχομένου επιτρέπει την πλήρη επεξεργασία όλων των κειμένων και εικόνων της ιστοσελίδας μέσω του Django Admin panel, με πλήρη υποστήριξη δύο γλωσσών (Αγγλικά/Ελληνικά).

## Βασικά Χαρακτηριστικά

### ✅ Πλήρως Δυναμικό Περιεχόμενο
- Όλα τα κείμενα είναι επεξεργάσιμα από το admin
- Όλες οι εικόνες μπορούν να ανέβουν/αλλάξουν από το admin
- Δίγλωσση υποστήριξη (EN/EL) για κάθε κείμενο
- Preview εικόνων στο admin panel

### 📑 Ενότητες με Δυναμικό Περιεχόμενο

## 1. Hero Section (Αρχική Οθόνη)
**Admin Location:** `Hero Section`

**Διαθέσιμα Πεδία:**
- 🎯 Mega Text (Vertical): Το κάθετο κείμενο δεξιά/αριστερά
- 💫 Main Title - Part 1: Πρώτο μέρος του τίτλου (2 γραμμές)
- ✨ Main Title - Part 2: Το highlighted μέρος του τίτλου (π.χ. "GROWTH!")
- 🎴 Service Showcase Card:
  - Τίτλος υπηρεσίας
  - Περιγραφή υπηρεσίας
  - Κείμενο κουμπιού
  - URL κουμπιού
  - Εικόνα υπηρεσίας (με preview)

**Note:** To Hero Section είναι singleton - υπάρχει μόνο ένα record.

---

## 2. Services Section (Υπηρεσίες)
**Admin Location:** `Services` + `Services Section Settings`

### Services Section Settings (Singleton)
**Πεδία:**
- 🎯 Mega Text: Το κάθετο κείμενο στο background

### Services (Πολλαπλά Records)
**Πεδία:**
- 📝 Title (EN/EL): Τίτλος υπηρεσίας
- 📝 Description (EN/EL): Περιγραφή υπηρεσίας
- 🖼️ Image: Εικόνα υπηρεσίας (με preview)
- 📐 Layout: Επιλογή "Image Left" ή "Image Right"
- 🔘 Button Text (EN/EL): Κείμενο κουμπιού
- 🔗 Button Link: URL κουμπιού
- 🔢 Sort Order: Σειρά εμφάνισης (μικρότερος αριθμός = πρώτο)
- ✓ Active: Ενεργοποίηση/Απενεργοποίηση

**Πώς να προσθέσω νέα υπηρεσία:**
1. Πατήστε "Add Service"
2. Συμπληρώστε Title EN/EL και Description EN/EL
3. Ανεβάστε εικόνα
4. Επιλέξτε layout (left/right)
5. Ορίστε Sort Order (0=πρώτο, 1=δεύτερο, κλπ)
6. Τσεκάρετε το "Active"
7. Save

---

## 3. About Section (Σχετικά)
**Admin Location:** `About Section`

**Διαθέσιμα Πεδία:**
- 📌 Section Title: Τίτλος ενότητας (π.χ. "Who's behind the Digi?")
- 👤 Introduction:
  - Intro Name: Όνομα και τίτλος
  - Intro Text: Εισαγωγικό κείμενο
- 📄 Description:
  - Description Part 1: Πρώτο μέρος περιγραφής
  - Brand Name: Όνομα brand
  - Description Part 2: Δεύτερο μέρος περιγραφής
- 🔘 Call-to-Action:
  - Button Text (EN/EL)
  - Button Link
- 🖼️ Images:
  - Main Image: Κύρια εικόνα (με preview)
  - Badge Top Left: Badge πάνω αριστερά
  - Badge Bottom Left: Badge κάτω αριστερά
  - Badge Bottom Right: Badge κάτω δεξιά

**Note:** To About Section είναι singleton - υπάρχει μόνο ένα record.

---

## 4. Contact Section (Επικοινωνία)
**Admin Location:** `Contact Section`

**Διαθέσιμα Πεδία:**
- 📌 Section Titles:
  - Title: Τίτλος φόρμας (π.χ. "CONTACT FORM")
  - Happy Clients Title: Τίτλος για τα logos
- 🏷️ Form Labels (όλα σε EN/EL):
  - Label Name: "Όνομα"/"Name"
  - Label Phone: "Τηλέφωνο"/"Phone"
  - Label Email: "E-mail"
  - Label Service: "Υπηρεσία"/"Service"
  - Label Budget: "Προϋπολογισμός"/"Budget"
  - Label Message: "Μήνυμα"/"Message"
- 📋 Dropdown Placeholders:
  - Service Select: "Επιλέξτε υπηρεσία"/"Select a service"
  - Budget Select: "Επιλέξτε προϋπολογισμό"/"Select budget"
- 🔘 Button:
  - Button Submit: "ΥΠΟΒΟΛΗ"/"SUBMIT"

**Note:** To Contact Section είναι singleton - υπάρχει μόνο ένα record.

---

## 5. Client Logos (Λογότυπα Πελατών)
**Admin Location:** `Client Logos`

**Πεδία:**
- 📝 Client Name: Όνομα πελάτη
- 🖼️ Logo: Εικόνα λογότυπου (με preview)
- 🔢 Sort Order: Σειρά εμφάνισης
- ✓ Active: Ενεργοποίηση/Απενεργοποίηση

**Πώς να προσθέσω νέο logo:**
1. Πατήστε "Add Client Logo"
2. Γράψτε το όνομα του πελάτη
3. Ανεβάστε το logo (προτεινόμενο: PNG με διαφάνεια)
4. Ορίστε Sort Order
5. Τσεκάρετε "Active"
6. Save

**⚠️ NOTE:** Τα logos εμφανίζονται στο Contact Section κάτω από το "Happy Clients" title.

---

## 6. Happy Clients Section
**Admin Location:** `Happy Clients Section`

**Πεδία:**
- 📌 Title (EN/EL): Τίτλος ενότητας
- 💬 Placeholder Text (EN/EL): Κείμενο όταν δεν υπάρχουν testimonials

**Note:** Αυτό είναι singleton - για testimonials χρησιμοποιήστε το "Testimonials" model.

---

## 7. Footer Section (Υποσέλιδο)
**Admin Location:** `Footer Section`

**Διαθέσιμα Πεδία:**
- 🖼️ Logo: Logo για το footer (με preview)
- 🌐 Social Media:
  - Instagram URL
  - Facebook URL
  - LinkedIn URL
- 📞 Contact Info:
  - Phone Label (EN/EL): "P."/"Τ."
  - Phone Number
  - Email Label (EN/EL): "E."
  - Email Address
- 📱 QR Code: QR code image (με preview)
- ©️ Copyright:
  - Copyright Year: Έτος (π.χ. 2026)
  - Copyright Text (EN/EL)

**Note:** To Footer είναι singleton - υπάρχει μόνο ένα record.

---

## Πώς Λειτουργεί το Σύστημα

### Singleton Models
Τα παρακάτω models είναι "singleton" - δηλαδή υπάρχει μόνο **ένα record**:
- Hero Section
- Services Section Settings
- About Section
- Contact Section
- Happy Clients Section
- Footer Section

**Αν δεν υπάρχει record**, το σύστημα θα δημιουργήσει αυτόματα ένα με default τιμές.

### List Models
Τα παρακάτω models μπορούν να έχουν **πολλά records**:
- Services (υπηρεσίες)
- Client Logos (λογότυπα πελατών)

Για αυτά τα models:
- Μπορείτε να προσθέσετε όσα records θέλετε
- Χρησιμοποιήστε το "Sort Order" για να ελέγξετε τη σειρά
- Χρησιμοποιήστε το "Active" checkbox για να ενεργοποιήσετε/απενεργοποιήσετε

---

## Δίγλωσση Υποστήριξη

Κάθε κείμενο έχει **δύο εκδοχές**:
- `field_en`: Αγγλική έκδοση
- `field_el`: Ελληνική έκδοση

**Το σύστημα αυτόματα:**
- Επιλέγει το σωστό κείμενο με βάση τη γλώσσα του επισκέπτη
- Αν δεν υπάρχει μετάφραση, εμφανίζει την αγγλική έκδοση (fallback)

---

## Οδηγός Εικόνων

### Προτεινόμενες Διαστάσεις

| Τύπος | Προτεινόμενο | Format |
|-------|-------------|--------|
| Hero Service Image | 600x400px | JPG/PNG |
| Service Images | 800x600px | JPG/PNG |
| About Main Image | 600x800px | JPG/PNG |
| About Badges | 150x150px | PNG (διαφάνεια) |
| Footer Logo | 300x100px | PNG (διαφάνεια) |
| QR Code | 200x200px | PNG |
| Client Logos | 200x80px | PNG (διαφάνεια) |

### Tips για Εικόνες:
- ✓ Χρησιμοποιήστε PNG με διαφάνεια για logos
- ✓ Συμπιέστε τις εικόνες πριν τις ανεβάσετε (optimizeimages.com)
- ✓ Χρησιμοποιήστε ονόματα αρχείων χωρίς κενά (π.χ. `my-logo.png`)
- ✗ Μην ανεβάζετε τεράστιες εικόνες (>2MB)

---

## Πού μπαίνουν τα αρχεία

### Εικόνες:
```
media/
  ├── hero/              # Hero service image
  ├── services/          # Service images
  ├── about/             # About main image
  │   └── badges/        # About badge images
  ├── footer/            # Footer logo & QR code
  └── client-logos/      # Client logo images
```

### Database:
Το `db.sqlite3` περιέχει όλα τα κείμενα και references στις εικόνες.

---

## Admin Panel Access

**URL:** `http://localhost:8000/admin/` (local) ή `https://yourdomain.com/admin/` (production)

**Sections στο Admin:**
1. **MAIN**
   - Hero Section
   - Services
   - Services Section Settings
   - About Section
   - Contact Section
   - Happy Clients Section
   - Footer Section
   - Client Logos
   
2. **SETTINGS**
   - Site Settings (Calendly URL)
   - Analytics Settings (GA4)
   
3. **QUOTES**
   - Quote Requests (από τη φόρμα επικοινωνίας)
   - Testimonials

---

## Seeding Scripts

Αν χρειαστεί να φορτώσετε ξανά τα default data:

```bash
# Activate virtual environment
.\env\Scripts\activate

# Copy service images
python copy_service_images.py

# Copy hero/about images (optional - if you have them)
python copy_hero_about_images.py

# Seed services
python seed_services.py

# Seed hero
python seed_hero.py

# Seed other content
python seed_additional_content.py

# Seed footer (χωρίς εικόνες - προσθέστε τις manually)
python seed_footer_and_logos.py
```

---

## Troubleshooting

### Δεν φαίνονται οι εικόνες στο site
1. Βεβαιωθείτε ότι έχετε ανεβάσει εικόνα στο admin
2. Ελέγξτε ότι ο φάκελος `media/` έχει τις σωστές εικόνες
3. Σε production, τρέξτε `python manage.py collectstatic`

### Δεν φαίνονται οι αλλαγές
1. Κάντε Hard refresh: Ctrl+Shift+R (Windows) ή Cmd+Shift+R (Mac)
2. Clear browser cache
3. Ελέγξτε ότι το record είναι "Active" (για Services/Client Logos)

### Τα κείμενα είναι στην λάθος γλώσσα
1. Ελέγξτε το language selector στο site (πάνω δεξιά)
2. Βεβαιωθείτε ότι έχετε συμπληρώσει και τα δύο πεδία (_en και _el)

---

## Quick Reference

### Για να αλλάξω το Hero title:
Admin → Hero Section → Main Title fields

### Για να προσθέσω νέα υπηρεσία:
Admin → Services → Add Service

### Για να αλλάξω τα social media links:
Admin → Footer Section → Social Media

### Για να προσθέσω client logo:
Admin → Client Logos → Add Client Logo

### Για να αλλάξω contact info:
Admin → Footer Section → Contact Info

---

## Support

Για περισσότερη βοήθεια, ελέγξτε:
- Django documentation: https://docs.djangoproject.com/
- Django Admin documentation: https://docs.djangoproject.com/en/stable/ref/contrib/admin/

---

**Τελευταία ενημέρωση:** Januar 2025
**Έκδοση συστήματος:** 1.0.0
