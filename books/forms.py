from bootstrap_modal_forms.forms import BSModalForm
from django import forms
from .models import Book


class BookForm(BSModalForm):
    # 특정 필드의 form 속성을 OverWriting 합니다
    publication_date = forms.DateField(
        error_messages={'invalid': 'YYYY-MM-DD 양식을 맞추세요'}
    )
    class Meta:
        model = Book
        exclude = ['timestamp']