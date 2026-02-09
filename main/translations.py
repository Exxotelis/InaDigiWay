# Greek Translation Dictionary
# This is a simple Python dict-based translation system for InaDigiWay

TRANSLATIONS_EL = {
    # Navigation and header
    "About": "Σχετικά με Εμάς",
    "Services": "Υπηρεσίες",
    "Contact": "Επικοινωνία",
    
    # Hero Section
    "Digital solutions that convert": "Ψηφιακές λύσεις που μετατρέπουν",
    "Your Online Success Starts Here": "Η Επιτυχία Σας Στο Διαδίκτυο Ξεκινά Εδώ",
    
    # About Section
    "About Us": "Σχετικά με Εμάς",
    "We are a digital marketing agency dedicated to delivering innovative solutions that drive growth and success for your business.": "Είμαστε μια ψηφιακή μάρκετινγκ αγορά αφιερωμένη στη παροχή καινοτόμων λύσεων που προωθούν την ανάπτυξη και την επιτυχία της επιχείρησής σας.",
    
    # Services Section
    "Web Design": "Σχεδιασμός Ιστοσελίδων",
    "Web Development": "Ανάπτυξη Ιστοσελίδων",
    "Mobile App": "Εφαρμογή Κινητού",
    "Branding": "Δημιουργία Ταυτότητας",
    "Social Media Marketing": "Μάρκετινγκ Κοινωνικών Δικτύων",
    
    # Contact Section
    "Contact Form": "Φόρμα Επικοινωνίας",
    "Happy Clients": "Ευχαριστημένοι Πελάτες",
    "Name": "Όνομα",
    "Phone": "Τηλέφωνο",
    "E-mail": "Email",
    "Service": "Υπηρεσία",
    "Budget": "Προϋπολογισμός",
    "Message": "Μήνυμα",
    "Select a service": "Επιλέξτε μια υπηρεσία",
    "Select budget": "Επιλέξτε προϋπολογισμό",
    "Submit": "Αποστολή",
    
    # Footer
    "Follow Us": "Ακολουθήστε μας",
    "Contact Info": "Πληροφορίες Επικοινωνίας",
    "All rights reserved": "Όλα τα δικαιώματα διατηρούνται",
    
    # Form messages
    "Professional digital marketing agency": "Επαγγελματική ψηφιακή μάρκετινγκ αγορά",
}

def translate(text, language_code):
    """
    Simple translation function
    
    Args:
        text: English text to translate
        language_code: Language code (e.g., 'el' for Greek)
    
    Returns:
        Translated text or original if not found
    """
    if language_code == 'el':
        return TRANSLATIONS_EL.get(text, text)
    return text
