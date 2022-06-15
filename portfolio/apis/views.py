from django.http import HttpResponse





def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# @api_view(['GET'])
# def post_collection(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
