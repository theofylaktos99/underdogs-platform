import sqlite3

# Σύνδεση στη βάση
conn = sqlite3.connect('underdogs.db')
cursor = conn.cursor()

try:
    # Έλεγχος δομής πίνακα users
    cursor.execute("PRAGMA table_info(users)")
    columns = cursor.fetchall()
    
    print("Δομή πίνακα users:")
    for col in columns:
        print(f"- {col[1]} ({col[2]})")
        
    print("\nΔεδομένα χρήστη theofylaktos99:")
    cursor.execute("SELECT * FROM users WHERE email = ?", ("theofylaktos99@gmail.com",))
    user_data = cursor.fetchone()
    
    if user_data:
        print("Βρέθηκε χρήστης:")
        for i, col in enumerate(columns):
            print(f"{col[1]}: {user_data[i]}")
    else:
        print("Δεν βρέθηκε χρήστης")
        
except Exception as e:
    print(f"Σφάλμα: {e}")
    
finally:
    conn.close()
