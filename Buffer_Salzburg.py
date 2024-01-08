# -------------------------------------------------------------
# Name: Jana Hack
# Date: 21.11.2023
# Inhalt: Dieses Script erzeugt einen definierten Buffer um
# die Fluesse Salzburgs und verbindet die gebufferten Einzelteile ("Dissolve").
# -----------------------------------------------------------
import arcpy

# Ueberschreiben von Daten erlauben
arcpy.env.overwriteOutput = 1

# Workspace eingeben
arcpy.env.workspace = r"C:\Users\Documents\Salzburg.gdb"

# Pfad für die Ausgabedaten festlegen
output_folder = r"C:\Documents\Mod5_Afg3\Outputs"

# Variablen angeben
sbgFluesse = "sbg_fluesse"
praefix = "Buffer"

# Buffergrößen vom Benutzer abfragen und in eine Liste umwandeln
Buffer_Werte = input("Geben Sie Bufferwerte an (Trennung mehrerer Werte mit Leerzeichen): ")
Buffer_Werte = [int(Wert) for Wert in Buffer_Werte.split()]

# Schleife durch die Liste der Buffergrößen
for Buffer_Wert in Buffer_Werte:
    # Datensatznamen erstellen und auf Gültigkeit prüfen
    output_name = arcpy.ValidateTableName(f"{praefix}_{Buffer_Wert}")

    # Überprüfen, ob der Datensatz schon existiert
    if arcpy.Exists(f"{output_folder}\\{output_name}.shp"):
        # Eindeutigen Namen generieren
        output_name = arcpy.CreateUniqueName(f"{output_folder}\\{output_name}.shp")

    # Buffer erstellen
    arcpy.Buffer_analysis(sbgFluesse, f"{output_folder}\\{output_name}.shp", f"{Buffer_Wert} Meters", "FULL", "ROUND", "ALL", "")

    # Print innerhalb der Schleife, um Wert für jede Schleife auszugeben
    print(f"Der neue Buffer wurde berechnet und als {output_name} gespeichert.")
