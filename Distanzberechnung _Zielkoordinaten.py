import math

# Gegebene Koordinaten
lat1 = 47.80
lon1 = 13.00

# Benutzereingabe für die Zielkoordinaten
lat2 = float(input("Geben Sie bitte die geogr. Breite eines beliebigen Ortes an: "))
lon2 = float(input("Geben Sie bitte die geogr. Länge eines beliebigen Ortes an: "))

# Umrechnung der Koordinaten von Grad in Radianten
lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

try:
    distance = 6370 * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon2 - lon1))
    print(f"Die kürzeste Entfernung beträgt {distance:.2f} Kilometer.")
except Exception as e:
    print(f"Fehler aufgetreten: {e}")

input("Press return to close this window...")
