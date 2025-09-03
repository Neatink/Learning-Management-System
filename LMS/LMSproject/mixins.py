from django.shortcuts import redirect

def access_denied_redirect():
    return redirect('access_denied_view')

class UserIsOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().id != request.user.id:
            return access_denied_redirect()
        return super().dispatch(request, *args, **kwargs)


class UserIsNotTeacherMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.role == 'Teacher':
            return access_denied_redirect()
        return super().dispatch(request, *args, **kwargs)
    

class UserIsAdminMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.role != 'Admin':
            return access_denied_redirect()
        return super().dispatch(request, *args, **kwargs)
    

class UserIsNotStudentMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.role == 'Student':
            return access_denied_redirect()
        return super().dispatch(request, *args, **kwargs)