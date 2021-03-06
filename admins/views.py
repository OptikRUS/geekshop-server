from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from users.models import User
from products.models import ProductCategory, Product
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm, CategoryAdminRegistrationForm, \
    CategoryAdminEditForm, ProductAdminRegistrationForm, ProductAdminEditForm


class CommonMixin(SuccessMessageMixin):
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CommonMixin, self).dispatch(request, *args, **kwargs)


@user_passes_test(lambda user: user.is_staff)
def index(request):
    context = {'title': 'Админ-панель'}
    return render(request, 'admins/index.html', context)


class AdminUserListView(CommonMixin, ListView):
    model = User
    template_name = 'admins/admin-users-read.html'
    title = 'Админка/Пользователи'


class AdminUserCreateView(CommonMixin, CreateView):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegistrationForm
    success_url = reverse_lazy('admin_staff:admin_users')
    title = 'Админка/Создание пользователя'
    success_message = 'Пользователь успешно создан!'


class AdminUserUpdateView(CommonMixin, UpdateView):
    model = User
    form_class = UserAdminProfileForm
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    title = 'Админка/Редактирование пользователя'
    success_message = 'Профиль пользователя успешно изменён!'


class AdminUserDeleteView(CommonMixin, DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    title = 'Админка/Редактирование пользователя'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.safe_delete()
        return HttpResponseRedirect(self.success_url)


class AdminCategoryListView(CommonMixin, ListView):
    model = ProductCategory
    template_name = 'admins/admin-categories-read.html'
    title = 'Админка/Категории'


class AdminCategoryCreateView(CommonMixin, CreateView):
    model = ProductCategory
    template_name = 'admins/admin-category-create.html'
    form_class = CategoryAdminRegistrationForm
    success_url = reverse_lazy('admin_staff:admin_categories')
    title = 'Админка/Создание категории'
    success_message = 'Категория успешно создана!'


class AdminCategoryUpdateView(CommonMixin, UpdateView):
    model = ProductCategory
    form_class = CategoryAdminEditForm
    template_name = 'admins/admin-category-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_categories')
    title = 'Админка/Редактирование категории'
    success_message = 'Категория успешно изменёна!'


class AdminCategoryDeleteView(CommonMixin, DeleteView):
    model = ProductCategory
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_categories')
    title = 'Админка/Редактирование пользователя'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.safe_delete()
        return HttpResponseRedirect(self.success_url)


class AdminProductListView(CommonMixin, ListView):
    model = Product
    template_name = 'admins/admin-products-list.html'
    title = 'Админка/Продукты'


class AdminProductCreateView(CommonMixin, CreateView):
    model = Product
    template_name = 'admins/admin-product-create.html'
    form_class = ProductAdminRegistrationForm
    success_url = reverse_lazy('admin_staff:admin_products')
    title = 'Админка/Создание товара'
    success_message = 'Товар успешно создан!'


class AdminProductUpdateView(CommonMixin, UpdateView):
    model = Product
    form_class = ProductAdminEditForm
    template_name = 'admins/admin-product-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_products')
    title = 'Админка/Редактирование товара'
    success_message = 'Товар успешно изменён!'


class AdminProductDeleteView(CommonMixin, DeleteView):
    model = Product
    template_name = 'admins/admin-product-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_products')
    title = 'Админка/Редактирование товара'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.safe_delete()
        return HttpResponseRedirect(self.success_url)

# @user_passes_test(lambda user: user.is_staff)
# def admin_users(request):
#     users = User.objects.all()
#     context = {
#         'title': 'Админка/Пользователи',
#         'users': users,
#     }
#     return render(request, 'admins/admin-users-read.html', context)

# @user_passes_test(lambda user: user.is_staff)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Пользователь успешно создан!')
#             return HttpResponseRedirect(reverse('admin_staff:admin_users'))
#         else:
#             print(form.errors)
#     else:
#         form = UserAdminRegistrationForm()
#     context = {'title': 'Админка/Создание пользователя', 'form': form}
#     return render(request, 'admins/admin-users-create.html', context)

# @user_passes_test(lambda user: user.is_staff)
# def admin_users_update(request, pk):
#     selected_user = User.objects.get(id=pk)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(instance=selected_user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Профиль пользователя успешно изменён!')
#             return HttpResponseRedirect(reverse('admin_staff:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=selected_user)
#     context = {'title': 'Админка/Редактирование пользователя', 'form': form, 'selected_user': selected_user}
#     return render(request, 'admins/admin-users-update-delete.html', context)

# @user_passes_test(lambda user: user.is_staff)
# def admin_users_delete(request, pk):
#     user = User.objects.get(id=pk)
#     user.safe_delete()
#     return HttpResponseRedirect(reverse('admin_staff:admin_users'))
