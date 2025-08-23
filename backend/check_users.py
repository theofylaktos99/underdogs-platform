import sqlite3

# Σύνδεση στη βάση
conn = sqlite3.connect('underdogs.db')
cursor = conn.cursor()

try:
    # Έλεγχος αν υπάρχει πίνακας users
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    table_exists = cursor.fetchone()
    
    if table_exists:
        # Εμφάνιση χρηστών
        cursor.execute('SELECT email, username FROM users')
        users = cursor.fetchall()
        
        print("Χρήστες στη βάση:")
        for user in users:
            print(f"Email: {user[0]}, Username: {user[1]}")
    else:
        print("Δεν υπάρχει πίνακας users στη βάση")
        
except Exception as e:
    print(f"Σφάλμα: {e}")
    
finally:
    conn.close()
