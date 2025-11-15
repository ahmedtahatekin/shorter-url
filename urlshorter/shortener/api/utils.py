import random
import string

# Kod için kullanılabilecek karakter havuzu (küçük/büyük harfler + rakamlar)
chars = string.ascii_letters + string.digits 
# Örn: 'a'..'z', 'A'..'Z', '0'..'9'

def generate_random_code(size=7):
    # Belirtilen uzunlukta rastgele alfanümerik dize üretir
    return ''.join(random.choice(chars) for _ in range(size))

def create_unique_short_code(instance, size=7):
    # Benzersiz bir kısa kod üretir ve varlığını kontrol eder
    from ..models import ShortURL # Döngüsel içe aktarmayı önlemek için burada çağırıyoruz


    # 1. Kod üret
    new_code = generate_random_code(size=size)
    
    # 2. Veritabanında kontrol et
    # Eğer bu kodla eşleşen başka bir nesne varsa (exists=True)
    qs_exists = ShortURL.objects.filter(short_code=new_code).exists()
    
    # 3. Eğer var ise, yeni bir kod üretmek için fonksiyonu tekrar çağır
    if qs_exists:
        return create_unique_short_code(instance, size=size)
        
    # 4. Benzersiz ise, kodu döndür
    return new_code