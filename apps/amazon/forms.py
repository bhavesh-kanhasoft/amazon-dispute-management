from django import forms
from .models import Order, Return, Dispute


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"


class ReturnForm(forms.ModelForm):
    class Meta:
        model = Return
        fields = "__all__"


class DisputeForm(forms.ModelForm):
    class Meta:
        model = Dispute
        fields = "__all__"

    # status = forms.ChoiceField(choices=Dispute.STATUS_CHOICES)

    # def __init__(self, *args, **kwargs):
    #     super(DisputeForm, self).__init__(*args, **kwargs)
    #     if self.instance is not None:
    #         print(self.instance)
    #         self.fields["return_order"].widget.attrs["readonly"] = True
    #         self.fields["return_order"].initial = self.instance.return_order.order.item
