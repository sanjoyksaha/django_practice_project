from django.http import HttpResponse
from django.shortcuts import render
from .models import Room

# rooms = [
#     {
#         "id": 1,
#         "name": "Learning django.",
#         "details": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
#                    "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
#                    "when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
#                    "It has survived not only five centuries, but also the leap into electronic typesetting, remaining "
#                    "essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing"
#                    " Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker "
#                    "including versions of Lorem Ipsum"
#     },
#     {
#         "id": 2,
#         "name": "Intermediate Course.",
#         "details": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and w"
#     },
#     {
#         "id": 3,
#         "name": "Python3 & Django Crush Course For Beginner.",
#         "details": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on t"
#     },
#     {
#         "id": 4,
#         "name": "Learn django Rest API's.",
#         "details": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum w"
#     }
# ]


# Create your views here.
def home(request):
    return render(request, 'base/home.html')


def room(request):
    # return HttpResponse("Rooms")
    rooms = Room.objects.all()
    data = {"rooms": rooms}
    return render(request, 'base/rooms.html', data)


def room_details(request, id):
    room_detail = Room.objects.get(id=id)

    data = {"room_details": room_detail}
    return render(request, 'base/room_detail.html', data)
