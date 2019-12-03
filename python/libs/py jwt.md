参考： [理解JWT（JSON Web Token）认证及python实践](https://segmentfault.com/a/1190000010312468)

例子
```
import jwt
import time

payload = {
    "iss": "gusibi.com",
    "iat": int(time.time()),
    "exp": int(time.time()) + 86400 * 7,
    "aud": "xx",
    "scopes": ['open'],
    
    "aa": "cc",
    'name': "name"
}
token = jwt.encode(payload, 'secret', algorithm='HS256')
print(token)
payload = jwt.decode(token, 'secret', audience='xx', algorithms=['HS256'])
payload = jwt.decode(token, verify=False)  # 不验证信息
print(payload)

'''
dic 有官方指定的key，程序在解密的时候会根据key的Value判断是否合法。这些key有

“exp”: 过期时间
“nbf”: 表示当前时间在nbf里的时间之前，则Token不被接受
“iss”: token签发者
“aud”: 接收者
“iat”: 发行时间

exp   
exp指过期时间，在生成token时，可以设置该token的有效时间，如果我们设置1天过期，1天后我们再解析此token会抛出
jwt.exceptions.ExpiredSignatureError: Signature has expired

nbf
nbf类似于token的 lat ，它指的是该token的生效时间，如果使用但是没到生效时间则抛出
jwt.exceptions.ImmatureSignatureError: The token is not yet valid (nbf)

iss
iss指的是该token的签发者，我们可以给他一个字符串。
注意，iss 在接收时如果不检验也没有问题，如果我们接收时需要检验但是又签名不一致，则会抛出
jwt.exceptions.InvalidIssuerError: Invalid issuer

aud
aud指定了接收者，接收者在接收时必须提供与token要求的一致的接收者（字符串），如果没写接收者或者接收者不一致会抛出
jwt.exceptions.InvalidAudienceError: Invalid audience

iat
iat指的是token的开始时间，如果当前时间在开始时间之前则抛出
jwt.exceptions.InvalidIssuedAtError: Issued At claim (iat) cannot be in the future.
'''
```
