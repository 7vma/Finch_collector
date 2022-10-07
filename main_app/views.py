from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Bird
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse


class Home(TemplateView):
    template_name = "home.html"
class About(TemplateView):
    template_name = "about.html"



# birds = [
#     Bird("Star Finch",
#             "http://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Neochmia_ruficauda.jpg/547px-Neochmia_ruficauda.jpg", 
#             "The Star Finch belongs to a group commonly known as the Australian Grassfinches.  It is native to Northern Australia, where it frequents wooded savannas, rice fields and cane plantations.  Much of its time spent foraging on the ground, often in the company of Crimson Finches."),
#     Bird("Masked Finch",
#             "http://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Poephila_personata_-Toledo_Zoo%2C_Ohio%2C_USA-6a.jpg/590px-Poephila_personata_-Toledo_Zoo%2C_Ohio%2C_USA-6a.jpg",
#             "Hailing from Northern Australia, Masked Finches are found in thorn brush, grassy scrub, parks and gardens, always within daily flying distance of water."),
#     Bird("Blue Back Lady Gouldian ", 
#             "https://leesexoticbirds.com/wp-content/uploads/2018/02/Blue_Gouldian.jpg", 
#             "The blue back lady gouldian has a salmon or black mask with a black outline followed by a blue border, blue back, an off-white abdomen, black and blue tail, and a purple breast."),    
#     Bird("Green Back Lady Gouldian",
#         "https://leesexoticbirds.com/wp-content/uploads/2018/02/Green_Back_Lady_Gouldian.jpeg",
#         "Adult males with a black head have a very distinctive multicolored pattern. They have a black head, chin and throat. Adult males with a red head have a bright red forehead, crown and face, bordered with black. Adult males with a yellow-head have a golden-yellow or orange forehead, crown and face, bordered with black."),
#     Bird("Red Cheek Cordon Bleu Finch",
#         "https://leesexoticbirds.com/wp-content/uploads/2018/02/Cordon_Blue_Pair-768x720.jpg",
#         "The adult male cordon bleu has uniformly brown upperparts, pale blue breast, flanks and tail and a yellow belly. They have a red patch on each cheek. Females are similar in color but are duller, and lack the cheek spot. Juveniles are colored like the female, but with blue restricted to the face and throat only."),
#     Bird("Purple Grenadier",
#         "https://leesexoticbirds.com/wp-content/uploads/2018/02/Purple_Grenadier-768x512.jpg",
#         "A male purple grenadier has a blue face, broken edges to blue underparts while an adult female has pale blue around the eye and lacks blue underparts."),
#     ]

class BirdList(TemplateView):
    template_name = "bird_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["birds"] = Bird.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["birds"] = Bird.objects.all()
            context["header"] = "Rare Birds"
        return context

class BirdCreate(CreateView):
    model = Bird
    fields = ['name', 'img', 'bio', 'verified_bird']
    template_name = "bird_create.html"
    success_url = "/birds/"
class BirdDetail(DetailView):
    model = Bird
    template_name = "bird_detail.html"

class BirdUpdate(UpdateView):
    model = Bird
    fields = ['name', 'img', 'bio', 'verified_bird']
    template_name = "bird_update.html"
    
    def get_success_url(self):
        return reverse('bird_detail', kwargs={'pk': self.object.pk})

class BirdDelete(DeleteView):
    model = Bird
    template_name = "bird_delete_confirmation.html"
    success_url = "/birds/"