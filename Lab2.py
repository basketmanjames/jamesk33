import arcpy

in_feature = arcpy.GetParameterAsText(0)
out_feature = arcpy.GetParameterAsText(1)
in_table = arcpy.GetParameterAsText(2)
in_field = arcpy.GetParameterAsText(3)
out_field = arcpy.GetParameterAsText(4)
notfoundvalue = arcpy.GetParameterAsText(5)

field = arcpy.ValidateFieldName(out_field)
arcpy.CopyFeatures_management(in_feature, out_feature)
arcpy.AddField_management(out_feature, field, "DOUBLE")

cursor_fc = arcpy.da.UpdateCursor(out_feature, [in_field,field])
for row in cursor_fc:
	cursor_table = arcpy.da.SearchCursor(in_table, ["lowerbound", "upperbound", "value"])
	row[1] = notfoundvalue
	cursor_fc.updateRow(row)
	for table in cursor_table:
		if row[0] >= table[0] and row[0] <= table[1]:
			row[1] = table[2]
			cursor_fc.updateRow(row)
		else:
			print "9999"
	del table
	del cursor_table
del row
del cursor_fc
