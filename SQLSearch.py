from components import Component
import os

Components = []
Plugins = []

filename = ""

def execute(path, sqlpath):
	filename = sqlpath
	with open(filename, 'rb') as file:
		lines = file.readlines()

	lines = str(lines)

	dbPrefix = getDbPrefix(path)

	beginExtensions = lines.find("VALUES", lines.find(dbPrefix+"extensions"), len(lines))

	iter = beginExtensions

	endExtensions = lines.find("ALTER TABLE", iter, len(lines)) #final da tabela com as informacoes

	# Encontrando Versao do Joomla

	positionFilesJoomla = lines.find("\\'files_joomla\\'", beginExtensions, endExtensions)

	j = lines.find("\"version\\", positionFilesJoomla, endExtensions)
	#print(j)
	joomlaVersion = lines[j:endExtensions].split(",")[0].split(":")[1].replace(":", "").replace("\\", "").replace(
		"\"", "")

	Components.append(Component("joomla", joomlaVersion))

	#Encontrando Componentes
	while 1:
		newIterValue = lines.find("\\'component\\'", iter, len(lines))
		iter = newIterValue + 1

		if newIterValue == -1 or newIterValue > endExtensions:
			break

		componentName = lines[newIterValue:endExtensions].split(",")[1].replace("\\'", "")

		j = lines.find("\"version\\", newIterValue+1, endExtensions)
		componentVersion = lines[j:endExtensions].split(",")[0].split(":")[1].replace(":", "").replace("\\", "").replace("\"", "")

		Components.append(Component(componentName.replace("com_", ""), componentVersion))

	Components.sort()

	#Encontrando Plugins
	iter = beginExtensions

	while 1:
		newIterValue = lines.find("\\'plugin\\'", iter, endExtensions)
		iter = newIterValue + 1

		if newIterValue == -1 or newIterValue > endExtensions:
			break

		l1 = lines.find("plg_", newIterValue+1, endExtensions)
		l2 = lines.find("PLG_", newIterValue+1, endExtensions)

		if l1 != -1 and l2 != -1:
			l = min(l1, l2)
		else:
			l = max(l1, l2)

		pluginName = lines[l:endExtensions].split(",")[0].replace("\\", "").replace("'", "").replace("\"", "")

		j = lines.find("\"version\\", newIterValue+1, endExtensions)
		pluginVersion = lines[j:endExtensions].split(",")[0].split(":")[1].replace(":", "").replace("\\", "").replace("\"", "")

		Plugins.append(Component(pluginName.replace("plg_", "").replace("PLG_", ""), pluginVersion))

	Plugins.sort()



def getAllComponents():
	return Components

def getAllPlugins():
	return Plugins

def getDbPrefix(path):
	reduced = os.path.split(path)[0]
	reduced = os.path.split(reduced)[0]
	file = os.path.join(reduced, 'configuration.php')
	with open(file, 'rb') as f:
		lines = f.readlines()
	for l in lines:
		line = str(l)
		if line.find("dbprefix") != -1:
			result = line.split("=")[1].split("'")[1]
			break
	return result
