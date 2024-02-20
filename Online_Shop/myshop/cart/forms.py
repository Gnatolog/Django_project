from django import forms  # импортируем формы джанго

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    # Возможность добавления от 0 до 20
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int)

    # Нужно ли добавить к существуещему количеству или добавить отдельно
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
