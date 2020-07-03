from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.http import HttpResponseRedirect
import msal
import uuid

def login(request):
    print('Inside Login')
    request.session['state'] = str(uuid.uuid4())
    print(f'UUID Set {request.session}')
    auth_url = _build_auth_url(scopes=settings.SCOPE, state=request.session['state'], request=request)
    return redirect(auth_url)

def authorized(request):
    if request.get['state'] != request.session.get("state"):
        return redirect('home')  # No-OP. Goes back to Index page
    if "error" in request:  # Authentication/Authorization failure
        return redirect('error')
    if request.get['code']:
        cache = _load_cache(request)
        result = _build_msal_app(cache=cache).acquire_token_by_authorization_code(
            request.get['code'],
            scopes=settings.SCOPE,  # Misspelled scope would cause an HTTP 400 error here
            redirect_uri=reverse("authorized"))
        if "error" in result:
            return redirect('error')
        request.session["user"] = result.get("id_token_claims")
        _save_cache(request, cache)
    return redirect("home")

def logout(request):
    request.session.clear()  # Wipe out user and its token cache from session
    return redirect(  # Also logout from your tenant's web session
        settings.AUTHORITY + "/oauth2/v2.0/logout" +
        "?post_logout_redirect_uri=" + reverse("index", kwargs={'_external': True}))


def _load_cache(request):
    cache = msal.SerializableTokenCache()
    if request.session.get("token_cache"):
        cache.deserialize(request.session["token_cache"])
    return cache

def _save_cache(request, cache):
    if cache.has_state_changed:
        request.session["token_cache"] = cache.serialize()

def _build_msal_app(cache=None, authority=None):
    return msal.ConfidentialClientApplication(
        settings.CLIENT_ID, authority=authority or settings.AUTHORITY,
        client_credential=settings.CLIENT_SECRET, token_cache=cache)

def _build_auth_url(request, authority=None, scopes=None, state=None):
    return _build_msal_app(authority=authority).get_authorization_request_url(
        scopes or [],
        state=state or str(uuid.uuid4()),
        redirect_uri=request.build_absolute_uri(reverse("authorized")))