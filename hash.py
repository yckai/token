import hashlib
def hash(id):
    secret = 'Sig1'
    group = 'group' + str(id)
    role = 'user'
    sign = hashlib.md5(bytes(role + secret, encoding='utf8'))
    return (group + '.' + role + '.' + sign.hexdigest())

def valideHash(role, signature):
    secret = 'Sig1'
    roleCheckUser = 'user'
    roleCkeckAdmin = 'admin'
    if role == 'user':
        comparsigntmp = hashlib.md5(bytes(roleCheckUser + secret, encoding='utf8'))
        comparsign = comparsigntmp.hexdigest()
        if signature == comparsign:
            code = 1
            return ("valid token User", code)
        else:
            code = 2
            return ("Invalid User Role or Signature", code)
    else:
        comparsigntmp = hashlib.md5(bytes(roleCkeckAdmin + secret, encoding='utf8'))
        comparsign = comparsigntmp.hexdigest()
        if signature == comparsign:
            code = 1
            return ("Admin ok", code)
        else:
            code = 2
            return ("Invalid Admin Role or Signature", code)