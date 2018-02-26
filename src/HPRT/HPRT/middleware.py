class AuthRequiredMiddleware(object):
    def process_request(self, request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('login')) # or http response
        return None