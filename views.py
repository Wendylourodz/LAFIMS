        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')
        
        user = User.objects.create_user(username=username, password=password)
        messages.success(request, 'Registered successfully! You can now log in.')
        return redirect('login')
    
    return render(request, 'items/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('items:home')
        else:
            messages.error(request, 'Login failed! Invalid username or password!')
    
    return render(request, 'items/login.html')


def process(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('items:home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('items:login')  

    return render(request, 'items/login.html')


def home_view(request):
    return render(request, 'items/home.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirm_password')  

        if password != confirmpassword:
            messages.error(request, 'Passwords do not match!')
            return redirect('items:register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('items:register')

        User.objects.create_user(username=username, password=password, email=email)

        messages.success(request, 'Registration successful. Please log in.')
        return redirect('items:login') 

    return render(request, 'items/register.html')
