from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Auth Microservice", version="1.0.0", docs_url=None, redoc_url=None)

class TokenVerifyRequest(BaseModel):
    token: str

@app.post("/verify-token")
def verify_token(data: TokenVerifyRequest):
    """
    ==========================================
    AUTH MİKROSERVİSİ (PORT 8001)
    ==========================================
    Bu servisin dünyadaki TEK görevi kendisine verilen Token'ın geçerli olup 
    olmadığını kontrol etmektir. Sipariş nedir, mail nedir bilmez.
    """
    if data.token == "super-secret-token":
        # Token doğruysa kullanıcının ID'sini geri dön
        return {"status": "success", "user_id": 42}
    
    # Token yanlışsa hata fırlat
    raise HTTPException(status_code=401, detail="Geçersiz Token! Kimlik Doğrulanamadı.")
