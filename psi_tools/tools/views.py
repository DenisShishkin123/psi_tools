from django.shortcuts import render
from django.views.generic import TemplateView, View

def tools(request):
    return render(request, "tools/tools.html")

# def tool(request):
#     return

class ToolsView(View):
    def get(self, request):
        return render(request, "tools/tools.html")

class ToolsTemplateView(TemplateView):
    template_name = "tools/tools.html"
    extra_context = {
        "title": "Инструменты"
    }