from django.shortcuts import redirect

class UserIsOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().id != request.user.id:
            return redirect('access_denied_view')
        return super().dispatch(request, *args, **kwargs)


class UserIsStudentMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.role != 'Student':
            return redirect('access_denied_view')
        return super().dispatch(request, *args, **kwargs)