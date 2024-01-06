from django.shortcuts import render,redirect
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate
from langchain.chains import SequentialChain
from CareerApp.models import RegistrationDB
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    if request.method == 'POST':
        input_text = request.POST.get('txt')

        # Your OpenAI API key
        openai_api_key = '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'

        # Create an OpenAI instance
        llm = OpenAI(openai_api_key=openai_api_key, temperature=0.8)

        # Define PromptTemplates
        first_input_prompt = PromptTemplate(input_variables=['Profession'], template='job description of {Profession}')
        chain1 = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='Job_Description')

        second_input_prompt = PromptTemplate(input_variables=['Profession'], template='what are the skills required for {Profession} and the qualifications required for {Profession}')
        chain2 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='Skills_and_Qualifications_Required')

        third_input_prompt = PromptTemplate(input_variables=['Profession'], template='what is the salary range for {Profession} in India')
        chain3 = LLMChain(llm=llm, prompt=third_input_prompt, verbose=True, output_key='Expected_Salary')

        fourth_input_prompt = PromptTemplate(input_variables=['Profession'], template='what is the scope of {Profession} in India and steps to be a {Profession} in India')
        chain4 = LLMChain(llm=llm, prompt=fourth_input_prompt, verbose=True, output_key='Scope_and_Steps_to_become_one')

        # Create a SequentialChain
        parent_chain = SequentialChain(
            chains=[chain1, chain2, chain3, chain4],
            input_variables=['Profession'],
            output_variables=['Job_Description', 'Skills_and_Qualifications_Required', 'Expected_Salary', 'Scope_and_Steps_to_become_one'],
            verbose=True
        )

        chatbot_responses = {}

        if input_text:
            # Get chatbot responses
            chatbot_responses = parent_chain({'Profession': input_text})
        print(chatbot_responses)
        context = {
            'input_text': input_text,
            'chatbot_responses': chatbot_responses,
        }

        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')



def register_pg(req):
    return render(req,"Register.html")

def register_save(request):
    if request.method=="POST":
        un=request.POST.get('Uname')
        em=request.POST.get('email')
        pwd=request.POST.get('password')
        reg=RegistrationDB(Username=un,Email=em,Password=pwd)
        reg.save()
        messages.success(request,"Registered Successfully")
        return redirect(Login_pg)

def Login_pg(req):
    return render(req,"Login.html")

def Login_Fn(request):
    if request.method=="POST":
        email=request.POST.get('em')
        passwd=request.POST.get('passwd')
        if RegistrationDB.objects.filter(Email=email,Password=passwd).exists():
            request.session['Email']=email
            request.session['Password']=passwd
            messages.success(request, "Logged-In Successfully")
            return redirect(home)
        else:
            messages.error(request, "Check Credentials")
            return redirect(Login_pg)
    else:
        messages.error(request, "Check Credentials")
        return redirect(Login_pg)

def Logout_fn(request):
    del request.session['Email']
    del request.session['Password']
    messages.success(request, "Logged-Out Successfully")
    return redirect(home)





def career_chatbot(request):
    if request.method == 'POST':
        input_text = request.POST.get('txt')

        # Assign the OpenAI API key
        openai_api_key = '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'

        first_input_prompt = PromptTemplate(input_variables=['query'], template='career information about {query}')

        # Create an instance of the OpenAI class with the API key as a named parameter
        llm = OpenAI(openai_api_key=openai_api_key, temperature=0.8)
        chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True)

        chatbot_response = None

        if input_text:
            chatbot_response = chain.run(input_text)

        context = {
            'input_text': input_text,
            'chatbot_response': chatbot_response,
        }
        print(chatbot_response)

        return render(request,'chatbot.html', context)
    else:
        return render(request,'chatbot.html')