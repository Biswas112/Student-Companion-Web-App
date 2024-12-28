from django.shortcuts import render,redirect
from dashboard.models import *
from .forms import *
from django.contrib import messages
from youtubesearchpython import VideosSearch
import requests, wikipedia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse

def home(request):

    return render (request,'home.html')
#-----------------------------------------------------------------------------------

def nots(request):
    if request.method=='POST':
        form=Notesform(request.POST)
        if form.is_valid():
           nots=notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
           nots.save()
        messages.success(request,f"Notes Added from {request.user.username} successfully")
    else:       
      form=Notesform()
    note=notes.objects.filter(user=request.user).order_by('title')
    data={'note':note,
          'form':form}
    return render(request,'notes.html',data)
#------------------------------------------------------------------------------------

def notes_det(request,id):
    note=notes.objects.get(id=id)
    return render(request,'notes_detail.html',{'note':note})
#-----------------------------------------------------------------------------------

def delete_note(request,pk=None):
    notes.objects.get(id=pk).delete()
    return redirect('notes')
#------------------------------------------------------------------------------------

def home_work(request):
    if request.method=='POST':
        form=Homeworkform(request.POST)
        if form.is_valid():
            try:
                finished=request.POST['is_finished']
                if finished=='on':
                    finished=True
                else:
                    finished=False
            except:
                    finished=False
                    
            hw=homework(user=request.user,subject=request.POST['subject'],title=request.POST['title'],description=request.POST['description'],due=request.POST['due'],is_finished=finished)
            hw.save()
            messages.success(request,f'Homework added from {request.user.username}!!!')
    else:
            
        form=Homeworkform()
    Home_work=homework.objects.filter(user=request.user).order_by('due')
    if len(Home_work)==0:
        Home_work_done=True
    else:
        Home_work_done=False
        
    data={'Home_work':Home_work,
          'form':form,
          'Home_work_done':Home_work_done }
    return render(request,'homework.html',data)
#------------------------------------------------------------------------------------

def update_homework(request,pk=None):
    home_work=homework.objects.get(id=pk)
    if home_work.is_finished ==True:
        home_work.is_finished =False
    else:
        home_work.is_finished=True
    home_work.save()
    return redirect('homework')

#-------------------------------------------------------------------------------------
def home_del(request,pk=None):
    homework.objects.filter(id=pk).delete()
    return redirect('homework')
#-------------------------------------------------------------------------------------
def tube(request):
    result_list = []

    if request.method == 'POST':
        form = dashboardform(request.POST)
        text = request.POST['text']
        video = VideosSearch(text, limit=10)
        video_results = video.result().get('result', [])

        if video_results:
            for i in video_results:
                result_dic = {
                    'input': text,
                    'title': i.get('title', 'No Title'),
                    'duration': i.get('duration', 'No Duration'),
                    'thumbnails': i.get('thumbnails', [{'url': 'No Thumbnail'}])[0].get('url', 'No Thumbnail'),
                    'channel': i.get('channel', {}).get('name', 'No Channel'),
                    'link': i.get('link', 'No Link'),
                    'views': i.get('viewCount', {}).get('short', 'No Views'),
                    'published': i.get('publishedTime', 'No Published Time')
                }

                desc = ""
                if 'descriptionSnippet' in i:
                    for j in i['descriptionSnippet']:
                        desc += j.get('text', '')
                result_dic['description'] = desc

                result_list.append(result_dic)

        data = {'form': form, 'result': result_list}
        return render(request, 'youtube.html', data)

    else:
        form = dashboardform()

    data = {'form': form}
    return render(request, 'youtube.html', data)
#------------------------------------------------------------------------------------

def to_do(request):
    if request.method=='POST':
        form=todo_form(request.POST)
        if form.is_valid():
            try:
              finished=request.POST['is_finished']
              if finished=='on':
                  finished=True
              else:
                  finished=False
            except:
                finished=False
            
            todo=Todo(user=request.user,title=request.POST['title'],is_finished=finished)
            todo.save()
            messages.success(request,f'Successfully {request.user} added to do list')
                
    else:
        form=todo_form()
    to_dos=Todo.objects.filter(user=request.user)           
    if len(to_dos)==0:
        done_todos=True
    else:
        done_todos=False
            
    data={'to_do':to_dos,'done_todos':done_todos,
          'form':form}
    return render(request,'todo.html',data)
#------------------------------------------------------------------------------------
def update_todo(request,pk=None):
    todo=Todo.objects.get(id=pk)
    if todo.is_finished==True:
        todo.is_finished=False
    else:
        todo.is_finished=True
    todo.save()  
    return redirect('to_do')

#------------------------------------------------------------------------------------

def delete_todo(request,pk):
    Todo.objects.get(id=pk).delete()
    return redirect('to_do')
#------------------------------------------------------------------------------------

def books(request):
    result_list = []
    try:
        if request.method == 'POST':
            text = request.POST.get('text', '') 
            form = dashboardform(request.POST)

            url = f"https://www.googleapis.com/books/v1/volumes?q={text}"

            r = requests.get(url)
            
            # Check for a successful response
            if r.status_code == 200:
                answer = r.json()
                
                # Parse the 'items' key if it exists
                if 'items' in answer:
                    for item in answer['items']:
                        volume_info = item.get('volumeInfo', {})
                        result_dic = {
                            'title': volume_info.get('title', 'No Title'),
                            'subtitle': volume_info.get('subtitle', 'No Subtitle'),
                            'description': volume_info.get('description', 'No Description'),
                            'pageCount': volume_info.get('pageCount', 'No Page Count'),
                            'categories': ', '.join(volume_info.get('categories', ['No Categories'])),
                            'averageRating': volume_info.get('averageRating', 'No Rating'),
                            'thumbnail': volume_info.get('imageLinks', {}).get('thumbnail', 'No Thumbnail'),
                            'previewLink': volume_info.get('previewLink', 'No Preview Link')
                        }
                        result_list.append(result_dic)

            data = {'form': form, 'result': result_list}
            return render(request, 'books.html', data)

        else:
            # Handle GET requests
            form = dashboardform()
            data = {'form': form, 'result': result_list}
            return render(request, 'books.html', data)

    except Exception as e:
        # Handle exceptions gracefully
        print(f"Error: {e}")
        return render(request, 'books.html', {'form': dashboardform(), 'result': [], 'error': 'An error occurred while fetching data.'})

#-----------------------------------------------------------------------------------

def dic(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        form = dashboardform(request.POST)
        
        if text:
            url = f'https://api.dictionaryapi.dev/api/v2/entries/en_US/{text}'
            try:
                r = requests.get(url)
                r.raise_for_status()  
                answer = r.json()

                phonetics = answer[0].get('phonetics', [{}])[0].get('text', 'No phonetics available')
                audio = answer[0].get('phonetics', [{}])[0].get('audio', 'No audio available')
                definition = answer[0].get('meanings', [{}])[0].get('definitions', [{}])[0].get('definition', 'No definition available')
                example = answer[0].get('meanings', [{}])[0].get('definitions', [{}])[0].get('example', 'No example available')
                synonyms = answer[0].get('meanings', [{}])[0].get('definitions', [{}])[0].get('synonyms', '[]')

                data = {
                    'form': form,
                    'input': text,
                    'pho': phonetics,
                    'audio': audio,
                    'defi': definition,
                    'exam': example,
                    'syn': synonyms
                }

            except requests.exceptions.RequestException as e:
                data = {
                    'form': form,
                    'input': text,
                    'error': f'Failed to fetch data from the API: {str(e)}'
                }

            except (IndexError, KeyError) as e:
                data = {
                    'form': form,
                    'input': text,
                    'error': 'Error parsing API response. Data structure might have changed.'
                }

        else:
            data = {
                'form': form,
                'input': '',
                'error': 'No text provided.'
            }

        return render(request, 'dictionary.html', data)

    else:
        form = dashboardform()
        data = {'form': form}
        return render(request, 'dictionary.html', data)

                 
#-----------------------------------------------------------------------------------

def wiki(request):
    if request.method=="POST":
        text=request.POST['text']
        form=dashboardform(request.POST)
        search=wikipedia.page(text)
        data={'form':form,
              'title':search.title,
              'link':search.url,
              'details':search.summary
              }
        
        return render(request,'wiki.html',data)
    else:
      form=dashboardform()
      
    data={'form':form}
    return render(request,'wiki.html',data)
#-----------------------------------------------------------------------------------

def conv(request):
    return render(request,'conversion.html')
#-----------------------------------------------------------------------------------

def log_in(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})
#-----------------------------------------------------------------------------------

def profile(request):
    home_work=homework.objects.filter(user=request.user)
    if len(home_work)==0:
        Home_work_done=True
    else:
        Home_work_done=False
    
    todo=Todo.objects.filter(user=request.user)
    if len(todo)==0:
        todo_done=True
    else:
        todo_done=False
            
    data={'homework':home_work,
          'Home_work_done':Home_work_done,
          'todo':todo,
          'todo_done':todo_done}
    return render(request,'profile.html',data)

def delete_pro(request,pk=None):
    homework.objects.filter(id=pk).delete()
    return redirect('profile')

def delete_pro1(request,pk=None):
    Todo.objects.filter(id=pk).delete()
    return redirect('profile')

def register(request):
    if request.method =="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})


def log_out(request):
    logout(request)
    return redirect('login')


#----------------------------------------------------------------------------------

def chat(request):
    return render(request,'chat.html')

