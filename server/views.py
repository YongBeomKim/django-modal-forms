from bootstrap_modal_forms.generic import BSModalLoginView, BSModalCreateView
from .forms import CustomUserCreationForm, CustomAuthenticationForm 
from django.urls import reverse_lazy
from django.shortcuts import redirect



class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_message = '등록이 완료 되었습니다'
    success_url = reverse_lazy('books:index')


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'login.html'
    success_message = '로그인 성공'
    success_url = reverse_lazy('books:index')

# 로그아웃 함수를 정의합니다
from django.contrib import auth, messages

def logout_view(request):
    auth.logout(request)
    messages.warning(request, "로그아웃 되었습니다")
    return redirect('books:index')