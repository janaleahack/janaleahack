# Import system modules
import arcpy
# Eingabedatei (Feature Class) festlegen
inputFC = arcpy.GetParameterAsText(0)
# Liste der Feldnamen erfassen
inputString = arcpy.GetParameterAsText(1)
fieldList =inputString.split(";")
fieldType = arcpy.GetParameterAsText(2)
for fieldName in fieldList:
    arcpy.AddField_management(inputFC , fieldName, fieldType)
    arcpy.AddMessage("Feld erstellt:" + fieldName)
arcpy.AddMessage ("Berechnung abgeschlossen")

