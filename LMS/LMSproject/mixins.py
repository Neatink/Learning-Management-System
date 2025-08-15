from django.shortcuts import redirect

def access_denied_redirect():
    return redirect('access_denied_view')

class UserIsOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().id != request.user.id:
            access_denied_redirect()
        return super().dispatch(request, *args, **kwargs)


class UserIsStudentMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.role != 'Student':
            access_denied_redirect()
        return super().dispatch(request, *args, **kwargs)
    

class UserIsAdminMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.role != 'Admin':
            access_denied_redirect()
        return super().dispatch(request, *args, **kwargs)