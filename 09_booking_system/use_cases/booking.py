from datetime import datetime
from domain.entities import AppointmentEntity
from domain.exceptions import OverlappingAppointmentError

class BookingUseCase:
    """
    ==========================================
    USE CASES (KULLANIM SENARYOLARI / İŞ KURALLARI)
    ==========================================
    SEBEP: Şirketin "Randevu alırken çakışma var mı kontrol et, varsa hata ver"
    şeklindeki altın kuralının kodlandığı yerdir.
    DİKKAT: Bu sınıf veritabanına doğrudan BAĞLANMAZ! SQL veya SQLAlchemy bilmez.
    Kendisine dışarıdan verilecek olan bir 'repository' (Kayıtçı) üzerinden konuşur.
    Buna Dependency Injection (Bağımlılık Enjeksiyonu) denir.
    """
    def __init__(self, repository):
        self.repository = repository

    def book_appointment(self, doctor_name: str, patient_name: str, start_time: datetime, end_time: datetime) -> AppointmentEntity:
        
        # 1. KURAL KONTROLÜ: Başlangıç saati, bitişten önce veya eşit olamaz!
        if start_time >= end_time:
            raise ValueError("Bitiş saati, başlangıç saatinden önce olamaz!")

        # 2. ÇAKIŞMA (OVERLAP/RACE CONDITION) KONTROLÜ:
        # Repository'e "Bu doktorun bu saatleri arasında başka randevusu var mı?" diye soruyoruz.
        has_overlap = self.repository.check_overlap(doctor_name, start_time, end_time)
        
        if has_overlap:
            # Çakışma varsa, Domain katmanında yazdığımız o saf, çerçevesiz hatayı fırlatıyoruz!
            raise OverlappingAppointmentError()

        # 3. Kural ihlali yoksa, güvenle veritabanına kaydet (Repository aracılığıyla)
        new_appointment = self.repository.save(
            doctor_name=doctor_name,
            patient_name=patient_name,
            start_time=start_time,
            end_time=end_time
        )
        
        return new_appointment
