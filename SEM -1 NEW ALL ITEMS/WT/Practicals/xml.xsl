<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html>
<body style="background-color:#EEEEEE">
<H2>ClASS STUDENT LIST</H2>
<TABLE BORDER="1">
<tr bgcolor="#9acd32">
<th>Roll NO</th>
<th>NAme</th>
<th>DOB</th>
<th>Phone</th>
<th>Marks</th>
</tr>
<xsl:for-each select="class/student">
<tr>
<td><xsl:value-of select="rollno"/></td>
<td><xsl:value-of select="name"/></td>
<td><xsl:value-of select="DOB"/></td>
<td><xsl:value-of select="phone"/></td>
<td><xsl:value-of select="marks"/></td>
</tr>
</xsl:for-each>
</TABLE>
</body>
</html>
</xsl:template>
</xsl:stylesheet>
