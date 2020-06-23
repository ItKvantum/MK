from wtforms import Form, StringField, TextAreaField
from wtforms.validators import DataRequired, Email
class PostForm(Form):
    title = StringField('Название')
    text = TextAreaField('Текст поста')

class ContactForm(Form):
    name = StringField("Имя: ", validators=[DataRequired()])
    email = StringField("Электронная почта: ", validators=[Email()])
    message = TextAreaField("Message", validators=[DataRequired()])