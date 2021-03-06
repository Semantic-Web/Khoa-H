# 20050628 *pike 

# very simple examples script for pySesame
# this does the same as tests.py, but in a human way.


import pySesame

# CONFIG ---------------------
# select an *empty* test database, plain rdf sail
# on which the user has read and write access

url 		= 'http://localhost:7080'
path 		= '/sesame/'
user 		= 'yourusername'
password 	= 'youruserpassword'
repository 	= 'yourrepositoryid'

# toggle tests to perform
tests	= {}
tests["anon"]			= True
tests["login"]			= True
tests["clear"]			= True
tests["upload"]			= True
tests["uploadbroken"]		= True
tests["uploadurl"]		= True
tests["extract"]		= True 
tests["rdql"]			= True
tests["rdqlrdf"]		= True 
tests["serqls"]			= True 
tests["serqlc"]			= True 
tests["remove"]			= True  

# ----------------------------

#import some example data
from tests_data import w3c, w3cRemoved, w3cResult, postURL
from tests_data import serqlSQuery, serqlCQuery, rdqlQuery, rdqlQueryResult
from tests_data import rdqlQueryRDF, serqlCQueryRDF, postcon


if tests["anon"]:
	# test some features on  anonymous acces
	print 24*'='
	print 'Testing anonymous connection'
	connection = pySesame.SesameConnection(url, path, 'debug')
	repos = connection.repositories()
	print 'There are %s repositories available for the anonymous user:'%len(repos)
	print "\tsesame id\t:read\t:write\t:title"
	for repo in repos:
		print "\t%(id)s\t:%(readable)s\t:%(writeable)s\t:%(title)s"%repo
	print 'closing anonymous connection'
	connection.close()

# test login / logoff
if tests["login"]:
	print 24*'='
	print 'Testing login connection'
	connection = pySesame.SesameConnection(url, path, 'debug')
	connection.login(user, password)
	print 'received sessionid %s '%connection.cookie
	repos = connection.repositories()
	print 'There are %s repositories available for user  %s:'%(len(repos),user)
	print "\tsesame id\t:read\t:write\t:title"
	for repo in repos:
		print "\t%(id)s\t:%(readable)s\t:%(writeable)s\t:%(title)s"%repo
	print 'logging out'
	connection.logout()
	print 'closing sesame connection .. which is useless because I already logged out'
	connection.close()

# more tests require logging in

print 
print 'loggin in again, for the next set of tests:'
connection = pySesame.SesameConnection(url, path, 'debug')
connection.login(user, password)

if tests["clear"]:
	print 24*'='
	print 'Testing clearing repo %s'%repository
	connection.clear(repository)
	print "....ok"
		
if tests["upload"]:
	print 24*'='
	print 'Testing uploading good rdf'
	connection.uploadData(repository, postcon)
	print 'good, clearing repo %s'%repository
	connection.clear(repository)
	
if tests["uploadbroken"]:
	print 24*'='
	print 'Testing uploading broken rdf'
	try:
		connection.uploadData(repository,postcon[:100])
		print 'bad ! .. I didn\'t get get an error ?'
	except:
		print 'good !.. I got an error :)'
		
if tests["uploadurl"]:
	print 24*'='
	print 'Testing uploading from url'
	connection.uploadURL(repository, postURL)
	print 'good, clearing repo %s'%repository
	connection.clear(repository)


if tests["extract"]:
	print 24*'='
	print 'Testing extracting the repo'
	print 'uploading----------'
	print w3c
	connection.uploadData(repository, w3c)
	result = connection.extract(repository, 'on', 'on')
	print '--------------------'
	if result!=w3cResult: 
		print "unexpected result ? ----------"
		print result
		print '--------------------'
	else:
		print "ok"
	print 'clearing repo %s'%repository
	connection.clear(repository)
	
if tests["rdql"]:
	print 24*'='
	print 'testing rdqlquery with table result'
	print 'uploading some dummy data  ..'
	connection.uploadData(repository, postcon)
	print 'submitting query----------'
	print rdqlQuery
	result = connection.tableQuery(repository, 'RDQL', rdqlQuery)
	if result != rdqlQueryResult:
		print "unexpected result ? ----------"
		print result
		print '--------------------'
	else:
		print "ok"
	print 'clearing repo %s'%repository
	connection.clear(repository)
	
if tests["rdqlrdf"]:
	print 24*'='
	print 'testing rdqlquery with rdf result'
	print 'uploading some dummy data ..'
	connection.uploadData(repository, postcon)
	print 'submitting query----------'
	print rdqlQuery
	result = connection.tableQuery(repository, 'RDQL', rdqlQuery,'rdf', 'rdfxml')
	if result != rdqlQueryRDF:
		print "unexpected result ? ----------"
		print result
		print '--------------------'
	else:
		print "ok"
	print 'clearing repo %s'%repository
	connection.clear(repository)                                    
	
	
if tests["serqls"]:
	print 24*'='
	print 'testing serql select query'
	print 'uploading some dummy data ..'
	connection.uploadData(repository, postcon)
	print 'submitting query----------'
	print serqlSQuery
	result = connection.tableQuery(repository, 'SeRQL', serqlSQuery)
	if result != rdqlQueryResult:
		print "unexpected result ? ----------"
		print result
		print '--------------------'
	else:
		print "ok"
	print 'clearing repo %s'%repository
	connection.clear(repository)          
	
	
if tests["serqlc"]:
	print 24*'='
	print 'testing serql construct query'
	print 'uploading some dummy data ..'
	connection.uploadData(repository, postcon)
	print 'submitting query----------'
	print serqlCQuery
	result = connection.graphQuery(repository, 'SeRQL', serqlCQuery, 'rdfxml')
	if result != serqlCQueryRDF:
		print "unexpected result ? ----------"
		print result
		print '--------------------'
	else:
		print "ok"
	print 'clearing repo %s'%repository
	connection.clear(repository)                              
	
if tests["remove"]:
	print 24*'='
	print 'testing remove query'
	print 'uploading some dummy data ..'
	connection.uploadData(repository, w3c)
	print 'submitting query----------'
	connection.remove(repository, '<http://www.w3.org/>',
		'<http://purl.org/dc/elements/1.1/title>',
		'"World Wide Web Consortium"')
	result = connection.extract(repository, 'on', 'on')
	if result != w3cRemoved:
		print "unexpected result ? ----------"
		print result
		print '--------------------'
	else:
		print "ok"
	print 'clearing repo %s'%repository
	connection.clear(repository)     	
		
	
connection.close()
	
