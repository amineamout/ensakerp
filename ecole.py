from osv import fields, osv

class ecole(osv.osv):

	_name = "ecole"
	_description = "Module ENSAK pour la demonstration"
	'''
	_comlums : dictionnaire d'objets
	'''
	_columns = {
	'nom' : fields.char('Nom', size=100, required = True),
	'type' : fields.selection([('com','Commerce'),('ing','Ingenieur')],'Type'),
	'ville' : fields.char('Ville', size=40, required = True),
	'tel' : fields.char('Num. Telephone', size=10),
	'ecole_annee' : fields.integer('Annee creation')
	}

ecole()
