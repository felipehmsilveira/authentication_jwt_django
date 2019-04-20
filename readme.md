=========================================================

#Login:

url: http://localhost:8000/login/

verb: post

body: {"nome":"","password":""}

return: {"token":"J0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ"}

=========================================================

#Refresh-token:

url: http://localhost:8000/refresh-token/

verb: post

body: {"token":"J0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ"}

return: {"token":"J0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ"}

=========================================================

#Verify-token:

url: http://localhost:8000/api-token-verify/

verb: post

body: {"token":"J0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ"}

return: {"token":"J0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ"}


=========================================================


#To Authentication in all urls

headers: {"Authorization": "JWT J0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ"}