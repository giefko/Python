

from xlrd import open_workbook
import types

wb = open_workbook("example.xls")
s=wb.sheet_by_index(0) 
    
for row in range(s.nrows):
        
    for col in range(s.ncols):
            
           
        k=s.cell(row,col).value
        
        am="something you search"
        

        if k==am:

            print "an other cell",s.cell(row,col+1).value
			print "something you want"
          
    
