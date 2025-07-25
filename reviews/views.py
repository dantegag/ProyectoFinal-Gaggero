from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

class EditarReviewView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['pelicula', 'texto', 'imagen']
    template_name = 'reviews/editar_review.html'
    success_url = reverse_lazy('ver_reviews')

    def test_func(self):
        review = self.get_object()
        return review.autor == self.request.user


class EliminarReviewView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'reviews/eliminar_review.html'
    success_url = reverse_lazy('ver_reviews')

    def test_func(self):
        review = self.get_object()
        return review.autor == self.request.user

@login_required
def crear_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.autor = request.user
            review.save()
            return redirect('ver_reviews')
    else:
        form = ReviewForm()
    return render(request, 'reviews/crear_review.html', {'form': form})

def ver_reviews(request):
    termino = request.GET.get('q')
    if termino:
        reviews = Review.objects.filter(
            Q(pelicula__titulo__icontains=termino) |
            Q(autor__username__icontains=termino)
        )
    else:
        reviews = Review.objects.all()

    return render(request, 'reviews/ver_reviews.html', {'reviews': reviews})

