from ctypes import*

dna = cdll.LoadLibrary('DDNAToolKit.dll')
gpod = cdll.LoadLibrary(r'C:\\Users\Kevin\dev.local\python\lib\gpod.dll')
d = cdll.LoadLibrary('C:/Users/Kevin/dev.local/python/lib/gpod.dll')
print(dna)
print(gpod)






#print(gpod.itdb_get_mountpoint('USB\\VID_05AC&PID_12A8\\714f8a24ab5da1ce252ae8969f865a48a052004d'))

