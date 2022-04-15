from flask_marshmallow import Marshmallow

ma = Marshmallow()

class PeopleSchema(ma.Schema):
    """Schema"""
    class Meta:
        fields = (
        'id', 
        'checked', 
        'name', 
        'type', 
        'age',
        'description',
        'datetime',
        )