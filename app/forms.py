from flask_security.forms import ConfirmRegisterForm, Required, TextField
from wtforms import IntegerField
from wtforms.validators import *

class ExtendedConfirmRegisterForm(ConfirmRegisterForm):
    first_name = TextField('First Name', [Required()])
    last_name = TextField('Last Name', [Required()])
    cell  = TextField('Telephone',[Length(min=10,max=10,message='Not a valid Phone number')])
    gender = TextField('Gender', [Required(),AnyOf(['Male','Female','male','female'], message='Please Enter Male or Female',)])
    college = TextField('College', [Optional()])
    batch = IntegerField('Batch',[Optional(),NumberRange(min=2000, max=2015, message="Enter valid Batch")])
    branch = TextField('Branch', [Optional()])

    # gender= db.Column(db.String(6))
    # accomodation =db.Column(db.Boolean(255))
    # time = db.Column(db.DateTime())
    # special= db.Column(db.String(255))
    # active = db.Column(db.Boolean())
    # confirmed_at = db.Column(db.DateTime())
