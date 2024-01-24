from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from .models import Order, Return, Dispute
from .forms import OrderForm, ReturnForm, DisputeForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect


class OrderListView(ListView):
    model = Order
    template_name = "amazon/order_list.html"


def create_order(request):
    if request.method == "POST":
        # If the form is submitted, process the data
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()  # This will create a new Order instance in the database
            return redirect(
                "order_list"
            )  # Redirect to the order list page or any other page you want
    else:
        # If it's a GET request, render the form
        form = OrderForm()

    return render(request, "amazon/create_order.html", {"form": form})


def dispute_list(request):
    disputes = Dispute.objects.all()
    return render(request, "amazon/dispute_list.html", {"disputes": disputes})


def dispute_create(request):
    if request.method == "POST":
        form = DisputeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dispute_list")
    else:
        form = DisputeForm()
    return render(request, "amazon/dispute_form.html", {"form": form})


def dispute_update(request, pk):
    dispute = get_object_or_404(Dispute, pk=pk)
    if request.method == "POST":
        form = DisputeForm(request.POST, instance=dispute)
        if form.is_valid():
            form.save()
            return redirect("dispute_list")
    else:
        form = DisputeForm(instance=dispute)
    return render(
        request, "amazon/dispute_form.html", {"form": form, "object": dispute}
    )


def dispute_delete(request, pk):
    dispute = get_object_or_404(Dispute, pk=pk)
    if request.method == "POST":
        dispute.delete()
        return redirect("dispute_list")
    return render(request, "amazon/dispute_confirm_delete.html", {"object": dispute})


# class ReturnCreateView(CreateView):
#     model = Return
#     form_class = ReturnForm
#     template_name = "amazon/return_create.html"


# class DisputeCreateView(CreateView):
#     model = Dispute
#     form_class = DisputeForm
#     template_name = "amazon/dispute_create.html"
