# -*- coding: utf-8 -*-
"""
:Autor: Adriano Leal
:Aluno: 11951
:email l911911951@alunos.ipbeja.pt
"""

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_protect


@login_required
def index(request):
    """
    Página principal do utilizador
    """

    TITULO = _(u'Internete das Coisas')

    #===========================================================================
    # acessorios = Accessory.objects.all()
    # tamLista = len(acessorios)
    #===========================================================================
    template = "home/index.html"
    return render_to_response(template,
                              locals(),
                              context_instance=RequestContext(request)
                              )

