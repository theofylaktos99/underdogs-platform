import sqlite3
import bcrypt

# Νέος κωδικός
new_password = "mellon"
# Δημιουργία hash με bcrypt
hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Σύνδεση στη βάση
conn = sqlite3.connect('underdogs.db')
cursor = conn.cursor()

try:
    # Ενημέρωση κωδικού για το χρήστη theofylaktos99@gmail.com
    cursor.execute(
        "UPDATE users SET hashed_password = ? WHERE email = ?",
        (hashed_password, "theofylaktos99@gmail.com")
    )
    
    if cursor.rowcount > 0:
        conn.commit()
        print("✅ Κωδικός ενημερώθηκε επιτυχώς!")
        print(f"📧 Email: theofylaktos99@gmail.com")
        print(f"🔑 Νέος κωδικός: {new_password}")
    else:
        print("❌ Δεν βρέθηκε χρήστης με αυτό το email")
        
except Exception as e:
    print(f"Σφάλμα: {e}")
    
finally:
    conn.close()
