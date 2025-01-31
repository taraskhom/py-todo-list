from django import forms
from todo_app.models import TaskModel, TagModel


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['content', 'deadline', 'tags']

    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Enter task content here...'
        })
    )

    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local'
        }),
        required=False
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=TagModel.objects,
        widget=forms.CheckboxSelectMultiple
    )
