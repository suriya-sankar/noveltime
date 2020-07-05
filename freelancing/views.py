from django.http import HttpResponse
from django.conf import settings 
from django.shortcuts import redirect
from .models import *
import docx


from django.shortcuts import render 

def index(request):
    all_stories=story.objects.all().order_by('upload_time')
    return render(request,'index.html',{'stories':all_stories.reverse()})

def fileupload(request):
    all_stories=story.objects.all()
    return render(request,'uploadingfile.html',{'stories':all_stories})
def fileupload_story(request):
     if request.method=='POST':
       
       story_name=request.POST['story_name']
       story_description=request.POST['story_description']
       story_tile=request.FILES['story_tile']
       story_category=request.POST['category']
       
       data=story()
       data.story_title=story_name
       data.story_descrtiption=story_description
       data.story_title_pic=story_tile
       data.category=story_category

       data.save()
       return redirect('fileupload')
def fileupload_chapter(request):
    if request.method=='POST':
        story_name=request.POST['story_name']
       
        chapter_name=request.POST['chapter_name']
        chapter_number=request.POST['chapter_number']
        author_name=request.POST['author_name']
        chapter_story=request.FILES['chapter_file']   
        chapter_pic=request.FILES['chapter_pic']
        chapter_description=request.POST['chapter_description']
        chap=chappter()
        chap.story_name=story_name
        chap.chapter_name=chapter_name
        chap.author_name=author_name
        chap.chapter_description=chapter_description
        chap.chapter_number=chapter_number
        chap.chapter_story=chapter_story
        chap.chapter_image=chapter_pic
        chap.save()
        return redirect('fileupload') 
def chapter_page(request,s_title):
    # print(s_title)
    chapters=chappter.objects.filter(story_name=s_title).order_by('chapter_time')
    
    return render(request,'chapter_slide.html',{'chap':chapters})
    # return render(request,'uploadingfile.html',{'stories':all_stories})
def reading_page(request,ss_title,c_num):
    
     
     
     chapter=chappter.objects.get(story_name=ss_title,chapter_number=c_num)
     commentss=comments.objects.filter(story_name=ss_title,chapter_number=c_num).order_by('comment_time')

     
     story=chapter.chapter_story
     doc=docx.Document(story)
     para=doc.paragraphs
   
    
   
     
    
     
     return render(request,'individual_page.html',{'chap':chapter,'para':para,'comments':commentss.reverse()})

def search(request):
    if request.method=='POST':
        val=request.POST['search']
        sto=story.objects.filter(story_title__contains=val)
        print(sto)
        return render(request,'index.html',{'stories':sto})   
def previous(request,s_name,c_num):

  
    if c_num=='1':
        return chapter_page(request,s_name)
    else:
        # chapter=chappter.objects.filter(story_name=s_name,chapter_number=(c_num-1))
        c_num=int(c_num)-1
        return reading_page(request,s_name,c_num)
def next_chap(request,s_name,c_num):
    print("next")
    chapters=chappter.objects.filter(story_name=s_name)
    num=len(chapters)
    if c_num==str(num):
        return chapter_page(request,s_name)
    else:
        c_num=int(c_num)+1    
        return reading_page(request,s_name,c_num)
def add_comment(request):
  if request.is_ajax(): 
    if request.method=='POST':
        print("hi")
        story_name=request.POST['story_name']   
        chapter_name=request.POST['chapter_name']
        chapter_number=request.POST['chapter_number']
        user_name=request.POST['comment_name']
        comment_text=request.POST['comment_text']
        print(story_name)
        comment=comments()
        comment.story_name=story_name
        comment.chapter_name=chapter_name
        comment.chapter_number=chapter_number
        comment.commenter_name=user_name
        comment.comments=comment_text
        comment.save()
        
        return reading_page(request,story_name,chapter_number)  
         