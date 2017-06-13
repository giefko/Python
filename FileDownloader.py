import urllib
url = "http://infoman.teikav.edu.gr/vathmologies/xls/z_a_empeira.xls"
source = urllib.urlopen(url).read()
filename = "z_a_empeira.xls"
file = open(filename,'w')
file.write(source)
file.close()

