class OverlappingAppointmentError(Exception):
    """
    ==========================================
    DOMAIN KATMANI (İSTİSNALAR / EXCEPTIONS)
    ==========================================
    SEBEP: İş kuralları ihlal edildiğinde fırlatılacak özel hata mesajlarımızdır.
    Aynı saat aralığına denk gelen (Çakışan) randevuları reddetmek için kullanılır.
    """
    def __init__(self, message="Reddedildi: Bu saat aralığında doktorun zaten başka bir randevusu var!"):
        self.message = message
        super().__init__(self.message)
