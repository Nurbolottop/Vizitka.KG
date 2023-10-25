from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model, authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

def custom_password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model().objects.get(id=uid)

        if default_token_generator.check_token(user, token):
            if request.method == "POST":
                new_password = request.POST.get('new_password')
                confirm_password = request.POST.get('confirm_password')

                if new_password and confirm_password and new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()

                    authenticated_user = authenticate(username=user.username, password=new_password)
                    if authenticated_user:
                        login(request, authenticated_user)
                        return redirect('password_reset_complete')  # Замените 'password_reset_complete' на ваш URL-путь для страницы успешного сброса пароля
                    else:
                        return HttpResponse('Не удалось аутентифицировать пользователя')
                else:
                    return HttpResponse('Пароли не совпадают или не введены')
            else:
                return render(request, 'users/forgot-password_confirm.html', {'uidb64': uidb64, 'token': token})
        else:
            return HttpResponse('Недействительный токен для сброса пароля.')
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        return HttpResponse('Недействительный пользователь.')