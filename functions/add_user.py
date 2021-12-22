from utils.mongo import db_config
from json import loads
from models.users import Users , Location

def add_user(body)-> Users:
    _full_name = body["full_name"]
    _email = body["email"]
    _province = body["province"]
    _town = body["town"]
    _district = body["district"]

    db_config()

    address = Location(
        province = _province,
        town= _town,
        district=_district
    )

    user: Users = Users(
        full_name=_full_name,
        email=_email,
    ).save()

    user.address = address

    user.save()
    user.reload()

    return user


