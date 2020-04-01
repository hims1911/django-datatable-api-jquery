from django.shortcuts import render
from .models import Post,PostDetails,Format
from .serializers import PostSerializer,PostDetailSerializer,FormatListSerializer
from django.http import HttpResponse,JsonResponse,HttpResponseNotFound
from django.template import loader


# Create your views here.
def index(request):
    '''new_obj = Post()
    new_obj.name = "hey ya!"
    new_obj.id_val = True
    new_obj.save()
    new_obj_1 = PostDetail(request,pk=new_obj.pk)
    print(new_obj_1)
    #new_obj_1.description = "the thing is description added"
    #new_obj_1.save()

    context = {
        'new_post_id' : new_obj.id,
    }'''
    template = loader.get_template('index.html')
    if(request.method =='GET'):
        post_all = Post.objects.all()
        post_serializer = PostSerializer(post_all,many=True)
        context = {
            'new_post_id' : post_serializer.data,
        }
        return HttpResponse(template.render(context, request))

    return HttpResponseNotFound("Not Found")
def PostList(request):
    if request.method == 'GET':
        post_all = Post.objects.all()
        post_serializer = PostSerializer(post_all, many=True)
        return JsonResponse(post_serializer.data, safe=False)

def PostDetail(request,pk):
    if(request.method == 'GET'):
        post_one = Post.objects.get(pk= pk)
        post_serializer = PostSerializer(post_one)
        return JsonResponse(post_serializer.data,safe= False)

def PostDetails_view(request,pk):
    if(request.method == 'GET'):
        post_detail = PostDetails.objects.get(pk = pk)
        post_detail_serializer = PostDetailSerializer(post_detail)
        context = {
            'postDetailData' : post_detail_serializer.data
        }
        template = 'post_detail.html'
        template = loader.get_template(template)
        return HttpResponse(template.render(context, request))
        #return JsonResponse(post_detail_serializer.data, safe= False)

def FormatList(request):
    if(request.method == 'GET'):
        format_list = Format.objects.all()
        format_list_serializer = FormatListSerializer(format_list, many=True)
        context = {
            'formatListData' : format_list_serializer.data
        }
        template = 'format.html'
        template = loader.get_template(template)
        return HttpResponse(template.render(context, request))

