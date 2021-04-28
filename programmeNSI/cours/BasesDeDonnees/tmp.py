texte="and 	as 	assert 	break 	class 	continue 	def 	del elif 	else except 	exec  	finally 	for 	from 	global if 	import 	in 	is 	lambda 	not 	or 	pass print  	raise 	return 	try 	while 	with 	yield"
liste=texte.split()
print("var motsPython = "+str(liste)+";")

listFunc="abs()	delattr()	hash()	memoryview()	set()all()	dict()	help()	min()	setattr()any()	dir()	hex()	next()	slice()ascii()	divmod()	id()	object()	sorted()bin()	enumerate()	input()	oct()	staticmethod()bool()	eval()	int()	open()	str()breakpoint()	exec()	isinstance()	ord()	sum()bytearray()	filter()	issubclass()	pow()	super() bytes()	float()	iter()	print()	tuple()callable()	format()	len()	property()	type()chr()	frozenset()	list()	range()	vars()classmethod()	getattr()	locals()	repr()	zip()compile()	globals()	map()	reversed()	__import__()complex()	hasattr()	max()	round()"
liste=listeFunc.split('()')
print("var fonctionsReserveesPython = "+str(liste)+";")
