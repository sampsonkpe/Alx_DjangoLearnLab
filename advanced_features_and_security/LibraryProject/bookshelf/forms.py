from django import forms

class ExampleForm(forms.Form):
    search_query = forms.CharField(
        max_length=100,
        required=True,
        help_text="Enter your search query"
    )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']  # adjust fields as per your model

